from SourceCode.Models.room import Room
import os 

'''
Class Floor contains hotel floor information 
and contains information about the rooms contained 
in this floor
'''

class Floor: 
    def __init__(self,id=int(),number_room=10):
        self.id = id 
        self.number_room = number_room 
        self.room = []
        
    def __info__(self):
        return f'Floor: {self.id}, Number of rooms: {self.number_room}'
    
    def string_for_csv(self):
        return str(self.id)+';'+str(self.number_room)
    
    def write_to_csv (self,filename):
        # Open the CSV file
        file = open(filename,'a')
        # Check if the file is empty
        is_empty = os.path.getsize(filename) == 0
        # Write headers if the file is empty
        if is_empty:
            file.write('$ID, Number Rooms\n')

        file.write(self.string_for_csv()+'\n')
        file.close()
        return True

    def read_from_csv (self,filename):
        file = open(filename,'r') # Open file .csv
        line = file.readline() # Read each line in the file 
        line_number = 1 # Init index

        while line != '':
            line = line.strip() # Remove spaces
            if line != '' and line[0] != '$':
                # This is not a comment or empty line, so read the fields
                fields = line.split(';') # Divide string into different fields
                check_condition = True # Check whether customer information is complete or not
                if len(fields)!= 6: # Room (ID, ID Floor, No Room , Room Type, Check In Date, Check Out Date)
                    print('Warning at line: ',line_number, 'Found: ',len(fields),end='')
                if len(fields) < 6 : 
                    print('Missing fields. Ignored it !')
                    check_condition = False 
                else:
                    print('Extra fields are ignored')
            
                if check_condition:
                    self.room.append(Room(id=fields[0],id_floor=fields[1],check_in_date=fields[4],check_out_date=fields[5]))
                
            line = file.readline() # Move to the next line
            line_number += 1 # Update new value 
        file.close()
        return True
    
    def remove_from_csv(self,filename,no_room=int(),checkin_date=''):
        # Find room information in the list
        for room in self.room:
            if room.check_in_date == checkin_date and int(room.no_room) == no_room:
                self.room.remove(room)
                print('Room ' + str(room.no_room) +  ' is deleted!')
            else:
                print("Can't find this room!")
        # Remove csv file 
        if(os.path.exists(filename) and os.path.isfile(filename)): 
            os.remove(filename) 
            print("File deleted") 
        else: 
            print("File not found")  
        # Update room information
        for i in self.room:
            print(i.__info__())
            i.write_to_csv(filename)
        return True
    
    def is_room_exist (self,no_room = int()):
        # Find a room information in a floor
        for room in self.room:
            if int(room.no_room) == no_room:
                return True
        return False