import operations
import json
from json import JSONDecodeError

print("Welcome to Amazon app")
c=1
while c!=0:
    print("Press:")
    print("0: Exit")
    print("1: Register as Admin")
    print("2: Register as Member")
    print("3: Login as Admin")
    print("4: Login as Member")
    c=int(input())
    if c==1:
        print("Enter Full Name:")
        F=input()
        print("Enter Email:")
        E=input()
        print("Enter Password:")
        P=input()
        print("Enter Address:")
        A=input()
        if '@' in E and '.com' in E and len(P)!=0 and len(E)!=0 and len(A)!=0 and len(F)!=0:
            operations.Register('admin','members.json','admins.json',F,A,E,P)
            print("Registered Successfully as Admin !!")
        else:
            print("Please Enter Valid Data")
    elif c==2:
        print("Enter Full Name:")
        F=input()
        print("Enter Email:")
        E=input()
        print("Enter Password:")
        P=input()
        print("Enter Address:")
        A=input()
        if '@' in E and '.com' in E and len(P)!=0 and len(E)!=0 and len(A)!=0 and len(F)!=0:
            ch=operations.Register('member','members.json','admins.json',F,A,E,P)
            if ch==True:
                print("Registered Successfully as Member !!")
            else:
                print("Registration Unsuccessful")
        else:
            print("Please Enter Valid Data")
    elif c==3:
        print("Enter Email")
        E=input()
        print("Enter Password")
        P=input()
        success=operations.Login('admin','members.json','admins.json',E,P)
        if success==True:
            temp=open('admins.json','r')
            adms=json.load(temp)
            owner_details=[]
            for i in range(len(adms)):
                if adms[i]["Email"]==E and adms[i]["Password"]==P:
                    owner_details.append(adms[i])
                    break
            while True:
                print("Press: ")
                print("1: Create Product")
                print("2: View Products List")
                print("3: Update Product")
                print("4: Delete Product")
                print("0: Logout")
                in1=int(input())
                if in1==1:
                    p_id=operations.AutoGenerate_ProductID()
                    print("Product ID generated is "+str(p_id))
                    print("Enter Product Name: ")
                    Product_Name=input()
                    print("Enter Manufacturer Name: ")
                    Manufacturer_Name=input()
                    print("Enter Price: ")
                    Product_Price=input()
                    print("Enter Discount: ")
                    Product_Discount=input()
                    if '%' not in Product_Discount:
                        Product_Discount+="%"
                    print("Enter Available Stock: ")
                    Product_Stock=input()
                    try:
                        int(Product_Price)
                    except ValueError:
                        Product_Price=""
                    try:
                        int(Product_Stock)
                    except ValueError:
                        Product_Stock=""
                    if len(p_id)!=0 and len(Product_Name)!=0 and len(Product_Price)!=0 and len(Product_Discount)!=0 and len(Product_Discount)!=0 and len(Product_Stock)!=0:
                        ch=operations.Create_Product(owner_details[0]["Full Name"],'products.json',p_id,Product_Name,Manufacturer_Name,int(Product_Price),Product_Discount,int(Product_Stock))
                        if ch==True:
                            print("Product successfully created !!")
                        else:
                            print("Product creation unsuccessful, Please Enter Valid Data")
                    else:
                        print("Product creation unsuccessful, Please Enter Valid Data")
                elif in1==2:
                    print("Press :")
                    print("1: View All Products")
                    print("2: View Product by Product ID")
                    in2=int(input())
                    if in2==1:
                        l=operations.Read_Products(owner_details[0]["Full Name"],'products.json')
                        if len(l)==0:
                            print("No products created till now!!")
                        else:
                            for i in range(len(l)):
                                print("Product ID: "+str(l[i]["Product ID"]))
                                print("Product Name: "+str(l[i]["Product Name"]))
                                print("Manufacturer Name: "+str(l[i]["Manufacturer Name"]))
                                print("Price: "+str(l[i]["Price"]))
                                print("Discount: "+str(l[i]["Discount"]))
                                print("Stock Available: "+str(l[i]["Total Stock Available"]))
                    elif in2==2:
                        print("Enter Product ID :")
                        pr_id=input()
                        dtls=[]
                        operations.Read_Product_By_ID('products.json',pr_id,dtls)
                        if len(dtls)==0:
                            print("Invalid ID")
                        else:
                            print("Product Name: "+str(dtls[i]["Product Name"]))
                            print("Manufacturer Name: "+str(dtls[i]["Manufacturer Name"]))
                            print("Price: "+str(dtls[i]["Price"]))
                            print("Discount: "+str(dtls[i]["Discount"]))
                            print("Stock Available: "+str(dtls[i]["Total Stock Available"]))
                    else:
                        print("Invalid  Choice")
                elif in1==3:
                    print("Enter Product ID: ")
                    prd_id=input()
                    print("Enter Detail to be udpdated: ")
                    detail_tbu=input()
                    print("Enter Updated detail: ")
                    u_detail=input()
                    dn=operations.Update_Product('products.json',prd_id,detail_tbu,u_detail)
                    if dn==True:
                        print("Product Update Successfully")
                    else:
                        print("Invalid Product Detail")
                elif in1==4:
                    print("Enter Product ID: ")
                    pr_id=input()
                    dn=operations.Delete_Product('products.json',pr_id)
                    if dn==True:
                        print("Product Deleted Successfully")
                    else:
                        print("Invalid Product ID")
                elif in1==0:
                    break
                else:
                    print("Invalid Choice")
        else:
            print("Invalid Credentials")
    elif c==4:
        print("Enter Email")
        E=input()
        print("Enter Password")
        P=input()
        success=operations.Login('member','members.json','admins.json',E,P)
        if success==True:
            temp=open('members.json','r')
            mems=json.load(temp)
            member_details=[]
            for i in range(len(mems)):
                if mems[i]["Email"]==E and mems[i]["Password"]==P:
                    member_details.append(mems[i])
                    break
            while True:
                print("Press: ")
                print("1: Create New Order")
                print("2: View Order History")
                print("3: Update Profile")
                print("4: Logout")
                in3=int(input())
                if in3==1:
                    temp=open('products.json','r')
                    try:
                        content=json.load(temp)
                        temp.close()
                        print("Products Available:")
                        for i in range(len(content)):
                            print(content[i]["Product ID"])
                        print("Enter Product ID")
                        id_pr=input()
                        print("Enter Quantity")
                        q=int(input())
                        o_id=operations.AutoGenerate_OrderID()
                        ch=operations.Place_Order('orders.json',member_details[0]["Full Name"],member_details[0]["Address"],'products.json',id_pr,q,o_id)
                        if ch==True:
                            print("Order Successfully Placed with order id: "+str(o_id))
                        else:
                            print("Order Unsuccessful")
                    except JSONDecodeError:
                        print("No Products Available")
                elif in3==2:
                    l=[]
                    operations.Order_History('orders.json',member_details[0]["Full Name"],l)
                    if len(l)==0:
                        print("No orders Placed Yet !!")
                    else:
                        for i in range(len(l)):
                            print("Order ID: "+str(l[i]["Order ID"]))
                            print("Product Name: "+str(l[i]["Product Name"]))
                            print("MRP: "+str(l[i]["Price"]))
                            print("Discount: "+str(l[i]["Discount"]))
                            print("Price after Discount: "+str(l[i]["Price after Discount"]))
                            print("Quantity: "+str(l[i]["Quantity"]))
                            print("Grand Total: "+str(l[i]["Total Cost"]))
                            print("Delivering to: "+str(l[i]["Delivering to"]))
                elif in3==3:
                    print("Enter Detail to be updated: ")
                    dtl_tbu=input()
                    print("Enter Update Detail: ")
                    up_dtl=input()
                    ch=operations.Update_Member('members.json',member_details[0]["Full Name"],dtl_tbu,up_dtl)
                    if ch==True:
                        print("Detail Updated Successfully !!")
                    else:
                        print("Invalid Detail")
                elif in3==4:
                    break
                else:
                    print("Invalid Choice")
        else:
            print("Invalid Credentials")
    elif c==0:
        break
    else:
        print("Invalid Choice")