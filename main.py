from json import load

from Scripts.Create_tables import Create_Tables
from Scripts.Room_merges import Room_merge

with open("./data/all_rooms.json", "r") as f:
    all_rooms_list = load(f)

with open("./data/next_duty_list.json", "r") as f:
    next_duty_rooms = load(f)
        

all_rooms_list_merged = Room_merge().merge()
Create_Tables(all_rooms_list_merged,next_duty_rooms)
