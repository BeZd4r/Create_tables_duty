from json import load
from datetime import datetime
from Scripts.Create_tables import Create_Tables
from Scripts.Room_merges import Room_merge
from Scripts.Add_cell_style import Add_cell_style

with open("./data/all_rooms.json", "r") as f:
    all_rooms_list = load(f)

with open("./data/next_duty_list.json", "r") as f:
    next_duty_rooms = load(f)
        
current_time = datetime.now()

all_rooms_list_merged = Room_merge().merge()
Create_Tables(all_rooms_list_merged,next_duty_rooms,current_time)
Add_cell_style(current_time)