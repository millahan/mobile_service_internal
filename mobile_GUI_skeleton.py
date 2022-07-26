from tkinter import *
from functools import partial #To prevent unwanted windows
from PIL import ImageTk, Image #To present logo

class MobileService:
    def __init__(self,parent):

        #Formatting Variables
        background_colour = "red"

        # Service main screen GUI
        self.GUI_frame = Frame(width=300, height=300, bg=background_colour,
                                     pady=10)
        self.GUI_frame.grid()

        #Mobile Service Logo (row 0)
        self.mobile_service_label = Label(self.GUI_frame, text = "Mobile Service",
                                            font="Arial 19 bold",
                                          bg=background_colour,
                                          padx=10, pady=10)
        self.mobile_service_label.grid(row=0)

        #Imformation Text (row 1)
        self.information_label = Label(self.GUI_frame,
                                       text = "Help text here",
                                      font="Arial 10 bold",
                                       wrap=250, justify=LEFT,
                                       fg = "maroon", bg=background_colour,
                                       padx=10, pady=10)
        self.information_label.grid(row=1)

        #Enter Job Button (row 2)
        self.enter_job_button = Button(self.GUI_frame, text="Enter New Job",
                                  command=lambda:self.to_job())
        self.enter_job_button.grid(row=2, column=0)

        #History Button (row 2)
        self.history_button = Button(self.GUI_frame, text="Job History",
                                  command=lambda:self.to_history())
        self.history_button.grid(row=2, column=1)

    def to_job(self):
        EnterJob(self)

    def to_history(self):
        History(self)

class EnterJob:
    def __init__(self, partner):

        #Disable New Job Button
        partner.enter_job_button.config(state=DISABLED)
        
        #Job Window
        self.job_box = Toplevel()

        #Close Job Window
        self.job_box.protocol('WM_DELETE_WINDOW', partial(self.close_job, partner))

        #GUI Frame Set Up
        self.job_frame = Frame(self.job_box)
        self.job_frame.grid()

        #Set Up Heading (row 0)
        self.job_heading = Label(self.job_frame, text = "Enter New Job Details",
                                 font="arial 19 bold", padx=10, pady=10)
        self.job_heading.grid(row=0)

    def close_job(self,partner):
        partner.enter_job_button.config(state=NORMAL)
        self.job_box.destroy()
        
class History:
    def __init__(self, partner):

        #Disable New Job Button
        partner.history_button.config(state=DISABLED)
        
        #Job Window
        self.history_box = Toplevel()

        #Close Job Window
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        #GUI Frame Set Up
        self.history_frame = Frame(self.history_box)
        self.history_frame.grid()

        #Set Up Heading (row 0)
        self.history_heading = Label(self.history_frame, text = "Job History",
                                 font="arial 19 bold", padx=10, pady=10)
        self.history_heading.grid(row=0)

        #Show All Jobs Button (row 2)
        self.show_all = Button(self.history_frame, text="Show All")
        self.show_all.grid(row=2, column=0)

        #Previous Job Button (row 2)
        self.previous_button = Button(self.history_frame, text="Previous")
        self.previous_button.grid(row=2, column=1)

        #Next Job Button (row 2)
        self.next_button = Button(self.history_frame, text="Next")
        self.next_button.grid(row=2, column=2)

    def close_history(self,partner):
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

#main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Suzy's Mobile Service")
    something = MobileService(root)
    root.mainloop()




        
