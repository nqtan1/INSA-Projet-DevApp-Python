import os

'''
The demand class contains room orders 
and dates condition functions
'''

# Assume that 1 month =  30 days and 1 year = 365 days
def date_to_int (date_string=''):
    tab  = date_string.split('/')
    return int(tab [0]) + int(tab[1]*30) + (int(tab[2]) - 2020)*365 

# Returns True if day_tring1 is greater than day_string2
def compare_dates (date_string1='',date_string2 = ''):
    date1 = date_to_int(date_string1)
    date2 = date_to_int(date_string2)
    delta = date1 - date2
    if delta > 0: 
        return True
    elif delta <= 0:
        return False

class demand:
    def __init__(self,no_room= int(),check_in_date='',check_out_date='' ):
        self.no_room = no_room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        
    def string_for_csv (self):
        return str(self.no_room) + ',' +self.check_in_date + ',' + self.check_out_date
    
    def write_to_csv (self,filename):
        # Open the CSV file
        file = open(filename,'a')
        # Check if the file is empty
        is_empty = os.path.getsize(filename) == 0
        # Write headers if the file is empty
        if is_empty:
            file.write('$No Room, Check In Date, Check Out Date\n')

        file.write(self.string_for_csv()+'\n')
        file.close()
        return True 
    
class list_demand:
    def __init__(self):
        self.demand = []
    
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
                if len(fields)!= 3: # Demande (No Room, Check In Date, Check Out Date)
                    print('Warning at line: ',line_number, 'Found: ',len(fields),end='')
                if len(fields) < 3 : 
                    print('Missing fields. Ignored it !')
                    check_condition = False 
                else:
                    print('Extra fields are ignored')
            
                if check_condition:
                    self.demand.append(demand(no_room=fields[0],check_in_date=fields[1], check_out_date=fields[2]))
                
            line = file.readline() # Move to the next line
            line_number += 1 # Update new value 
        file.close()
        return True 
    
    def remove_from_csv(self,filename,no_room=int(),checkin_date=''):
        # Find room information in the list
        for demande in self.demand:
            if demand.check_in_date == checkin_date and int(demand.no_room) == no_room:
                self.room.remove(demand)
                print('Demand of room ' + str(demand.no_room) +  ' is deleted!')
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
    
    # Check for existence in demand list
    def is_room_exist (self,no_room=int()):
        for demand in self.demand:
            if demand.no_room == no_room:
                return True
        return False
    
    # Check if the booking date is the same or not
    def is_valide (self,no_room= int(),check_in_date='', check_out_date=''):
        check_condition = []
        index = 0
        if len(self.demand) == 0 and self.is_room_exist(no_room) == False: # There are no reservations 
            return True
        else:
            for demand in self.demand: # Check conditions with previous demands
                if demand.no_room == no_room:
                    # Conditions not satisfied for booking
                    # because the room has been booked before
                    # [check_in_date,check_out_day] have to in [check_in_date_before,check_out_day_before]
                    # or completely outside that range
                    if (compare_dates(demand.check_in_date,check_in_date) and compare_dates(check_out_date,demand.check_in_date)) and (compare_dates(demand.check_out_date,check_in_date) and compare_dates(check_out_date,demand.check_out_date)):
                        check_condition[index] = False
                    else:
                        check_condition[index] = True
                    index = index + 1 
        # Check the value in the list
        # If a False value exists, it means 
        # the date condition is not satisfied            
        for check in check_condition:
            if check == False:
                return False
        return True