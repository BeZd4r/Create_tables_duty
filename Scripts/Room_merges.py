from json import load

class Room_merge:

    def __init__(self):
        with open("./data/all_rooms.json", "r") as f:
            self.all_rooms_list = load(f)

            
    def merge(self):
        all_merged_rooms = {}
        for floors in self.all_rooms_list.keys():
        
            deficient_rooms_list = {}
            all_merged_rooms[floors] = {}

            for wing in self.all_rooms_list[floors].keys():

                room_list = []

                for current_room in self.all_rooms_list[floors][wing]:

                    peoples_count = self.all_rooms_list[floors][wing][current_room]

                    if peoples_count < 3:

                        if deficient_rooms_list != {}:

                            unused_deficent_rooms = {}

                            for deficient_rooms in deficient_rooms_list.copy().keys():

                                
                                if peoples_count + deficient_rooms_list[deficient_rooms]["Count_peoples"] < 3:

                                    deficient_rooms_list[deficient_rooms]["Count_peoples"] += peoples_count
                                    deficient_rooms_list[deficient_rooms]["Rooms"] += f', {current_room}'

                                elif peoples_count + deficient_rooms_list[deficient_rooms]["Count_peoples"] == 3:    
                                    deficient_rooms_list[deficient_rooms]["Count_peoples"] += peoples_count
                                    deficient_rooms_list[deficient_rooms]["Rooms"] += f', {current_room}'
                                    # room_list.append(deficient_rooms_list[deficient_rooms]["Rooms"])
                                    # del deficient_rooms_list[deficient_rooms]["Rooms"]

                                else:
                                    deficient_rooms_list[current_room] = {"Count_peoples" : peoples_count, "Rooms" : f'{current_room}'}
                                # print(deficient_rooms_list)
                        else:

                            deficient_rooms_list[current_room] = {"Count_peoples" : peoples_count, "Rooms" : f'{current_room}'}
                            # print(deficient_rooms_list)

                    else:
                
                        room_list.append(current_room)


                for deficient_rooms in deficient_rooms_list:

                    room_list.append(deficient_rooms_list[deficient_rooms]["Rooms"])
                
                all_merged_rooms[floors][wing] = room_list
        return all_merged_rooms