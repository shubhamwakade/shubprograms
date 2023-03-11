import ast
admindict={'admin':'admin','vinu':'vinu'}
with open("inventoryfile.txt") as f:
  data=f.read()
f.close()
inventory=ast.literal_eval(data)

def additem():
  if inventory=={}:
    itemid=1
  else:
    a=[]
    for i in inventory:
      j=int(i)
      a.append(j)
      itemid=max(a)
      itemid+=1
  itemname=input('Enter Item name: ')
  unit=input('Enter Unit No: ')
  price=int(input('Enter Price per Unit: '))
  discounttf=True
  while discounttf:
    a=int(input('Enter Discount per unit: '))
    if price>a:
      discount=a
      discounttf=False
    else:
      print('Error. Discount value given lower than Price. Try again.')
  stock=input('Stock Availability: ')
  inventory[str(itemid)]={
      'itname':itemname,
      'itemid':str(itemid),
      'per unit':unit,
      'price':price,
      'Discount':discount,
      'discounted price':price-discount,
      'stock':stock
  }
  a=open("inventoryfile.txt",'w')
  a.write(str(inventory))
  a.close()
  print('Item added Successfully')
  return inventory

def edit():
  edittf=True
  while edittf:
    edititem=input('Enter Item ID of the Item you needs to edit: ')
    if edititem in inventory:
      edittf=False
    else:
      print('''
      Item ID not present in the inventory.''')
      show()

  inventory[edititem]['itname']=input('Enter Item name: ')
  inventory[edititem]['per unit']=input('Enter Unit No: ')
  inventory[edititem]['price']=int(input('Enter Price per unit: '))
  discounttf=True
  while discounttf:
    a=int(input('Enter Discount per unit: '))
    if inventory[edititem]['price']>a:
      inventory[edititem]['Discount']=a
      discounttf=False
    else:
      print('Error. Discount value given lower than Price. Try again.')
  inventory[edititem]['discounted price']=inventory[edititem]['price']-inventory[edititem]['Discount']
  inventory[edititem]['stock']=input('Stock Availability: ')
  a=open("inventoryfile.txt",'w')
  a.write(str(inventory))
  a.close()
  print('Edited Item Successfully')
  return inventory

def show():
  print('Here are the Items available in Inventory.')
  for i in inventory:
    print(' Item ID', inventory[i]['itemid'],'\n',
        'Item Name:',inventory[i]['itname'],'\n',
          'Price','INR {}'.format(inventory[i]['price']),' per', inventory[i]['per unit'],'\n',
          'Discounted Price','INR {}'.format(inventory[i]['discounted price']),' per', inventory[i]['per unit'],'\n',
          'Stock Availability',inventory[i]['stock'],'\n')
def displayuser():
  for i in inventory:
    print(' Item ID', inventory[i]['itemid'],'\n',
        'Item Name:',inventory[i]['itname'],'\n',
          'Price','INR {}'.format(inventory[i]['price']),' per', inventory[i]['per unit'],'\n',
          'Discounted Price','INR {}'.format(inventory[i]['discounted price']),' per', inventory[i]['per unit'],'\n')    
def remove():
  remtf=True
  while remtf:
    rem=input('Enter Item ID of the Item you needs to remove: ')
    if rem in inventory:
      remtf=False
    else:
      print('Item ID not present in the inventory.')
      show()

  inventory.pop(rem)
  a=open("inventoryfile.txt",'w')
  a.write(str(inventory))
  a.close()
  print('Removed Item Successfully')
  return inventory
