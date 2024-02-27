import re 
import tkinter as tk
from tkinter import ttk,messagebox
from SourceCode.Models import client,room,demand


def is_valid_phone_number(phone_number):
    # Define a regular expression pattern for a valid phone number
    pattern = re.compile(r'^\d{10}$')  # Assuming a 10-digit phone number
    # Use the pattern to match the phone number
    match = pattern.match(phone_number)
    return bool(match)

def is_valid_date(date_string):
    # Define a regular expression pattern for a valid date (dd/mm/yyyy)
    date_pattern = re.compile(r'^\d{1,2}/\d{1,2}/\d{4}$')
    # Use the pattern to match the date
    match = date_pattern.match(date_string)
    return bool(match)

def is_validate_email(email):  
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

class check_in_window:
    # Create a window 
    def __init__(self,master):
        self.master = master
        self.master.title('Check In')
        self.master.config(bg='white',width=400,height=500)
        self.master.attributes('-topmost',True)
        self.widgets()
        
    def widgets(self):
        # OK button function (used to check in)
        def get_check_in():
            id_floor = int(combo_floor.get())
            id_room = int(combo_room.get())
            nb_per = int(entry_person.get())
            date_come = entry_date_come.get()
            date_depart = entry_date_depart.get()
            email = entry_email.get()
            phone = entry_phone.get()
            name = entry_rep.get()
 
            # Print the collected information 
            print(f"Rep: {name}, Email: {email}, Phone: {phone}, Floor: {id_floor}, Room: {id_room}, Persons: {nb_per}, Date Come: {date_come}, Date Depart: {date_depart}")
            
            # Check whether the format of the input information is correct or not
            if is_valid_date(date_come) == True and is_valid_date(date_depart) == True and is_valid_phone_number(phone) == True and is_validate_email(email)== True :   
                new_demand = demand.demand(no_room=id_floor*100+id_room,check_in_date=date_come,check_out_date=date_depart)
                list_demand = demand.list_demand()
                list_demand.read_from_csv("Data/demand.csv")
                
                # Check whether the date condition is satisfied or not
                if list_demand.is_valide(id_floor*100+id_room,date_come,date_depart): 
                    # Work with file .csv 
                    # Write new demand into the .csv file
                    new_demand.write_to_csv("Data/demand.csv")
                    
                    # Write new client information into the .csv file
                    new_client = client.Client(full_name=name,phone_number=phone,email=email,no_room=id_floor*100+id_room,check_in_date=date_come,check_out_date=date_depart)
                    new_client.write_to_csv('Data/client.csv')
                    
                    # Write new room in booked status into the .csv file
                    new_room = room.Room(id_room,id_floor,date_come,date_depart)
                    new_room.write_to_csv('Data/room.csv')
                    messagebox.showinfo("Finish", "Your room has been successfully booked. Thank you for choosing our service!")
                    # Close the check-in window
                    self.master.destroy()
                else:
                    messagebox.showinfo("Oops! Some errors", "Your room has been reserved. Please choose another date! \n You can refer to the information in 'Show room situation'.")
            else: 
                messagebox.showinfo("Oops! Some errors", "Please re-enter your information in the correct format!")
            
        pad_x = 10 # Space between cells horizontally
        pad_y = 10 # Vertical spacing between cells
        
        # Main frame 
        frame = tk.Frame(master=self.master, padx=50,pady=10)
        frame.config(bg="white", width=400, height=500)
        frame.pack_propagate(False)
        frame.pack(expand=True)
        frame.grid(columnspan=3)
        
        ''' ROOM INFORMATION '''
        label_room_info = tk.Label(master=frame, text=" ROOM INFORMATION ",
                            font=('Times', '15'), bg="white")
        label_room_info.grid(row=0,column=1,padx=pad_x,pady=pad_y)
        
        # Floor
        # Label 
        label_floor = tk.Label(master=frame, text=" Floor ",
                            font=('Times', '15'), bg="white")
        label_floor.grid(row=1, column=0, sticky="w",padx=pad_x,pady=pad_y)

        # List 
        list_floor = [1, 2, 3, 4, 5] # Assume that this hotel has 5 floors
        combo_floor = ttk.Combobox(frame, values=list_floor,
                                state="readonly", width=50, background="red")
        combo_floor.grid(row=1, column=1, sticky="w",padx=pad_x,pady=pad_y)
        
        # Room
        # Label
        label_room = tk.Label(master=frame, text=" Room ",
                            font=('Times', '15'), bg="white")
        label_room.grid(row=2, column=0, sticky="w",padx=pad_x,pady=pad_y)
        
        # List
        list_room = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Assume that each floor of the hotel has 10 rooms
        combo_room = ttk.Combobox(frame, values=list_room,
                                state="readonly", width=50)
        combo_room.grid(row=2, column=1, sticky="w",padx=pad_x,pady=pad_y)

        # Nb Person
        label_person = tk.Label(master=frame, text=" Number of people ",
                            font=('Times', '15'), bg="white")
        label_person.grid(row=3, column=0, sticky='w',padx=pad_x,pady=pad_y)

        entry_person = tk.Entry(master=frame, width=50)
        entry_person.grid(row=3, column=1, sticky='w',padx=pad_x,pady=pad_y)

        ''' REPRESENTATIVE INFORMATION '''  
        label_rep_info = tk.Label(master=frame, text=" REPRESENTATIVE INFORMATION ",
                            font=('Times', '15'), bg="white")
        label_rep_info.grid(row=4,column=1,padx=pad_x,pady=pad_y)    
          
        # Representative
        label_rep = tk.Label(master=frame, text=" Full Name ",
                            font=('Times', '15'), bg="white")
        label_rep.grid(row=5, column=0, sticky='w',padx=pad_x,pady=pad_y)
        
        entry_rep = tk.Entry(master=frame, width=50)
        entry_rep.grid(row=5, column=1, sticky='w',padx=pad_x,pady=pad_y)
        
        # Phone 
        label_phone = tk.Label(master=frame, text=" Phone number ",
                            font=('Times', '15'), bg="white")
        label_phone.grid(row=6,column=0, sticky="w",padx=pad_x,pady=pad_y)
        
        entry_phone = tk.Entry(master=frame, width=50)
        entry_phone.grid(row=6, column=1, sticky='w',padx=pad_x,pady=pad_y)
        
        # Email
        label_email =  tk.Label(master=frame, text=" Email ",
                            font=('Times', '15'), bg="white")
        label_email.grid(row=7,column=0,sticky='w',padx=pad_x,pady=pad_y)
        
        entry_email = tk.Entry(master=frame, width=50)
        entry_email.grid(row=7,column=1,sticky='w',padx=pad_x,pady=pad_y)
        
        # Date Come and Depart 
        label_date_come = tk.Label(master=frame, text=" From (dd/mm/202y)",
                                font=('Times', '15'), bg="white")
        label_date_come.grid(row=8, column=0, sticky="w",padx=pad_x,pady=pad_y)

        entry_date_come = tk.Entry(master=frame, width=50)
        entry_date_come.grid(row=8, column=1, sticky="w",padx=pad_x,pady=pad_y)

        label_date_depart = tk.Label(master=frame, text=" To (dd/mm/202y)",
                                font=('Times', '15'), bg="white")
        label_date_depart.grid(row=9, column=0, sticky='w',padx=pad_x,pady=pad_y)

        entry_date_depart = tk.Entry(master=frame, width=50)
        entry_date_depart.grid(row=9, column=1, sticky='w',padx=pad_x,pady=pad_y)
        
        ''' BUTTON '''
        # Button to perform check-in
        but_check_in = tk.Button(frame, text="OK",width=8,command=get_check_in)
        but_check_in.grid(row=10, column=2)

        # Button cancel
        but_cancel = tk.Button(master=frame,text="Cancel",command=self.master.destroy,width=8)
        but_cancel.grid(row=10,column=3)
        
        
def open_check_in_window():
    root = tk.Tk()
    checkin = check_in_window(root)
    root.mainloop()