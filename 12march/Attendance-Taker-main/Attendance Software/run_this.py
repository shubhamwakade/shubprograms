import json
import add_participant
import total
import timeit
print('**********          HELLO PARTHO UNCLE !!!          **********')
while True:
    print('choose 1 for adding all new participants  ')
    print('choose 2 for give attendance for morning gongyo  ')
    print('choose 3 for give attendance for study meeting')
    print('choose 4 for BYE BYE......  ')
    choose = input().strip()
    if choose == '1':
        add_participant.add_participant()
    if choose == '2':
        print('give date -> date should be of the type "14/03/2001"')
        DATE1 = input('enter the date  ->    ')
        total.present_in_morning_gongyo(DATE1)
    if choose == '3':
        print('give date -> date should be of the type "14/03/2001"')
        DATE2 = input('enter the date  ->    ')
        total.present_in_study_meeting(DATE2)
    if choose == '4':
        print('ok bye')
        break
    else:
        print('choose something valid')