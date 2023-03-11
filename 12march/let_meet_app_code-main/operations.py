import json
import string
import random
from json import JSONDecodeError
from datetime import datetime,date

def AutoGenerate_EventID():
    #generate a random Event ID
    Event_ID=''.join(random.choices(string.ascii_uppercase+string.digits,k=3))
    return Event_ID

def Register(type,member_json_file,organizer_json_file,Full_Name,Email,Password):
    '''Register the member/ogranizer based on the type with the given details'''
    if type.lower()=='organizer':
        f=open(organizer_json_file,'r+')
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
                json.dump(content,f)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
        f.close()
    else:
        f=open(member_json_file,'r+')
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
                json.dump(content,f)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
        f.close()


def Login(type,members_json_file,organizers_json_file,Email,Password):
    '''Login Functionality || Return True if successful else False'''
    d=0
    if type.lower()=='organizer':
        f=open(organizers_json_file,'r+')
    else:
        f=open(members_json_file,'r+')
    try:
        content=json.load(f)
    except JSONDecodeError:
        f.close()
        return False
    for i in range(len(content)):
        if content[i]["Email"]==Email and content[i]["Password"]==Password:
            d=1
            break
    if d==0:
        f.close()
        return False
    f.close()
    return True

def Create_Event(org,events_json_file,Event_ID,Event_Name,Start_Date,Start_Time,End_Date,End_Time,Users_Registered,Capacity,Availability):
    '''Create an Event with the details entered by organizer'''
    file=open(events_json_file,'r+')
    data={
            "ID":Event_ID,
            "Name":Event_Name,
            "Organizer":org,
            "Start Date":Start_Date,
            "Start Time":Start_Time,
            "End Date":End_Date,
            "End Time":End_Time,
            "Users Registered":Users_Registered,
            "Capacity":Capacity,
            "Seats Available":Availability,

        }
    try:
         content=json.load(file)
         if data not in content:
            content.append(data)
            file.seek(0)
            file.truncate()
            json.dump(content,file)


    except JSONDecodeError:
        l=[]
        l.append(data)
        json.dump(l,file)
    file.close()

def View_Events(org,events_json_file):
    '''Return a list of all events created by the logged in organizer'''
    file=open(events_json_file,'r+')
    content=json.load(file)
    list_of_all_events=[]
    for i in range(len(content)):
        if content[i]["Organizer"]==org:
            list_of_all_events.append(content[i])  
        else:
            pass
    file.close()
    return list_of_all_events

def View_Event_ByID(events_json_file,Event_ID):
    '''Return details of the event for the event ID entered by user'''
    file=open(events_json_file,'r+')
    content=json.load(file)
    list=[]
    for i in range(len(content)):
        if content[i]["ID"]==Event_ID:
            list.append(content[i])    
    file.close()
    return list
    

def Update_Event(org,events_json_file,event_id,detail_to_be_updated,updated_detail):
    '''Update Event by ID || Take the key name to be updated from member, then update the value entered by user for that key for the selected event
    || Return True if successful else False'''
    file=open(events_json_file,'r+')
    content=json.load(file)
    for i in range(len(content)):
        if content[i]["ID"]==event_id:
            if detail_to_be_updated=='Name':
                content[i]['Name']=updated_detail
            elif detail_to_be_updated=='Start Date':
                content[i]['Start Date']=updated_detail
            elif detail_to_be_updated=='Start Time':
                content[i]['Start Time']=updated_detail
            elif detail_to_be_updated=='End Date':
                content[i]['End Date']=updated_detail
            elif detail_to_be_updated=='End Time':
                content[i]['End Time']=updated_detail
            else:
                return False  
            file.seek(0)
            file.truncate()
            json.dump(content,file)
            file.close() 
    return True
def Delete_Event(org,events_json_file,event_ID):
    '''Delete the Event with the entered Event ID || Return True if successful else False'''
    file=open(events_json_file,'r+')
    content=json.load(file)
    for i in range(len(content)):
        if content[i]["ID"]==event_ID:
            del content[i]
            file.seek(0)
            file.truncate()
            json.dump(content, file)
            file.close()
            return True
        else:
            pass


def Register_for_Event(events_json_file,event_id,Full_Name):
    '''Register the logged in member in the event with the event ID entered by member. 
    (append Full Name inside the "Users Registered" list of the selected event)) 
    Return True if successful else return False'''
    date_today=str(date.today())
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    '''Write your code below this line'''
    file=open(events_json_file,'r+')
    content=json.load(file)
    for i in range(len(content)):
        if content[i]["ID"]==event_id:
            content[i]['Users Registered'].append(Full_Name)
            content[i]['Seats Available']-=1
            file.seek(0)
            file.truncate()
            json.dump(content, file)
            file.close()
            return True
        else:
            pass
       

def fetch_all_events(events_json_file,Full_Name,event_details,upcoming_ongoing):
    '''View Registered Events | Fetch a list of all events of the logged in memeber'''
    '''Append the details of all upcoming and ongoing events list based on the today's date/time and event's date/time'''
    date_today=str(date.today())
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    '''Write your code below this line'''
    file=open(events_json_file,'r+')
    content=json.load(file)
    list=[]
    for i in range(len(content)):
        if Full_Name in content[i]['Users Registered']:
            Start_Date=content[i]["Start Date"]
            Start_Time=content[i]["Start Time"]
            y,m,d = [int(j) for j in Start_Date.split('-')]
            start_date=date(y,m,d)
            y,m,d = [int(j) for j in date_today.split('-')]
            current_date = date(y,m,d)
            if start_date>=current_date:
                upcoming_ongoing.append(content[i])        
    file.close()
    return upcoming_ongoing
    

def Update_Password(members_json_file,Full_Name,new_password):
    '''Update the password of the member by taking a new passowrd || Return True if successful else return False'''
    file=open(members_json_file,'r+')
    content=json.load(file)
    for i in range(len(content)):
        if content[i]["Full Name"]==Full_Name:
            content[i]["Password"]=new_password
            file.seek(0)
            file.truncate()
            json.dump(content, file)
            file.close()
    return True

def View_all_events(events_json_file):
    '''Read all the events created | DO NOT change this function'''
    '''Already Implemented Helper Function'''
    event_details=[]
    f=open(events_json_file,'r')
    try:
        content=json.load(f)
        f.close()
    except JSONDecodeError:
        f.close()
        return event_details
    for i in range(len(content)):
        event_details.append(content[i])
    return event_details
