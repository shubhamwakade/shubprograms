import Admin as vv
from User import Customer
user = Customer(str,str,str,str,str)
Temp_variable = 1
Temp  = True
Temp_var = True
while Temp_var:
    inp = int(input("Where you want to login select, 1.Admin   2 .User   3.User Registration  4.Exit"))
    if Temp_variable == 0:
        Temp=True
    if inp == 1:
        Username = input("Enter the username of admin: ")
        password = input("Enter the password of admin: ")
        if vv.admin_information[Username] == password:
            print(f"you 're logged in succesfully {Username}......")
            admin_crawler= True
            while admin_crawler:
                admin_choice = int(input("Choose the option of admin panel 1.ADD NEW ITEMS 2.EDIT ITEMS 3.VIEW ITEMS 4.REMOVE ITEMS 5. EXIT"))
                if admin_choice == 1:
                    vv.add_new_items()
                elif admin_choice == 2:
                        vv.edit_items()
                elif admin_choice == 3:
                        vv.view_items()
                elif admin_choice == 4:
                       vv.remove_items()
                elif admin_choice   == 5:
                        admin_crawler = False
                        print(f"you are exit from the admin panel{Username}")
                else:
                        print("This is the invalid option please select the valid option...")
        else:
            print("These are the wrong credentials! SORRY please check again....")

    elif inp == 2:
        print("Welcome to the User panel")
        email_enter = input("Enter the username:")
        password = input("Enter the password:")
            
        if Customer.login_info[email_enter] == password:
            print(f" You are successfully logged{email_enter}")
        User_crawler = True
        while User_crawler:
            user_choice = int(input(f"{email_enter},Enter the option 1.place new order 2.order history 3.update profile 4.Exit"))
            if user_choice ==1:
                user.place_order()
                    
            elif user_choice ==2:
                user.order_history_see()
            
            elif user_choice == 3:
                user.update_profile()

            elif user_choice == 4:
                User_crawler = False
                print("You are successfully logged out.....")
            else:
                print("You choose the invalid option")
        else:
            print("These are the wrong credentials! SORRY")

    elif inp ==3:
        new_email = input("Enter the Email:")
        if new_email in user.login_info.keys():
            print("Email Already Registered..")
        else:
            print("Enter your Details....")
            new_name = input("Enter the name:")
            new_phone_no = int(input("Enter the number:"))
            new_address = input("Enter the address:")
            new_password = input("Enter the password:")
            user = Customer (new_email,new_name,new_phone_no,new_address,new_password)
            print("Registered successfully")
            print("Now you  can login....")

    elif inp == 4:
        exit()
    else:
        print("select proper options...")




