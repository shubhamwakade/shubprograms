import adminfiles as ad
import random
import ast

with open('loginfile.txt') as f:
    data = f.read()
f.close()

logindeets = ast.literal_eval(data)

def signup():
  
  name=input('Full Name: ')
  address=input('Address: ')
  phoneno=input('Phone number: ')
  emailid=input('Email ID: ')
  userver=True
  while userver:
    a=input('Username: ')
    if a in logindeets:
      print("Username already exists. Choose another username.")
    else:
      username=a
      userver=False
  password=input('Password: ')
  userdeet={username:          
  {'name':name,
  'address':address,
  'phoneno':phoneno,
  'emailid':emailid,
  'username':username,
  'password':password}
  }
  logindeets.update(userdeet)
  a=open('loginfile.txt','w+')
  a.write(str(logindeets))
  a.close()

  
class User(object):
  logincred={}
  costdict={}
  ordid=[]
  def __init__(self,name,address, emailid,phoneno,username, password):
    self.name=name
    self.address=address
    self.emailid=emailid
    self.phoneno=phoneno
    self.username=username
    self.password=password
    User.logincred[self.username]=self.password 
    self.profile={'Name: ',name}
    self.orderhistory={}
      
  @classmethod
  def login(cls,username,password):
    if cls.logincred.get(username)==password:
      return True
    else:
      return False

  def change(self):
    changetf=True
    while changetf:
      changeid=input('''What do you want to change? 

    1.Name
    2.Address
    3.Phone no
    4.Email
    5.Password
    6.No change/Exit updating details
    (Enter Sl No.)
    ''')
      changeidup=changeid.upper()
      if changeidup=='1':
        newname=input('New Name: ')
        self.name=newname
      elif changeidup=='2':
        newad=input('New Address: ')
        self.address=newad
      elif changeidup=='3':
        newph=input('Enter Phone Number: ')
        self.phoneno=newph
      elif changeidup=='4':
        newemail=input('Enter Mail ID: ')
        self.emailid=newemail
      elif changeidup=='5':
        newpwd=input('Enter New Password: ')
        self.password=newpwd
      elif changeidup=='6':
        print('No changes made/Exiting update tab.')
        changetf=False
      else:
        print('Wrong input.')

  def order(self):
    print('Welcome')
    ad.displayuser()
    askorder=input('''
    Do you want to order? 
    Y/N: ''')

    askorderstr=askorder.upper()
    if askorderstr=='Y':
      x=0
      orderp={}
      askorderT=True
      while askorderT:
        current_order={}
        orderidtf=True
        while orderidtf:
          orditem=input('Enter Item ID of the Item you want to order: ')
          if orditem in ad.inventory and orditem not in orderp:
            orderidtf=False
          else:
            print('\nItem ID not present in the Items or Item already in cart.\n')
        ordno=int(input('Enter Quantity of items you need: '))
        x+= ad.inventory[orditem]['discounted price']*ordno
        current_order={orditem:{'Item Name':ad.inventory[orditem]['itname'],
            'Quantity':ordno}
            }
        orderp.update(current_order)

        askagaintf=True
        while askagaintf:
          askagain=input('''
        Do you want to change/add more items? Y/N: 
        ''')
          askagainup=askagain.upper()
          if askagainup=='Y':
            print('Select your next item.')
            askagaintf=False
          elif askagainup=='N':
            if User.ordid==[]:
              a=1
            else:
              a=max(User.ordid)+1
            User.ordid.append(a)
            order={'Orderid: {}'.format(a):orderp}
            for i in order:
              b=order[i]
              for j in b:
                c=b[j]
                print('\nItem Name: ',c['Item Name'])
                print('Quantity:', c["Quantity"])
            cost={'Orderid: {}'.format(a):x}
            User.costdict.update(cost)
            print('The bill is ',x,' Rupees\n')
            askorderT,askagaintf= False,False
          else:
            print('Wrong Input')
      
      confirmtf=True
      while confirmtf:
        confirm=input('Would you like to confirm order? Y/N: ')
        confirmup=confirm.upper()
        if confirmup=='Y':
            print('Your order is confirmed.')
            self.orderhistory.update(order)

            confirmtf=False
        elif confirmup=='N':
            print('Your Order is cancelled.')
            order.clear()
            confirmtf=False
        else:
            print('Wrong Input.')
    
    elif askorderstr=='N':
      print('No orders taken.')
    else:
      print('Wrong Input.')
  
  def orderlist(self):
    print('Your orders are:\n')
    orderhist=self.orderhistory
    x=1
    for i in orderhist:
      print('Order',x)
      x+=1
      b=(orderhist[i])
      for j in b:
        c=b[j]
        print('Item Name: ',c['Item Name'])
        print('Quantity:', c["Quantity"])
        print('Cost:',User.costdict[i], 'Rupees\n' )
 