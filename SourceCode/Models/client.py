import os

class Client: 
    def __init__(self,full_name='', phone_number='', email='',no_room = int, check_in_date='', check_out_date=''):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.no_room = no_room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
    
    def __info__(self):
        return f"Name: {self.full_name}, Email: {self.email},Phone Number: {self.phone_number},No Room: {self.no_room}, Check In Date: {self.check_in_date}, Check Out Date: {self.check_out_date}"
    
    def string_for_csv (self):
        return self.full_name+';'+self.phone_number+';'+self.email+';' + str(self.no_room) +';' +str(self.check_in_date)+';'+str(self.check_out_date)
    
    def write_to_csv (self,filename):
        # Open the CSV file in append mode
        file = open(filename,'a')
        # Check if the file is empty
        is_empty = os.path.getsize(filename) == 0
        # Write headers if the file is empty
        if is_empty:
            file.write('$Full Name,Phone Number,Email,No Room,Check In Date,Check Out Day\n')

        file.write(self.string_for_csv()+'\n')
        file.close()
        
class list_client:
    def __init__(self):
        self.client = []
        
    def __info__(self):
        for i in self.client:
            print(i.__info__())
            
    def read_from_csv(self,filename):
        file = open(filename,'r') # Open file .csv
        line = file.readline() # Read each line in the file 
        line_number = 1 # Init index

        while line != '':
            line = line.strip() # Remove spaces
            if line != '' and line[0] != '$':
                # This is not a comment or empty line, so read the fields
                fields = line.split(';') # Divide string into different fields
                check_condition = True # Check whether customer information is complete or not
                if len(fields)!= 5 : # Client (Full Name,Phone Number,Email,No Room,Check In Date,Check Out Day)
                    print('Warning at line: ',line_number, 'Found: ',len(fields),end='')
                if len(fields) < 5: 
                    print('Missing fields. Ignored it !')
                    check_condition = False 
                else:
                    pass
            
                if check_condition:
                    self.client.append(Client(full_name=fields[0],phone_number=fields[1],email=fields[2],no_room=fields[3],check_in_date=fields[4],check_out_date=fields[5]))
                
            line = file.readline() # Move to the next line
            line_number += 1 # Update new value 
        file.close()
        return True
    
    def write_to_csv (self,filename):
        for client in self.client:
            client.write_to_csv(filename)   
        return True
    
    def remove_from_csv(self,filename,full_name='',checkin_date=''):
        for client in self.client:
            if client.full_name == full_name and str(client.check_in_date) == checkin_date:
                self.client.remove(client)
                print("Deleted!")
            else :
                print("Can't find this client!")
                
        if(os.path.exists(filename) and os.path.isfile(filename)): 
            os.remove(filename) 
            print("File deleted") 
        else: 
            print("File not found")     
            
        # Update room information
        for i in self.client:
            print(i.__info__())
            i.write_to_csv(filename)
        return True
    
    def is_exist (self,full_name,checkin_date):
        for client in self.client:
            if client.full_name == full_name and str(client.check_in_date) == checkin_date:
                return True
        return False     