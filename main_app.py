import tkinter as tk
import check_in 
import check_out 
import show_room_situation

class windowApp: 
    # Create a window 
    def __init__(self,master):
        self.master = master
        self.master.title('Hotel booking')
        self.master.attributes('-topmost',True)
        
        # To create widgets
        self.widgets()

    def widgets(self):
        # Main frame 
        x = 10
        pad_space = 10
        
        frame = tk.Frame(master=self.master, padx=50,pady=10)
        frame.config(bg="white", width=1080, height=720)
        frame.pack_propagate(False)
        frame.pack(expand=True)
        frame.grid(columnspan=4)
        
        # Logo 
        logo_path = '/home/nguyenquoctan/ProjetHotel/Assets/logoHotel.png' # Please change the folder path 
                                                                           #according to where the file is located 
                                                                           # on your computer
        logo_image = tk.PhotoImage(file=logo_path).subsample(2,2)
        label_logo = tk.Label(master=frame, image=logo_image)
        label_logo.photo = logo_image
        label_logo.grid(row=0, column=0,padx=pad_space,pady=pad_space)

        # Welcome
        labelWelcome = tk.Label(master=frame,text=" Welcome to our Hotel !",bg='white',font=('Narkisim',15))
        labelWelcome.grid(row=0,column=1,padx=pad_space,pady=pad_space,sticky='nsew') 

        # Button Check In 
        butCheckIn = tk.Button(master=frame,text="Check In",width=x,command=check_in.open_check_in_window) # Call check_in window
        butCheckIn.grid(row=1,column=1,padx=pad_space,pady=pad_space,sticky='nsew')

        # Button Check Out
        butCheckOut = tk.Button(master=frame,text="Check Out",width=x,command=check_out.open_check_out_window) # Call check_out window
        butCheckOut.grid(row=2,column=1,padx=pad_space,pady=pad_space,sticky='nsew')

        # Button Show Available Room
        butShowRoom = tk.Button(master=frame,text="Show Room Situation",width=x,command=show_room_situation.open_show_room_situation) # Call show_room_situation 
        butShowRoom.grid(row=3,column=1,padx=pad_space,pady=pad_space,sticky='nsew')

        # Button Quit 
        butQuit = tk.Button(master=frame,text="Quit",command=quit,width=x)
        butQuit.grid(row=4,column=1,padx=pad_space,pady=pad_space,sticky='nsew')

def home():
    root = tk.Tk()
    mainWindow = windowApp(root)
    root.mainloop()
    
if __name__ == "__main__":
    home()