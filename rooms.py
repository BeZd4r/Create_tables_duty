import json

all_rooms = {}
for i in range(1,6):
    all_rooms[f'Floor_{i}'] = {"Left_wing":{}, "Right_wing":{}}

for i in range(1,10):
    j = 0
    for key in all_rooms:
        j+=1
        if key == "Floor_1" and (i < 2 or i > 6):
            continue
        else:
            all_rooms[key]["Left_wing"][f'{j}0{i}' if i <10 else f'{j}{i}'] = 3
for i in range(21,26):
    j = 0
    for key in all_rooms:
        j+=1
        if key == "Floor_1" and i < 24:
            continue
        else:
            all_rooms[key]["Left_wing"][f'{j}0{i}' if i <10 else f'{j}{i}'] = 3
for i in range(10,18):
    j = 0
    for key in all_rooms:
        j+=1
        if key == "Floor_1" and i < 12:
            continue
        else:
            all_rooms[key]["Right_wing"][f'{j}0{i}' if i <10 else f'{j}{i}'] = 3
for i in range(18,21):
    j = 0
    for key in all_rooms:
        j+=1
        if key == "Floor_1" and i > 19:
            continue
        else:
            all_rooms[key]["Right_wing"][f'{j}0{i}' if i <10 else f'{j}{i}'] = 3

with open("All_rooms/all_rooms.json", "w") as f:
    json.dump(all_rooms,f, indent=4)