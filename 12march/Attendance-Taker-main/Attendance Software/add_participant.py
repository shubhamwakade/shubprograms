import json
def add_participant():
    with open('total_participant.json','w') as fp:
        print('enter participant name with comma')
        total_participants = input().split(',')
        json.dump(total_participants, fp, indent=4)