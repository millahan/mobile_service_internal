#Hannah Millward
#August 2022
#Trial 2: Show a single error message

from tkinter import *
from functools import partial  # To prevent unwanted windows
from PIL import ImageTk, Image  # To present logo

class MobileService:
    def __init__(self, parent):
        # Formatting Variables
        background_colour = "red"

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
                                     command=lambda: self.to_history())
        self.history_button.grid(row=0, column=1)

    def to_job(self):
        EnterJob(self)

    def to_history(self):
        History(self)

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

        #Variables
        self.job_numbers = []
        self.customer_names = []
        self.distances = []
        self.minutes = []
        self.wofs = []

        # Logo (row 0)
        img = PhotoImage(file='logo.png')
        self.logo_label = Label(self.job_frame, image=img)
        self.logo_label.img = img
        self.logo_label.grid(row=0)

        # Set Up Heading (row 1)
        self.job_heading = Label(self.job_frame, text="Enter New Job Details",
                                 font="arial 19 bold", padx=10, pady=10)
        self.job_heading.grid(row=1)

        #Entry Frame (row 2)
        self.entry_error_frame = Frame(self.job_frame, width=200)
        self.entry_error_frame.grid(row=2)

        #Error Text
        self.error_label = Label(self.entry_error_frame, fg="maroon",
                                        text="", font="Arial 10 bold", wrap=275,
                                        justify=LEFT)
        self.error_label.grid(row=0, columnspan=2, pady=5)

        #Job Number
        self.job_number_title = Label(self.entry_error_frame, text="Job Number:",
                                font="arial 14 bold", padx=10, pady=10)
        self.job_number_title.grid(row=1, column=0)
        self.job_number_entry = Entry(self.entry_error_frame,
                                        font="Arial 14 bold", width=10)
        self.job_number_entry.grid(row=1, column=1)


        #Enter Customer Name
        self.customer_name_title = Label(self.entry_error_frame, text="Customer Full Name:",
                                 font="arial 14 bold", padx=10, pady=10)
        self.customer_name_title.grid(row=2, column=0)
        self.customer_name_entry = Entry(self.entry_error_frame,
                                        font="Arial 14 bold", width=10)
        self.customer_name_entry.grid(row=2, column=1)

        #Distance Travelled
        self.distance_title = Label(self.entry_error_frame, text="Distance Travelled:",
                                font="arial 14 bold", padx=10, pady=10)
        self.distance_title.grid(row=3, column=0)
        self.distance_entry = Entry(self.entry_error_frame,
                                        font="Arial 14 bold", width=10)
        self.distance_entry.grid(row=3, column=1)

        # enables elements based on checkbox inputs
        def is_checked():
            # enables minutes spent entry once checkbox selected
            if self.virus_checked.get() == 0:
                self.minutes_entry.config(state="disabled")
            else:
                self.minutes_entry.config(state="normal")
            # enables enter job button if at least one checkbox selected
            if (self.virus_checked.get() == 0) & (self.wof_checked.get() == 0):
                self.save_button.config(state="disabled")
            else:
                self.save_button.config(state="normal")

        # checkbox for virus protection
        self.virus_checked = BooleanVar()
        self.virus_checkbox = Checkbutton(self.entry_error_frame,
                                                     text="Virus protection required",
                                                     font="Arial 10 italic",
                                                     justify=LEFT,
                                                     padx=10, variable=self.virus_checked,
                                                     command=is_checked)
        self.virus_checkbox.grid(row=5, column=0)

        self.minutes_entry = Entry(self.entry_error_frame, width=25,
                                                    font="Arial 12",
                                                    bg="white", state="disabled")
        self.minutes_entry.grid(row=5, column=1)

        # checkbox for WOF and tune to minimise errors
        self.wof_checked = BooleanVar()
        self.wof_checkbox = Checkbutton(self.entry_error_frame,
                                             text='WOF and tune required',
                                             font="Arial 10 italic",
                                             justify=LEFT,
                                             padx=10, variable=self.wof_checked,
                                             command=is_checked)
        self.wof_checkbox.grid(row=6, column=0)


        # Buttons frame (row 3)
        self.job_buttons_frame = Frame(self.job_frame)
        self.job_buttons_frame.grid(row=3)

        # Save Jobs Button (row 2)
        self.save_button = Button(self.job_buttons_frame, text="Save", command=self.check_input, state = DISABLED)
        self.save_button.grid(row=0, column=0)

        # Cancel Input Button (row 2)
        self.cancel_button = Button(self.job_buttons_frame, text="Cancel", command=lambda: self.close_job(partner))
        self.cancel_button.grid(row=0, column=1)

    def check_input(self):
        job_number = self.job_number_entry.get()
        distance = self.distance_entry.get()
        virus_required = self.virus_checked.get()
        minutes = self.minutes_entry.get()

        if virus_required == 0:
            minutes = 0

        # Set error background colours (and assume that there are no errors at start)
        error_back = "#FFAFAF"
        j_error = "no"
        d_error = "no"
        m_error = "no"

        # change background to white (for testing purposes)
        self.job_number_entry.config(bg="white")
        self.error_label.config(text="")
        self.distance_entry.config(bg="white")
        self.minutes_entry.config(bg="white")

        try:
            job_number = int(job_number)

        except ValueError:
            j_error = "yes"
            self.job_number_entry.config(bg=error_back)

        try:
            distance = float(distance)

        except ValueError:
            d_error = "yes"
            self.distance_entry.config(bg=error_back)

        try:
            minutes = int(minutes)

        except ValueError:
            m_error = "yes"
            self.minutes_entry.config(bg=error_back)

        if j_error == "yes" or d_error == "yes" or m_error == "yes":
            error_feedback = "Please enter correct information in all fields."
            self.error_label.config(text=error_feedback)
        else:
            self.calc_cost(self)

    def calc_cost(self,partner):
        print("Made it to calc function")

    def close_job(self, partner):
        partner.enter_job_button.config(state=NORMAL)
        self.job_box.destroy()



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Suzy's Mobile Service")
    something = MobileService(root)
    root.mainloop()





