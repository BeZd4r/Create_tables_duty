from openpyxl import load_workbook, Workbook
from json import load
from datetime import datetime
from calendar import monthrange
from openpyxl.styles import Color, PatternFill, Font, Border
from openpyxl.styles import colors

with open("All_rooms/all_rooms.json", "r") as f:
    all_rooms = load(f)

with open("All_rooms/last_duty_list.json", "r") as f:
    last_duty_rooms = load(f)

current_time = datetime.now()
current_year = current_time.year
current_month = current_time.month
days = monthrange(current_year, current_month)
days = days[-1] + 1

Fill_cell_style = PatternFill(patternType='solid',
                       fgColor='808080')

deficient_rooms_list = dict()

def Create_tables(deficient_rooms_list):
    for floors in all_rooms.keys():

        deficient_rooms_list[floors] = {}

        for wing in all_rooms[floors].keys():

            wb = Workbook()
            sheet = wb.active

            i = 1

            for room in all_rooms[floors][wing]:

                isWrite = True
                i += 1
                peoples = all_rooms[floors][wing][room]
                if peoples < 3:
                        deficient_rooms_list[floors][room] = {"Peoples": peoples, "Column": i}
                        deficient_rooms_list[floors] = sorted(deficient_rooms_list[floors].items(), key=lambda item:item[1])
                        deficient_rooms_list[floors] = dict(deficient_rooms_list[floors])
                        print(deficient_rooms_list)
                        if deficient_rooms_list[floors] != {}:
                            stop_flag = False
                            for deficient_rooms in deficient_rooms_list[floors]:
                                print(list(deficient_rooms_list[floors][deficient_rooms].values()))
                                for count in deficient_rooms:
                                    print(count)
                                    if int(count) + peoples < 3:
                                        pass
                                    elif int(count) + peoples == 3:
                                        pass
                                    else:
                                        continue
                        else:
                            cell = sheet.cell(row=1, column=i) 
                            cell.value = room  
                            isWrite = False
                if isWrite:              
                    cell = sheet.cell(row=1, column=i) 
                    cell.value = room

            for day in range(1,days):
                cell = sheet.cell(row=day+1, column=1) 
                cell.value = f'{day}.{current_month}'
            wb.save(filename=f'{floors}/{wing}.xlsx')
            
def Paint_cells():
    for floors in all_rooms.keys():
        
        for wing in all_rooms[floors].keys():
            path = f'{floors}/{wing}.xlsx'
            wb = load_workbook(path)
            sheet = wb.active
            row = sheet.max_row
            column = sheet.max_column

            last_duty = last_duty_rooms["last_duty_list"][floors][wing]
            rooms = all_rooms[floors][wing]

            for dates in range(2,row+1):
                for room in range(2,column+1):
                    room_cell = sheet.cell(row=1, column=room)
                    room_value = room_cell.value

                    duty_room = sheet.cell(row=dates, column=room)
                    if room_value == last_duty_rooms["last_duty_list"][floors][wing]:
                        duty_room = sheet.cell(row=dates, column=room)
                        duty_room.fill = Fill_cell_style
                        
            wb.save(filename=f'{floors}/{wing}.xlsx')                
       
Create_tables(deficient_rooms_list)
Paint_cells()

print(deficient_rooms_list)