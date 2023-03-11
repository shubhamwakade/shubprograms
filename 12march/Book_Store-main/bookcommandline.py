import bookstore
import json
from json import JSONDecodeError

print("Welcome to book library")
tp=open('admin.json','r+')
try:
    cp=json.load(tp)
    if 'admin@edyoda.com' not in str(cp):
        bookstore.Register('admin','admin.json','user.json','admin','admin@edyoda.com','admin')
    tp.close()
except JSONDecodeError:
    bookstore.Register('user','admin.json','user.json','admin','admin@edyoda.com','admin')
c=1
while True:
    print("Press:")
    print("1: Register")
    print("2: Login")
    print("0: Exit")
    try:
        c=int(input())
    except ValueError:
        print("Please enter valid choice")
        continue
    if c == 1:
            print("Press :")
            print("1: Register as admin")
            print("2: Register as user")
            try:
                in1 = int(input())
            except ValueError:
                print("Please enter valid choice")
            if in1 == 1:
                print("Enter Full Name:")
                F = input()
                print("Enter Email:")
                E = input()
                print("Enter Password:")
                P = input()
                if (len(F) * len(E) * len(P)) == 0 or '@' not in E or '.com' not in E:
                 print("Please enter valid data")
                 continue
                else:
                 bookstore.Register('admin', 'admin.json', 'user.json', F, E, P)
                 print("Registered successfully as admin")
            elif in1 == 2 :
             print("Enter Full Name:")
             F = input()
             print("Enter Email:")
             E = input()
             print("Enter Password:")
             P = input()
             if (len(F) * len(E) * len(P)) == 0 or '@' not in E or '.com' not in E:
                print("Please enter valid data")
                continue
            else:
                bookstore.Register('user', 'admin.json', 'user.json', F, E, P)
                print("Registered successfully as user")
    elif c == 2:
        print("Press: ")
        print("1: Login as admin")
        print("2: Login as user")
        try:
            in1 = int(input())
        except ValueError:
            print("Please enter valid choice")
        if in1 == 1:
            print("Enter Email:")
            E = input()
            print("Enter Password:")
            P = input()
            s = bookstore.Login('admin','user.json', 'admin.json', E, P)
            if s == False:
                print("Invalid Credentials")
                continue
            else:
                t = open('organizers.json', 'r')
                cnt = json.load(t)
                t.close()
                n = ""
                for i in range(len(cnt)):
                 if cnt[i]["Email"] == E and cnt[i]["Password"] == P:
                    n = cnt[i]["Full Name"]
                    break
                print("Welcome " + str(n))
                while True:
                        print("Press :")
                        print("1: Create book")
                        print("2: Retrive all books created")
                        print("3: View books Details by ID")
                        print("4: Update book")
                        print("5: Delete book")
                        print("0: Logout")
                        try:
                            i1 = int(input())
                        except ValueError:
                            print("Please enter valid choice")
                        if i1==1:
                            book_ID = bookstore.AutoGenerate_EventID()
                            print("Book ID Generated - " + str(book_ID))
                            nme = input("bookname")
                            ad = input("admin name")
                            ab = int(input("aviable books"))
                            bookstore.Create_book('bookfile.json', book_ID,nme,ad,ab)
                            print("book created successfully")
                        elif i1 == 2:
                            print("Enter book ID")
                            ev_id = input()
                            f14 = open('bookfile.json', 'r')
                            try:
                                c14 = str(json.load(f14))
                                if ev_id not in c14:
                                    print("Invalid event ID")
                                    continue
                            except JSONDecodeError:
                                print("Book not available")
                                continue
                            d = bookstore.View_books('events.json', ev_id)
                            print("book Name: " + str(d[0]['Name']))
                            print("Seats Available: " + str(d[0][' book Available']))
                            print('\n')
                        elif i1 == 4:
                            print("Enter book ID:")
                            _id = input()
                            print(
                                "Enter detail to be Updated ( Name ||  Books Availblity ): ")
                            dtl = input("which one want to update")
                            udtl = input("updated")
                            f11 = open('bookfile.json', 'r')
                            try:
                                c11 = str(json.load(f11))
                                f11.close()
                            except JSONDecodeError:
                                print("No book created")
                                f11.close()
                                continue
                            if _id not in c11:
                                print("Invalid book ID")
                                continue
                            else:
                                ch = bookstore.Update_book('bookfile.json',_id, dtl,udtl )
                                if ch == False:
                                  print("Cannot update book")
                                else:
                                  print("book updated successfully")
                        elif i1 == 5:
                            print("Enter book ID")
                            book_id = input()
                            f1 = open('bookfile.json', 'r')
                            try:
                                c1 = str(json.load(f1))
                                f1.close()
                            except JSONDecodeError:
                                print("No book created")
                                f1.close()
                                continue
                            if book_id not in c1:
                                print("Invalid book ID")
                                continue
                            if len(book_id) == 0:
                                print("Please enter valid data")
                                continue
                            else:
                                o1 = bookstore.Delete_book( 'bookfile.json', book_id)
                            if o1 == True:
                                print("book deleted successfully")
                            else:
                                print("Cannot delete book")
                        elif i1 == 0:
                                break
                        else:
                            print("Ivalid Option")