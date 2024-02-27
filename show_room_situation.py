import tkinter as tk
from SourceCode.Models.floor import Floor

class room_situation_window: 
    # Create a window 
    def __init__(self,master):
        self.master = master
        self.master.title('Room Information')
        self.master.config(bg='white',width=400,height=500)
        self.master.attributes('-topmost',True)
        
        # To create widgets
        self.widgets()
        
    def widgets(self):
        pad_x = 10 
        pad_y = 10
        
        # Main frame
        frame = tk.Frame(master=self.master, padx=50,pady=10)
        frame.config(bg="white", width=400, height=500)
        frame.pack_propagate(False)
        frame.pack(expand=True)         
        
        # Title of room        
        label_ID = tk.Label(frame, text='ID Room', font=("Arial", 12),background='white')
        label_ID.grid(column=0,row=0,padx=20, pady=20)
        
        label_ID_Floor = tk.Label(frame, text='ID Floor', font=("Arial", 12),background='white')
        label_ID_Floor.grid(column=2,row=0,padx=20, pady=20)
        
        label_No_Room = tk.Label(frame, text='No Room', font=("Arial", 12),background='white')
        label_No_Room.grid(column=3,row=0,padx=20, pady=20)
        
        label_Checkin = tk.Label(frame, text='Check In Date', font=("Arial", 12),background='white')
        label_Checkin.grid(column=4,row=0,padx=20, pady=20)
        
        label_Checkout = tk.Label(frame, text='Check Out Date', font=("Arial", 12),background='white')
        label_Checkout.grid(column=5,row=0,padx=20, pady=20)
        
        # Read room data from .csv file
        info = Floor()
        info.read_from_csv("Data/room.csv")

        # Show room informations
        no_row = 1 # Indice of row 
        for room in info.room:
            label_ID = tk.Label(frame, text= str(room.id), font=("Arial", 12),background='white')
            label_ID.grid(column=0,row=no_row,padx=20, pady=20)
            
            label_ID_Floor = tk.Label(frame, text=str(room.id_floor), font=("Arial", 12),background='white')
            label_ID_Floor.grid(column=2,row=no_row,padx=20, pady=20)
            
            label_No_Room = tk.Label(frame, text=str(room.no_room), font=("Arial", 12),background='white')
            label_No_Room.grid(column=3,row=no_row,padx=20, pady=20)
            
            label_Checkin = tk.Label(frame, text=room.check_in_date, font=("Arial", 12),background='white')
            label_Checkin.grid(column=4,row=no_row,padx=20, pady=20)
            
            label_Checkout = tk.Label(frame, text=room.check_out_date, font=("Arial", 12),background='white')
            label_Checkout.grid(column=5,row=no_row,padx=20, pady=20)
            
            no_row = no_row + 1
        
        
def open_show_room_situation():
    root = tk.Tk()
    show_situation = room_situation_window(root)
    root.mainloop()