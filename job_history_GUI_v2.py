from tkinter import *
from functools import partial  # To prevent unwanted windows
from PIL import ImageTk, Image  # To present logo


class MobileService:
    def __init__(self, parent):
        # Formatting Variables
        background_colour = "red"

        self.jobs_list = ["job number 1 customer name hannah cost is 500",
                          "job number 2 customer name mandy cost is 40",
                          "job number 3 customer name lisa cost is 200",]

        # Service main screen GUI
        self.GUI_frame = Frame(bg=background_colour,
                               pady=10)
        self.GUI_frame.grid()

        # Logo
        img = PhotoImage(file='logo.png')

        self.logo_label = Label(self.GUI_frame, image=img)
        self.logo_label.img = img
        self.logo_label.grid(row=0)

        # Mobile Service Logo (row 0)
        self.mobile_service_label = Label(self.GUI_frame, text="Mobile Service",
                                          font="Arial 19 bold",
                                          bg=background_colour,
                                          padx=10, pady=10)
        self.mobile_service_label.grid(row=1)

        # Imformation Text (row 1)
        self.information_label = Label(self.GUI_frame,
                                       text="Help text here",
                                       font="Arial 10 bold",
                                       wrap=250, justify=LEFT,
                                       fg="maroon", bg=background_colour,
                                       padx=10, pady=10)
        self.information_label.grid(row=2)

        # Buttons frame
        self.buttons_frame = Frame(self.GUI_frame)
        self.buttons_frame.grid(row=3)

        # Enter Job Button (row 2)
        self.enter_job_button = Button(self.buttons_frame, text="Enter New Job",
                                       command=lambda: self.to_job())
        self.enter_job_button.grid(row=0, column=0)

        # History Button (row 2)
        self.history_button = Button(self.buttons_frame, text="Job History",
                                     command=lambda: self.to_history(self.jobs_list),state=DISABLED)
        self.history_button.grid(row=0, column=1)

        if len(self.jobs_list) >= 1:
            self.history_button.config(state=NORMAL)

    def to_job(self):
        EnterJob(self)

    def to_history(self,jobs_list):
        History(self,jobs_list)

class EnterJob:
    def __init__(self, partner):
        # Disable New Job Button
        partner.enter_job_button.config(state=DISABLED)

        # Job Window
        self.job_box = Toplevel()

        # Close Job Window
        self.job_box.protocol('WM_DELETE_WINDOW', partial(self.close_job, partner))

        # GUI Frame Set Up
        self.job_frame = Frame(self.job_box)
        self.job_frame.grid()

        # Logo
        img = PhotoImage(file='logo.png')
        self.logo_label = Label(self.job_frame, image=img)
        self.logo_label.img = img
        self.logo_label.grid(row=0)

        # Set Up Heading (row 0)
        self.job_heading = Label(self.job_frame, text="Enter New Job Details",
                                 font="arial 19 bold", padx=10, pady=10)
        self.job_heading.grid(row=1)

        # Buttons frame
        self.job_buttons_frame = Frame(self.job_frame)
        self.job_buttons_frame.grid(row=2)

        # Show All Jobs Button (row 2)
        self.save_button = Button(self.job_buttons_frame, text="Save")
        self.save_button.grid(row=0, column=0)

        # Previous Job Button (row 2)
        self.cancel_button = Button(self.job_buttons_frame, text="Cancel", command=lambda: self.close_job(partner))
        self.cancel_button.grid(row=0, column=1)

    def close_job(self, partner):
        partner.enter_job_button.config(state=NORMAL)
        self.job_box.destroy()


class History():
    def __init__(self, partner,jobs_list):
        # Disable New Job Button
        partner.history_button.config(state=DISABLED)

        self.counter = 0

        # Job Window
        self.history_box = Toplevel()

        # Close Job Window
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # GUI Frame Set Up
        self.history_frame = Frame(self.history_box)
        self.history_frame.grid()

        # Logo
        img = PhotoImage(file='logo.png')
        self.logo_label = Label(self.history_frame, image=img)
        self.logo_label.img = img
        self.logo_label.grid(row=0)

        # Set Up Heading (row 0)
        self.history_heading = Label(self.history_frame, text="Job History",
                                     font="arial 19 bold", padx=10, pady=10)
        self.history_heading.grid(row=1)

        # Display frame
        self.display_frame = Frame(self.history_frame)
        self.display_frame.grid(row=2)

        # Job Text
        self.job_overview = Label(self.display_frame, text=jobs_list[self.counter],
                                  font="arial 14 bold")
        self.job_overview.grid(row=0)

        # Buttons frame
        self.history_buttons_frame = Frame(self.history_frame)
        self.history_buttons_frame.grid(row=3)

        # Previous Job Button (row 2)
        self.previous_button = Button(self.history_buttons_frame, text="Previous",state=DISABLED,command=lambda:self.previous(self.counter, jobs_list))
        self.previous_button.grid(row=0, column=0)

        # Next Job Button (row 2)
        self.next_button = Button(self.history_buttons_frame, text="Next",command=lambda:self.next(self.counter, jobs_list))
        self.next_button.grid(row=0, column=1)

    def next(self, counter, jobs_list):
        self.counter +=1
        self.job_overview.config(text=jobs_list[self.counter])
        self.check_button(jobs_list)

    def previous(self, counter, jobs_list):
        self.counter -=1
        self.job_overview.config(text=jobs_list[self.counter])
        self.check_button(jobs_list)

    def check_button(self,jobs_list):
        if self.counter < len(jobs_list)-1:
            self.next_button.config(state=NORMAL)
        if self.counter == len(jobs_list)-1:
            self.next_button.config(state=DISABLED)
        if self.counter > 0:
            self.previous_button.config(state=NORMAL)
        if self.counter == 0:
            self.previous_button.config(state=DISABLED)

    def close_history(self, partner):
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Suzy's Mobile Service")
    something = MobileService(root)
    root.mainloop()





