import json
import timeit
def present_in_morning_gongyo(date):
    with open('total_participant.json') as fp:
        content = json.load(fp)
        print('if present write "p" for absent do nothing')
        present_count = 0
        total_participant = 0
        morning_gongyo = []
        for i in content:
            print(i)
            total_participant +=1
            give_input = input().lower().strip()
            if give_input == 'p':
                present_count +=1
                morning_gongyo.append(i)
    print('Total participants are', total_participant, 'and total partcipant who attended morning gongyo are', present_count)
    with open('attendance_sheet.json') as fp1:
        fp1.seek(0)
        content1 = json.load(fp1)
        content1.setdefault(date,[('present in morning gongyo',morning_gongyo),('total participant',total_participant)])
    with open('attendance_sheet.json','w') as fp2:
        json.dump(content1,fp2,indent=4)

def present_in_study_meeting(date):
    with open('total_participant.json') as fp:
        content = json.load(fp)
        print('if present write "p" for absent do nothing')
        present_count = 0
        total_participant = 0
        study_meeting = []
        for i in content:
            print(i)
            total_participant +=1
            give_input = input().lower().strip()
            if give_input == 'p':
                present_count +=1
                study_meeting.append(i)
    print('Total participants are', total_participant, 'and total partcipant who attended study meeting', present_count)
    with open('attendance_sheet.json') as fp1:
        fp1.seek(0)
        content1 = json.load(fp1)
        content1[date].insert(1,('present in study meeting',study_meeting))
    with open('attendance_sheet.json','w') as fp2:
        json.dump(content1,fp2,indent=4)
        