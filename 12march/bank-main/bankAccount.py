from mainAccount import *

choice = input(" Do you want proceeded Y/N:")
if choice.lower() == 'y':
    pin = int(input("Enter your pin:"))
    x = Account(pin)
    if x.Validate_pin():
        print("Pin Confirmed!!")
        print("Select Account Type")
        print("1)Checking Account")
        print("2)Saving Account")
        print("3)Busniness Account")
        Account_Type = input("Please select one of the above:")
        logic_setter=Atm_Logic("")
        if Account_Type == "1":
            logic_setter.CheckingAccount_Functions()
        elif Account_Type == "2":
            logic_setter.SavingAccount_Functions()
        elif Account_Type == "3":
            logic_setter.BusniessAccount_Functions()

    else:
        print("Pin Invalid!! Please Try Again")
