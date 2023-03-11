import Admin as vv

class Customer:
    login_info = {"vishalkobarne0405@gmail.com":"vishal@123"}
    def __init__(self,email,name,phone_no,address,password):
        self.email = email
        self.name = name
        self.phone_no = phone_no
        self.address = address
        self.password = password
        self.profile = {"Name":name}
        Customer.login_info[self.email] =self.password
        self.order_history = {}
        
    

    def place_order(self):
        print("What do you want to order from the resturant")
        print(vv.view_items())
        user_choice = input("If you want to order then select 1.YES 2.NO ")
        if user_choice =="YES":
            n = int(input("Enter how many items do you want to order ?"))
            Bill = 0
            Discount_on_bill = 0
            for i in range(n):
                itemid = int(input("Enter the itemid  here:"))
                quan = int(input("Enter the quantity of the item:"))
                Bill = Bill + vv.menu_list[itemid]["Price"]*quan
                Discount_on_bill = Discount_on_bill +vv.menu_list[itemid]['Discount'] 
                vv.menu_list[itemid]['Stock'] = vv.menu_list[itemid]['Stock'] - quan
                self.order_history[itemid] = {
                    "Name" :vv.menu_list[itemid]["Foodname"],
                    "Price":vv.menu_list[itemid]["Price"],
                    "Quantity":quan
                    }
                again_ask =  input("Your order is confirmed ! Are you still want to order Enter YES otherwise NO")
                if again_ask =="YES":
                
                    print(f"Discount on your bill is {Discount_on_bill}")
                    print(f"After Deduced Discount on bill is its cost is  {Bill-Discount_on_bill} INR in total")
                    print(f"This is your quantity{quan}")

                elif again_ask == "NO":
                    print("Your order has been cancelled")
                    self.order_history.clear()
                else:
                    print("Invalid choice")
        elif user_choice == 2:
            print("You selected 2 option so we cancelled this..")
        else:
            print("Invalid no")
    
    def order_history_see(self):
        print(self.order_history)

    def update_profile(self):
        print("you can update your profile from here...")
        email = input("Enter your email id")
        if email in Customer.login_info.keys():
            print("Email Matched.....")
            del Customer.login_info[email]

            new_email = input("Enter the new Email:")
            new_name = input("Enter the  new name")
            new_phone_no = int(input("Enter the  new phone number:"))
            new_Adresss = input("Enter the new Addresss:")
            new_password = input("Enter the new password:")

            Customer .login_info[new_email] = {'email':new_email,
            "name":new_name,
            "phone_no":new_phone_no,
            "address":new_Adresss,
            "password":new_password
            }
            print("Profile updated successfully....")
        else:
            print("Email not registered.....")
    @classmethod
    def login(cls,enter_email,password):
            if enter_email in cls.login_info.keys():
                if cls.login_info.get(enter_email)['Password'] == password:
                    print("logged in successfully")
                    return True
                else:
                    print("Something went wrong ...")
            else:
                print(f"{enter_email} this email is not registered yet..please try again.....")
                return False
