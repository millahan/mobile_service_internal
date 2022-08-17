from tkinter import *
from functools import partial  # To prevent unwanted windows
import math

class MobileService:
    def __init__(self, parent):
        # Formatting Variables
        background_colour = "#caf0f8"

        self.jobs_list = []

        # Service main screen GUI
        self.GUI_frame = Frame(pady=10, padx =10, bg=background_colour)
        self.GUI_frame.grid()

        # Logo
        img = PhotoImage(file='logo.png')

        self.logo_label = Label(self.GUI_frame, image=img)
        self.logo_label.img = img
        self.logo_label.grid(row=0)

        # Mobile Service Logo (row 0)
        self.mobile_service_label = Label(self.GUI_frame, text="Mobile Service Job Calculator",
                                          font="Arial 19 bold", bg=background_colour,
                                          padx=10, pady=10)
        self.mobile_service_label.grid(row=1)

        # Imformation Text (row 1)
        self.information_label = Label(self.GUI_frame,
                                       text="Please enter relevent job details in the fields below and select at least once service. For virus protection, please enter the amount of minutes spent.",
                                       font="Arial 10 italic",
                                       wrap=365, justify=LEFT,bg=background_colour,
                                       padx=10, pady=10)
        self.information_label.grid(row=2)

        # Entry Frame (row 2)
        self.entry_error_frame = Frame(self.GUI_frame, width=200,bg=background_colour)
        self.entry_error_frame.grid(row=3)

        # Job Number
        self.job_number_title = Label(self.entry_error_frame, text="Job Number:",
                                      font="arial 14", padx=10, pady=10,bg=background_colour)
        self.job_number_title.grid(row=0, column=0)
        self.job_number_entry = Entry(self.entry_error_frame,
                                      font="Arial 12", width=12)
        self.job_number_entry.grid(row=0, column=1)

        # Job Error
        self.job_error_label = Label(self.entry_error_frame, fg="maroon",
                                     text="", font="Arial 10 bold", wrap=275,bg=background_colour,
                                     justify=LEFT)
        self.job_error_label.grid(row=1, columnspan=2, pady=5)

        # Enter Customer Name
        self.customer_name_title = Label(self.entry_error_frame, text="Customer Full Name:",
                                         font="arial 14", padx=10,bg=background_colour, pady=10)
        self.customer_name_title.grid(row=2, column=0)
        self.customer_name_entry = Entry(self.entry_error_frame,
                                         font="Arial 12", width=12)
        self.customer_name_entry.grid(row=2, column=1)

        # Customer Error
        self.customer_name_label = Label(self.entry_error_frame, fg="maroon",
                                         text="", font="Arial 10 bold", bg=background_colour,wrap=275,
                                         justify=LEFT)
        self.customer_name_label.grid(row=3, columnspan=2, pady=5)

        # Distance Travelled
        self.distance_title = Label(self.entry_error_frame, text="Distance Travelled (km):",
                                    font="arial 14", padx=10,bg=background_colour, pady=10)
        self.distance_title.grid(row=4, column=0)
        self.distance_entry = Entry(self.entry_error_frame,
                                    font="Arial 12", width=12)
        self.distance_entry.grid(row=4, column=1)

        # Distance Error
        self.distance_error_label = Label(self.entry_error_frame, fg="maroon",
                                          text="", font="Arial 10 bold", bg=background_colour,wrap=275,
                                          justify=LEFT)
        self.distance_error_label.grid(row=5, columnspan=2, pady=5)

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
                                          text="Virus Protection:",
                                          font="Arial 14",
                                          justify=LEFT,bg=background_colour,
                                          padx=10, variable=self.virus_checked,
                                          command=is_checked)
        self.virus_checkbox.grid(row=6, column=0)

        # Virus Minutes Entry
        self.minutes_entry = Entry(self.entry_error_frame, width=12,
                                   font="Arial 12",
                                   bg="white", state="disabled")
        self.minutes_entry.grid(row=6, column=1)

        # checkbox for WOF and tune to minimise errors
        self.wof_checked = BooleanVar()
        self.wof_checkbox = Checkbutton(self.entry_error_frame,
                                        text='WOF and Tune',
                                        font="Arial 14",bg=background_colour,
                                        justify=LEFT,
                                        padx=10, variable=self.wof_checked,
                                        command=is_checked)
        self.wof_checkbox.grid(row=7, column=0)

        # Virus Minutes Error
        self.virus_error_label = Label(self.entry_error_frame, fg="maroon",
                                       text="", font="Arial 10 bold",bg=background_colour, wrap=275,
                                       justify=LEFT)
        self.virus_error_label.grid(row=8, columnspan=2, pady=5)

        # Buttons frame (row 3)
        self.job_buttons_frame = Frame(self.GUI_frame)
        self.job_buttons_frame.grid(row=4)

        # Save Jobs Button (row 0)
        self.save_button = Button(self.job_buttons_frame, bg= "#90e0ef",text="Save", font="Arial 10 bold",command=self.check_input, state=DISABLED)
        self.save_button.grid(row=0, column=0)

        # History Button (row 2)
        self.history_button = Button(self.job_buttons_frame, bg= "#90e0ef",font="Arial 10 bold", text="Job History",state=DISABLED,
                                     command=lambda: self.to_history(self.jobs_list))
        self.history_button.grid(row=0, column=1)

    def check_input(self):
        job_number = self.job_number_entry.get()
        customer_name = self.customer_name_entry.get()
        distance = self.distance_entry.get()
        virus_required = self.virus_checked.get()
        minutes = self.minutes_entry.get()

        if virus_required == 0:
            minutes = 0

        # Set error background colours (and assume that there are no errors at start)
        error_back = "#FFAFAF"

        # change background to white (for testing purposes)
        self.job_number_entry.config(bg="white")
        self.job_error_label.config(text="")

        self.distance_entry.config(bg="white")
        self.distance_error_label.config(text="")

        self.minutes_entry.config(bg="white")
        self.virus_error_label.config(text="")

        self.customer_name_entry.config(bg="white")
        self.customer_name_label.config(text="")

        try:
            job_number = int(job_number)
            j_error = "no"

            if job_number < 0:
                j_error = "yes"
                error_feedback = "Negative numbers not allowed."
                self.job_number_entry.config(bg=error_back)
                self.job_error_label.config(text=error_feedback)

        except ValueError:
            j_error = "yes"
            error_feedback = "Please enter a job number (no text/decimals)."
            self.job_number_entry.config(bg=error_back)
            self.job_error_label.config(text=error_feedback)

        try:
            distance = float(distance)
            d_error = "no"

            if distance <= 0 or distance >= 100:
                d_error = "yes"
                error_feedback = "Please enter a distance between 0 and 100km)."
                self.distance_entry.config(bg=error_back)
                self.distance_error_label.config(text=error_feedback)

        except ValueError:
            d_error = "yes"
            error_feedback = "Please enter a distance in KM (no text)."
            self.distance_entry.config(bg=error_back)
            self.distance_error_label.config(text=error_feedback)

        try:
            minutes = int(minutes)
            m_error = "no"

            if minutes < 0 or minutes > 480:
                m_error = "yes"
                error_feedback = "Please enter the time taken on virus protection between 0 and 480 minutes."
                self.minutes_entry.config(bg=error_back)
                self.virus_error_label.config(text=error_feedback)

        except ValueError:
            m_error = "yes"
            error_feedback = "Please enter minutes (no text/decimals)."
            self.minutes_entry.config(bg=error_back)
            self.virus_error_label.config(text=error_feedback)

        c_error = "no"
        if customer_name == "":
            c_error = "yes"
            error_feedback = "Please enter a customer name."
            self.customer_name_entry.config(bg=error_back)
            self.customer_name_label.config(text=error_feedback)


        if j_error == "no" and d_error == "no" and m_error == "no" and c_error == "no":
            self.calc_cost(self)

    def calc_cost(self, partner):

        # Lists

        job_number = self.job_number_entry.get()
        customer_name = self.customer_name_entry.get()
        distance = float(self.distance_entry.get())
        virus_required = self.virus_checked.get()
        wof_required = self.wof_checked.get()

        cost = 10
        cost = int(cost)

        def round_decimals_up(distance):
            # Returns a value rounded up to a specific number of decimal places.
            rounded_distance = math.ceil(distance)
            return rounded_distance

        if (distance % 1) < .5:
            rounded_distance = round(distance)
        else:
            rounded_distance = round_decimals_up(distance)
            
        if rounded_distance > 5:
            distance_to_pay = rounded_distance - 5
            cost += distance_to_pay * .5

        if wof_required == 1:
            cost += 100

        if virus_required == 1:
            minutes_on_virus = float(self.minutes_entry.get())
            virus_fee = minutes_on_virus * .8
            cost += virus_fee

        name = customer_name.title()
        
        m_error = "yes"
        error_feedback = f"{name}'s information has been saved! Press job history to view."
        self.virus_error_label.config(text=error_feedback)

        self.job_info = f"""Job Number: {job_number}
Customer: {name}
Total Service Cost: ${cost:.2f}
"""
        self.jobs_list.append(self.job_info)
        if len(self.jobs_list) >= 1:
            self.history_button.config(state=NORMAL)
            
    def to_history(self,jobs_list):
        History(self,jobs_list)

class History():
    def __init__(self, partner,jobs_list):
        # Disable New Job Button
        partner.history_button.config(state=DISABLED)

        #Formatting variables
        background_colour = "#90e0ef"
        
        #Set up Counter
        self.counter = 0

        # Job Window
        self.history_box = Toplevel()

        # Close Job Window
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # GUI Frame Set Up
        self.history_frame = Frame(self.history_box,bg=background_colour)
        self.history_frame.grid()

        # Logo
        img = PhotoImage(file='logo.png')
        self.logo_label = Label(self.history_frame, image=img)
        self.logo_label.img = img
        self.logo_label.grid(row=0)

        # Set Up Heading (row 0)
        self.history_heading = Label(self.history_frame, text="Job History",
                                     font="arial 19 bold", padx=10, pady=10,bg=background_colour)
        self.history_heading.grid(row=1)

        # Display frame
        self.display_frame = Frame(self.history_frame,bg=background_colour)
        self.display_frame.grid(row=2)

        # Job Text
        self.job_overview = Label(self.display_frame, text=jobs_list[self.counter],
                                  font="arial 12",bg=background_colour)
        self.job_overview.grid(row=0)

        # Buttons frame
        self.history_buttons_frame = Frame(self.history_frame)
        self.history_buttons_frame.grid(row=3)

        # Previous Job Button (row 2)
        self.previous_button = Button(self.history_buttons_frame,bg="#caf0f8", text="Previous",state=DISABLED,command=lambda:self.previous(self.counter, jobs_list))
        self.previous_button.grid(row=0, column=0)

        # Next Job Button (row 2)
        self.next_button = Button(self.history_buttons_frame, bg="#caf0f8",text="Next",command=lambda:self.next(self.counter, jobs_list))
        self.next_button.grid(row=0, column=1)

        if len(jobs_list) == 1:
            self.next_button.config(state=DISABLED)

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





