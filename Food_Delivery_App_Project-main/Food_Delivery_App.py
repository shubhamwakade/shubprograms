import json
import datetime
from json.decoder import JSONDecodeError
def register_user(user_json,name,password,age,email,address,phn):
    user={
        "id":1,
        "name":name,
        "password":password,
        "age":age,
        "Email":email,
        "phone_number":phn,
        "address":address,
        "order history":{}
        }
    try:
        file=open(user_json,"r+")
        content=json.load(file)
        for i in range(len(content)):
            if content[i]["phone_number"]==phn:
                file.close()
                return "user already exists"
        else:
            user["id"]=len(content)+1
            content.append(user)
    except JSONDecodeError:
        content=[]
        content.append(user)

    file.seek(0)
    file.truncate()
    json.dump(content,file,indent=4)
    file.close()
    return "success"
def user_Order_History(user_json,user_id):
    file=open(user_json,"r+")
    content=json.load(file)
    for i in range(len(content)):
        if content[i]["id"]==user_id:
            print("order history")
            print("Date | Order")
            for i,j in content[i]["order history"].items():
                print(f"{i} | {j}")
            file.close()
            return True
    return False







count=0
def user_place_order(user_json, food_json, user_id, food_name, quantity):
    global count
    date = datetime.datetime.today().strftime('%m-%d-%Y')
    file = open(user_json, "r+")
    content = json.load(file)
    file1 = open(food_json, "r+")
    content1 = json.load(file1)
    flag=0
    food_price=0
    for i in range(len(content1)):
        if content1[i]["name"] == food_name:
            if content1[i]["no_of_plates"] >= quantity:
                for j in range(len(content)):
                    if content[j]["id"] == user_id:
                        content1[i]["no_of_plates"]-=quantity
                        if date not in content[j]["order history"]:
                            content[j]["order history"][date] = [content1[i]["name"]]
                            flag=1
                            count=count+1
                            food_price=content1[i]["price"]*quantity
                            print("Food_price:",food_price)
                        else:
                            content[j]["order history"][date].append(content1[i]["name"])
                            flag=1
                            count=count+1
                            food_price=content1[i]["price"]*quantity
                            print("Food_price:",food_price)
            else:
                print("Pls Enter less quantity")
                break   
    if flag==0:
        print("Order Not Available")
    elif(flag==1):
        print("Be Ready For Your Order") 
        if food_price>100:
            food_price_with_discount=food_price*0.2
            food_price=food_price-food_price_with_discount
            print("Congratulation you got 20 percent discount on Order paid only:",food_price,"rs")
        else:
            print("Sorry NO Dicount")
                     
    
        
        
    file.seek(0)
    file.truncate()
    json.dump(content, file, indent=4)
    file.close()
    
    file1.seek(0)
    file1.truncate()
    json.dump(content1, file1, indent=4)
    file1.close()

def update_userProfile(user_json,user_id,name,password,age,email,address,phn):
    print("Make Update")
    file=open(user_json,"r+")
    content=json.load(file)
    for i in range(len(content)):
        if content[i]["id"]==user_id:
            content[i]["name"]=name
            content[i]["password"]=password
            content[i]["age"]=age
            content[i]["Email"]=email
            content[i]["address"]=address
            content[i]["phone_number"]=phn
            print("updation Successfull")
        #else:
            #print("Enter valid User Id")
            #break
    file.seek(0)
    file.truncate()
    json.dump(content,file,indent=4)
    file.close()


 
    


#CURD operation for food
def add_food(food_json,food_name,price,no_of_plates=1,):
    food={
        "id":1 ,
        "name":food_name,
        "price":price,
        "no_of_plates":no_of_plates
    }
    try:
        fp=open(food_json,"r+")
        content=json.load(fp)
        for i in range(len(content)):
            if content[i]["name"]==food_name:
                fp.close()
                return "food already exists"
            
        food["id"]=len(content)+1
        content.append(food)
    except JSONDecodeError:
        content=[]
        content.append(food)
    fp.seek(0)
    fp.truncate()
    json.dump(content,fp,indent=4)
    fp.close()
    return "success"

def update_food(food_json, food_id,no_plates=-1, price=-1):
    file = open(food_json, "r+")
    content = json.load(file)
    for i in range(len(content)):
        if (content[i]["id"] == food_id):
            content[i]["no_of_plates"] += no_plates
            break
    file.seek(0)
    file.truncate()
    json.dump(content, file, indent=4)
    file.close()
    return "success"

def remove_food(food_json,food_id):
    file=open(food_json,"r+")
    content=json.load(file)
    for i in range(len(content)):
        if content[i]["id"] == food_id:
            del content[i]
            file.seek(0)
            file.truncate()
            json.dump(content,file,indent=4)
            file.close()
            return "sucess"
    return "please Enter valid food_id"

def read_food(food_json):
    file=open(food_json)
    content=json.load(file)
    print("MENU")
    for i in range(len(content)):
        print("Food_Id:",content[i]["id"])
        print(f"------>NAME:{content[i]['name']}")
        print(f"------->Price:{content[i]['price']}")
        print(f"------>Number of Plates available:{content[i]['no_of_plates']}")
    
    file.close()
    return True


val=input("Enter the Online food orderining System Y/n :")

while val.lower()=="y":
    print("MENU :")
    print("1) Register")
    print("2) Login")
    print("3) Exit")
    val1=input("choose one value from the above:")
    if val1=="1":
        print("-------REGISTER-------")
        name=input("Enter the Full name:")
        password=input("Enter the Password :")
        age=input("Enter your age :")
        email=input("Enter the Email address :")
        address=input("Enter the Residential address :")
        phn=input("Enter the Phn_no :")
        register_user("user.json",name,password,age,email,address,phn)
    elif val1 == "2":
        print("---------Login--------")
        while True:
            print("1)User")
            print("2)Admin")
            print("3)Exit")
            val2=input("choose on value from above")
            if val2 =="1":
                print("-------USER------")
                user=input("Enter Name :")
                password=input("Enter the Password :")
                file=open("user.json","r+")
                content=json.load(file)
                flag=0
                for i in range(len(content)):
                    if content[i]["name"]==user:
                        if content[i]["password"]==password:
                            flag=1
                            while True:
                                print()
                                print("Please View the Menu Before Place The Order")
                                print("PLEASE PLACE THE ORDER MORE THAN 100rs TO GET 20 PERCENT DISCOUNT")
                                print("1) View Menu")
                                print("2) Place Order")
                                print("3) History of food_order")
                                print("4) Update Profile")
                                print("5) Exit")
                                val3=input("User Enter Your Choice :")
                                if val3=="1":
                                    read_food("food.json")
                                elif val3=="2":
                                    print("Please Check the User_ID in User.json Then only put")
                                    user_id=int(input("Enter UserID :"))
                                    food_name=input("Enter the food want to eat :")
                                    quantity=int(input("enter the quantity of food :"))
                                    user_place_order("user.json", "food.json", user_id, food_name, quantity)
                                elif val3=="3":
                                    user_id=int(input("Enter UserID :"))
                                    user_Order_History("user.json",user_id)
                                elif val3=="4":
                                    user_id=int(input("Enter UserID :"))
                                    name=input("Enter the new User Name:")
                                    password=input("Enter the new Password:" )
                                    age=input("Updated Age:")
                                    email=input("Update Email address:")
                                    address=input("Update Residential Address:")
                                    phn=input("Enter the new phone number:")
                                    update_userProfile("user.json",user_id,name,password,age,email,address,phn)

                                else:
                                    print("Thanks for the Visit")
                                    break

                       # else:
                       #     print("please enter the correct password")

                    #else:
                        #   print("please enter the correct user name")
                if flag==0:
                    print("Please enter the correct USER NAME OR PASSWORD")

            elif val2=="2":
                print("$--------ADMIN------$")
                user=input("Enter Name :")
                password=input("Enter the Password :")
                file = open("admin.json", "r+")
                content = json.load(file)
                if content["name"] == user:
                    if content["password"] == password:
                        while True:
                            print()
                            print("1) Add New Food")
                            print("2) Edit Food")
                            print("3) View Food")
                            print("4) Remove Food") 
                            print("5) Exit")
                            val3 = input("Enter Your Choice Admin!!")
                            if val3 == "1":
                                food_name = input("Enter Food Name: ")
                                price=float(input("set the price"))
                                no_plates = int(input("Enter the Stock Value: "))
                                add_food("food.json", food_name,price, no_plates)
                            elif val3 == "2":
                                print("Please Check the Food_ID in food.json Then only put")
                                food_id =int(input("Enter Food ID: "))
                                no_plates = int(input("Enter the Stock Value: "))
                                update_food("food.json", food_id, no_plates)
                            elif val3=="3":
                                read_food("food.json")
                            elif val3=="4":
                                food_id=int(input("Enter FOODid :"))
                                remove_food("food.json",food_id)
                            else:
                                file.close()
                                print("%%%%Bye Bye%%%%%")
                                break
                    else:
                        print("Wrong Password!!")
                else:
                    print("Wrong Username!!")
            else:
                break
    else:
#--------------Exit--------------------#
        print("Thank you!!")
        break