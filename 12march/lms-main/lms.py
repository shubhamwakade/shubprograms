# MINI PROJECT LMS 
class LMS:
    """"This class is used to keep record libaray book"""
    def __init__(self,listOfBooks,libaryName):
        self.listOfBooks=listOfBooks
        self.libaryname=libaryName
        self.bookDict={}
        id=101

        with open(self.listOfBooks) as file:
            content=file.readlines()

        for line in content:
            self.bookDict.update({str(id):{"books_title":line.replace("\n",""),
            'lender_name':'',"status":'Available'}})
            id+=1

    def display_books(self):
        print("----------List of books-----------")
        print("bookId \t\t Title")
        print("----------------------------------")

        for key,value in self.bookDict.items():
            print(key,"\t\t",value.get("books_title"),"[",value.get("status"),"]")


    def issue_books(self):
        bookId=input("Enter A BookId:")
        if bookId in self.bookDict.keys():
            if not self.bookDict[bookId]["status"]=="Available":
                print(f"This book is  already issued to {self.bookDict[bookId]['lender_name']} ans bookId is {bookId}")
            elif self.bookDict[bookId]["status"]=="Available":
                name=input("Enter Your name:")
                self.bookDict[bookId]["lender_name"]=name
                self.bookDict[bookId]["status"]="Already Issued"
                print("Book issued sucessfully")
        else:
            print("book id not found")

    def add_books(self):
        new_book=input("Enter a book name:")
        if new_book=='':
            return self.add_books()
        else:
            with open(self.listOfBooks,"a") as file_update:
                file_update.writelines(f'{new_book}\n')
                self.bookDict.update({str(int(max(self.bookDict))+1):{'books_title':new_book,
                'lender_name':'','status':'Available'}})
        print(f'the book {new_book} has been added sucessfully')      
    
    def return_books(self):
        bookId=input("Enter A BookId:")
        if bookId in self.bookDict.keys():
            if  self.bookDict[bookId]["status"]=="Available":
                print(f"This book is  already Available in libaray,please check the bookId")
                return self.return_books()
            elif not self.bookDict[bookId]["status"]=="Available":
                self.bookDict[bookId]["lender_name"]=''
                self.bookDict[bookId]["status"]="Available"
                print("Book update sucessfully")
        else:
            print("book id not found")
try:
    lms=LMS("lms_file.txt","Python LMS")
    press_key_list={"D":"Display book","I":"Issued book","A":"Added book","R":"Return book","Q":"Quit"}

    key_press=False

    while not (key_press =="q"):
        print("--------Welcome to LMS--------")
       
        for key,value in press_key_list.items():
           print("press",key,"To",value)
        key_press=input("Press key:").upper()
        if key_press=="I":
            print("\ncureent selection:Issued book\n")
            lms.issue_books()
        elif key_press=="D":
            print("\ncureent selection:Display book\n")
            lms.display_books()
        elif key_press=="A":
            print("\ncureent selection:Added book\n")
            lms.add_books()
        elif key_press=="R":
            print("\ncureent selection:Return book\n")
            lms.return_books()

except Exception as e:
    print(e)


