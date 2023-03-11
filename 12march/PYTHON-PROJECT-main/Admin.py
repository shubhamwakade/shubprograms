
admin_information = {"vishal":"vishal@0405"}

menu_list={1:{"foodId":1,"Foodname":"Pizza","Quantity":15,"Price":150,"Discount":5,"Stock":20},
           2:{"foodId":2,"Foodname":"Sandwich","Quantity":10,"Price":90,"Discount":4,"Stock":15},
           3:{"foodId":3,"Foodname":"Fried chicken","Quantity":5,"Price":110,"Discount":6,"Stock":10},
           }

# adding mew items ----
def add_new_items():
    item_id= int(input("Enter the foodId:"))
    item_name = input("Enter the food name:")
    item_quantity = int(input("Enter the quantity:"))
    item_price = int(input("Enter the price of food:"))
    item_discount = int(input("Enter the discount of food :"))
    item_stock = int(input("Enter the stock value of food:"))
    menu_list[item_id] = {
      "FoodId":item_id,
      "Foodname":item_name,
      "Quantity":item_quantity,
      "Price":item_price,
      "Discount":item_discount,
      "Stock":item_stock
      }
    print("The Item " + item_name +  "is added successfully")
    return menu_list


#Editing items-----
def edit_items():
    item = int(input("Enter the foodId which you want to edit:"))
    aa = input("Enter the Foodname:")
    bb = int(input("Enter the price of the item:"))
    cc = int(input("Enter the stock of the item:"))
    dd = int(input("Enter the discount of the item:"))
    ee = int(input("Enter the  Quantity of the item:"))
    menu_list[item]["Foodname"] = aa
    menu_list[item]["Price"] = bb
    menu_list[item]["Stock"] = cc
    menu_list[item]["Discount"] =dd
    menu_list[item]["Quantity"] = ee
    print(f"{item} Items Edited Successfully.......")
    return menu_list

# viewing inventory------

def view_items():
    print("******** HERE IS THE INVENTORY OF SAI SHRADDHA RESTURANTS *********")
    x = 0 
    for values in menu_list.values():
        x+=1
        print(x, values)



# Removing items--------
def remove_items():
    aa = int(input("Enter the foodId which you want to exit"))
    menu_list.pop(aa)
    print("Removed item successfully")
    return menu_list
