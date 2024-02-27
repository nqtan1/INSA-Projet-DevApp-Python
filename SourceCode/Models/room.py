import os 

'''
Classroom contains information of the room
'''

# We define the room type for each floor as follows:
# Room  x01 -> x05 : SINGLE
# Room  x06 -> x09 : DOUBLE 
# Room  x10 : FAMILY
def defi_room_type (id):
    if id >= 1 and id <= 5 : 
        type_room = 'SINGLE'
    elif id >= 6 and id <= 9:
        type_room = 'DOUBLE'
    else:
        type_room = 'FAMILY'
    return type_room;  

# Define No room
def defi_no_room (id_floor,id_room):
        return int(id_floor)*100 + int(id_room)
    
class Room: 
    def __init__(self,id=int(),id_floor=int(),check_in_date='',check_out_date=''):
        self.id = id 
        self.id_floor = id_floor
        self.no_room = defi_no_room(self.id_floor,self.id)
        self.room_type = defi_room_type(int(self.id))
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
    
    def __info__(self):
        return f'Id: {self.id}, Floor: {self.id_floor}, Room: {self.no_room}, Type: {self.room_type}, Check In Date: {self.check_in_date}, Check Out Date: {self.check_out_date}'
    
    def string_for_csv(self):
        return str(self.id)+';'+str(self.id_floor)+';'+str(self.no_room)+';'+self.room_type + ';' + self.check_in_date + ';' + self.check_out_date
    
    
    def write_to_csv (self,filename,methode='a'):
        # Open the CSV file in append mode
        file = open(filename,methode)
        # Check if the file is empty
        # Write headers if the file is empty
        if os.path.getsize(filename) == 0:
            file.write('$ID,ID Floor, No Room, Room Type,Check In Date, Check Out Date\n')

        file.write(self.string_for_csv()+'\n')
        file.close()
        return True