from SourceCode.Models.floor import Floor
import os 

'''
Class Hotel contains information about the hotel 
and data about the floors in that hotel.
'''

class Hotel:
    def __init__(self,name='',address='',email='',phone='',num_floors=int()):
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
        self.num_floors = num_floors
        self.floor = []
    
    def __info__(self):
        return f'Hotel: {self.name}, Address: {self.address}, Email: {self.email}, Phone: {self.phone}, {self.num_floors}'
    
    def string_for_csv (self):
        return self.name+';'+self.address+';'+self.email+';'+self.phone+';'+str(self.num_floors)
    
    def write_to_csv (self,filename):
        # Open the CSV file in append mode
        file = open(filename,'a')
        # Check if the file is empty
        is_empty = os.path.getsize(filename) == 0
            # Write headers if the file is empty
        if is_empty:
            file.write('$Name,Address,Email,Phone Number,Number Floors\n')

        file.write(self.string_for_csv()+'\n')
        file.close()

    def read_from_csv (self,filename):
        file = open(filename,'r+') # Read file .csv
        line = file.readline() # Read each line in the file 
        line_number = 1 # Init index

        while line != '':
            line = line.strip() # Remove spaces
            if line != '' and line[0] != '$':
                # This is not a comment or empty line, so read the fields
                fields = line.split(';') # Divide string into different fields
                check_condition = True # Check whether customer information is complete or not
                if len(fields)!=2: # Floor (id,Number Room)
                    print('Warning at line: ',line_number, 'Found: ',len(fields),end='')
                if len(fields) < 2 : 
                    print('Missing fields. Ignored it !')
                    check_condition = False 
                else:
                    print('Extra fields are ignored')
            
                if check_condition:
                    self.floor.append(Floor(id=fields[0],number_room=fields[1]))
                
            line = file.readline() # Move to the next line
            line_number += 1 # Update new value 
        file.close()
        return True
    
    def remove_from_csv(self,filename,id_floor=int()):
        # Find information of floor in the list 
        for floor in self.floor:
            if int(floor.id) == id_floor:
                self.floor.remove(floor)
                print('Deleted!')
            else:
                print("Can't find this floor!")
        # Remove csv file 
        if(os.path.exists(filename) and os.path.isfile(filename)): 
            os.remove(filename) 
            print("file deleted") 
        else: 
            print("file not found")      
        # Update room information
        for i in self.floor:
            print(i.__info__())
            i.write_to_csv(filename) 
        return True