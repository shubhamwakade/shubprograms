
import adminfiles as adm
from user import User
import user
import ast
try: 
  select=input('''
  Welcome
  choose login type
  1.Admin
  2.User
  (enter Sl No.)
  ##Enter any other character to Exit##

  ''')
  if select== "1":
    username=input('Enter username of Admin: ')
    password=input('Enter password: ')

    if (username,password) in adm.admindict.items():
      print('You have successfully logged in.')
      print('What would you like to do?')
      admintf=True
      while admintf:
        adminstuff=input('''
        1.Add items to inventory
        2.Edit items in inventory
        3.Show items in inventory
        4.Remove items in inventory
        5.Exit
        (enter Sl. no)
        ''')
        if adminstuff=="1":
          adm.additem()
        elif adminstuff=="2":
          adm.edit()
        elif adminstuff=="3":
          adm.show()
        elif adminstuff=="4":
          adm.remove()
        elif adminstuff=="5":
          print('you are exiting.')
          admintf=False
        else:
          print('Wrong input.')

    else:
      print("You have entered wrong credentials.")


  elif select=="2":
    upf=True
    while upf:
      uporin=input('''Do you have an account?
    1.Yes
    2.No
    (Enter Sl. No)
    ''')


      if uporin=='2':
        print('''Lets create an account
        Enter following details''')
        user.signup()
        print('Account created succesfully.')
        upf=False
      elif uporin=='1':
        upf=False
      else:
        print('Wrong input. Try again.')

    print('Enter Login credentials.')

    username=input('Enter username: ')
    usernamecred=username
    password=input('Enter password: ')
    with open('loginfile.txt') as f:
      data=f.read()
    f.close()
    logindeets=ast.literal_eval(data)
    if username in logindeets:
      username=User(logindeets[username]['name'],logindeets[username]['address'],logindeets[username]['emailid'],logindeets[username]['phoneno'],logindeets[username]['username'],logindeets[username]['password'])



    if User.login(usernamecred,password):
      print('You have successfully logged in.')

      usertf=True
      while usertf:
        userstuff=input('''
        1.Place New Order
        2.Order History
        3.Update Profile
        ####Enter any key other key to exit####

        ''')
        if userstuff=="1":
          username.order()
        elif userstuff=="2":
          username.orderlist()
        elif userstuff=="3":
          username.change()
        else:
          print('You are exiting the app.')
          usertf=False

    else:
      print('''
      You have entered wrong credentials.
      Exiting application.''')

  else:
    print('You are exiting the application.')
except:
  print('Wrong Data type entered')
finally:
  print('End')
