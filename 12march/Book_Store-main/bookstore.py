
import json
from operator import truediv
import string
import random
from json import JSONDecodeError
from datetime import datetime,date
from turtle import st, update
import mysql.connector

def AutoGenerate_EventID():
    #generate a random Event ID
    book_ID = ''.join(random.choices(string.ascii_uppercase+string.digits,k=3))
    return book_ID

def Register(type,user_json_file,admin_json_file,Full_Name,Email,Password):
    '''Register the member/ogranizer based on the type with the given details'''
    if type.lower()=='admin':
        f=open(admin_json_file,'r+')
        d={
            "Full Name":Full_Name,
            "Email":Email,
            "Password":Password
        }
        try:
            content=json.load(f)
            if d not in content:
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content, f)
        except JSONDecodeError:
             l = []
             l.append(d)
             json.dump(l, f)
        f.close()
    else:
           f = open(user_json_file, 'r+')
           d = {
               "Full Name": Full_Name,
               "Email": Email,
               "Password": Password
           }
           try:
               content = json.load(f)
               if d not in content:
                   content.append(d)
                   f.seek(0)
                   f.truncate()
                   json.dump(content, f)
           except JSONDecodeError:
               l = []
               l.append(d)
               json.dump(l, f)
           f.close()
def Login(type,admin_json_file,user_json_file,Email,Password):
    '''Login Functionality || Return True if successful else False'''
    d=0
    if type.lower()=='admin':
        f=open(admin_json_file,'r+')
    else:
        f=open(user_json_file,'r+')
    try:
        content=json.load(f)
    except JSONDecodeError:
        f.close()
        return False
    for i in range(len(content)):
        if content[i]["Email"]==Email and content[i]["Password"]==Password:
            d=1
            break


def Create_book(booksfile,book_ID,book_Name,admin_Registered,Availability):
    f=open(booksfile,'r+')
    d={
            "ID":book_ID,
            "Name":book_Name,
            "admin Registered":admin_Registered,
            "books Available":Availability,

        }
    try:
         content=json.load(f)
         if d not in content:
            content.append(d)
            f.seek(0)
            f.truncate()
            json.dump(content, f)

    except JSONDecodeError:
          l = []
          l.append(d)
          json.dump(l, f)
          f.close()


def View_books(book_ID, bookfile):
    file = open(bookfile, 'r+')
    content = json.load(file)
    d = []
    for i in range(len(content)):
        if content[i]["ID"] == book_ID:
            d.append(content[i])
    file.close()
    return d


    '''Return a list of all books created by the logged in admin'''

def Update_book(bookfile,book_id, detail_to_be_updated, update_detail):
    file=open(bookfile,'r+')
    content=json.load(file)
    for i in range(len(content)):
        if content[i]["ID"]==book_id:
            if detail_to_be_updated=='Name':
                content[i]['Name']=update_detail
            elif detail_to_be_updated=='book Available':
                content[i]['book Available']=update_detail
            else:
                return False
            file.seek(0)
            file.truncate()
            json.dump(content,file)
            file.close()

def Delete_book(bookfile,book_ID):
    file=open(bookfile,'r+')
    content=json.load(file)
    id= book_ID
    print(content[0]["ID"]==book_ID)
    for i in range(len(content)):
        if content[i]["ID"]==book_ID:
            del content[i]
            file.seek(0)
            file.truncate()
            json.dump(content, file)
            file.close()
            return True
        else:
            pass
