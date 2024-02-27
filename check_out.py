import re
import tkinter as tk
from tkinter import messagebox
from SourceCode.Models.client import list_client
from SourceCode.Models.floor import Floor

def is_valid_date(date_string):
    # Define a regular expression pattern for a valid date (dd/mm/yyyy)
    date_pattern = re.compile(r'^\d{1,2}/\d{1,2}/\d{4}$')
    # Use the pattern to match the date
    match = date_pattern.match(date_string)
    return bool(match)

class check_out_window: 
    # Create a window 
    def __init__(self,master):
        self.master = master
        self.master.title('Check Out')
        self.master.config(bg='white',width=400,height=500)
        self.master.attributes('-topmost',True)
        
        # To create widgets
        self.widgets()
        
    def widgets(self):
        pad_x = 10 # Space between cells horizontally
        pad_y = 10 # Vertical spacing between cells
        
        # Main frame
        frame = tk.Frame(master=self.master, padx=50,pady=10)
        frame.config(bg="white", width=400, height=500)
        frame.pack_propagate(False)
        frame.pack(expand=True)
        frame.grid(columnspan=3)
        
        # OK button function (used to check out)
        def get_check_out():
            no_room = int(entry_no_room.get())
            client_name = entry_client.get()
            check_in_date = entry_check_in_date.get()
            print(f'Id Room: {no_room}, Client Name: {client_name}, Check-In Date: {check_in_date}')
            
            clients_data = list_client()
            clients_data.read_from_csv('Data/client.csv')
            
            rooms_data = Floor()
            rooms_data.read_from_csv('Data/room.csv')
            
            # We can add more conditions in there to verify before delete.
            clients_data.remove_from_csv('Data/client.csv',client_name,check_in_date)
            rooms_data.remove_from_csv("Data/room.csv",no_room=no_room,checkin_date=check_in_date)
            messagebox.showinfo("Finish", "Thank you for choosing our service! See you again!")
            # Close the check-out window
            self.master.destroy()

        
        # Label : Room number 
        label_room_no = tk.Label(master=frame,text="Room number: ",bg='white')
        label_room_no.grid(row=1,column=0,padx=pad_x,pady=pad_y)
        
        # Entry : Enter room number 
        entry_no_room = tk.Entry(master=frame, width=40)
        entry_no_room.grid(row=1,column=1,padx=pad_x,pady=pad_y)
        
        # Label : Client info
        label_client = tk.Label(master=frame,text="Full name: ",bg='white')
        label_client.grid(row=2,column=0,padx=pad_x,pady=pad_y)
        
        # Entry : Enter client info
        entry_client = tk.Entry(master=frame, width=40)
        entry_client.grid(row=2, column=1,padx=pad_x,pady=pad_y)
        
        # Label : Date Come
        label_check_in_date = tk.Label(master=frame, text=" Check-in Date (dd/mm/202y)", bg="white")
        label_check_in_date.grid(row=3, column=0, sticky="w",padx=pad_x,pady=pad_y)

        # Entry : Check-In Date
        entry_check_in_date = tk.Entry(master=frame, width=40)
        entry_check_in_date.grid(row=3, column=1, sticky="w",padx=pad_x,pady=pad_y)
        
        # Button check out 
        but_check_out = tk.Button(master=frame, text="OK",width=8,command=get_check_out)
        but_check_out.grid(row=4,column=1,pady=pad_y)
        
        # Button cancel
        but_quit = tk.Button(master=frame, text="Cancel",width=8,command=self.master.destroy)
        but_quit.grid(row=4, column=1,sticky='e',pady=pad_y)
        
        
def open_check_out_window():
    root = tk.Tk()
    checkout = check_out_window(root)
    root.mainloop()