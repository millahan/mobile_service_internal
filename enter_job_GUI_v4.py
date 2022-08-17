from tkinter import *
from functools import partial  # To prevent unwanted windows
from PIL import ImageTk, Image  # To present logo


class MobileService:
    def __init__(self, parent):
        # Formatting Variables
        background_colour = "red"

        self.jobs_list = []

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

        # Entry Frame (row 2)
        self.entry_error_frame = Frame(self.GUI_frame, width=200,)
        self.entry_error_frame.grid(row=3)

        # Job Number
        self.job_number_title = Label(self.entry_error_frame, text="Job Number:",
                                      font="arial 14 bold", padx=10, pady=10)
        self.job_number_title.grid(row=0, column=0)
        self.job_number_entry = Entry(self.entry_error_frame,
                                      font="Arial 14 bold", width=10)
        self.job_number_entry.grid(row=0, column=1)

        # Job Error
        self.job_error_label = Label(self.entry_error_frame, fg="maroon",
                                     text="", font="Arial 10 bold", wrap=275,
                                     justify=LEFT)
        self.job_error_label.grid(row=1, columnspan=2, pady=5)

        # Enter Customer Name
        self.customer_name_title = Label(self.entry_error_frame, text="Customer Full Name:",
                                         font="arial 14 bold", padx=10, pady=10)
        self.customer_name_title.grid(row=2, column=0)
        self.customer_name_entry = Entry(self.entry_error_frame,
                                         font="Arial 14 bold", width=10)
        self.customer_name_entry.grid(row=2, column=1)

        # Customer Error
        self.customer_name_label = Label(self.entry_error_frame, fg="maroon",
                                         text="", font="Arial 10 bold", wrap=275,
                                         justify=LEFT)
        self.customer_name_label.grid(row=3, columnspan=2, pady=5)

        # Distance Travelled
        self.distance_title = Label(self.entry_error_frame, text="Distance Travelled:",
                                    font="arial 14 bold", padx=10, pady=10)
        self.distance_title.grid(row=4, column=0)
        self.distance_entry = Entry(self.entry_error_frame,
                                    font="Arial 14 bold", width=10)
        self.distance_entry.grid(row=4, column=1)

        # Distance Error
        self.distance_error_label = Label(self.entry_error_frame, fg="maroon",
                                          text="", font="Arial 10 bold", wrap=275,
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
                                          text="Virus protection required",
                                          font="Arial 10 italic",
                                          justify=LEFT,
                                          padx=10, variable=self.virus_checked,
                                          command=is_checked)
        self.virus_checkbox.grid(row=6, column=0)

        # Virus Minutes Entry
        self.minutes_entry = Entry(self.entry_error_frame, width=25,
                                   font="Arial 14 bold",
                                   bg="white", state="disabled")
        self.minutes_entry.grid(row=6, column=1)

        # checkbox for WOF and tune to minimise errors
        self.wof_checked = BooleanVar()
        self.wof_checkbox = Checkbutton(self.entry_error_frame,
                                        text='WOF and tune required',
                                        font="Arial 10 italic",
                                        justify=LEFT,
                                        padx=10, variable=self.wof_checked,
                                        command=is_checked)
        self.wof_checkbox.grid(row=7, column=0)

        # Virus Minutes Error
        self.virus_error_label = Label(self.entry_error_frame, fg="maroon",
                                       text="", font="Arial 10 bold", wrap=275,
                                       justify=LEFT)
        self.virus_error_label.grid(row=8, columnspan=2, pady=5)

        # Buttons frame (row 3)
        self.job_buttons_frame = Frame(self.GUI_frame)
        self.job_buttons_frame.grid(row=4)

        # Save Jobs Button (row 0)
        self.save_button = Button(self.job_buttons_frame, text="Save", command=self.check_input, state=DISABLED)
        self.save_button.grid(row=0, column=0)

        # History Button (row 0)
        self.history_button = Button(self.job_buttons_frame, text="Job History", command=lambda: self.to_history())
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
        j_error = "no"
        d_error = "no"
        m_error = "no"
        c_error = "no"

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

        except ValueError:
            d_error = "yes"
            error_feedback = "Please enter a distance in KM (no text/decimals)."
            self.distance_entry.config(bg=error_back)
            self.distance_error_label.config(text=error_feedback)

        try:
            minutes = int(minutes)

        except ValueError:
            m_error = "yes"
            error_feedback = "Please enter minutes (no text/decimals)."
            self.minutes_entry.config(bg=error_back)
            self.virus_error_label.config(text=error_feedback)

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

        print(f"inital cost is {cost}")

        def round_decimals_up(distance):
            # Returns a value rounded up to a specific number of decimal places.
            rounded_distance = math.ceil(distance)
            return rounded_distance

        if (distance % 1) < .5:
            rounded_distance = round(distance)
        else:
            rounded_distance = round_decimals_up(distance)
        print(rounded_distance)

        if rounded_distance > 5:
            distance_to_pay = rounded_distance - 5
            cost += distance_to_pay * .5
            print(f"Distance cost is {cost}")

        if wof_required == 1:
            cost += 100
            print(f"Distance and wof is {cost}")

        if virus_required == 1:
            minutes_on_virus = float(self.minutes_entry.get())
            virus_fee = minutes_on_virus * .8
            cost += virus_fee
            print(f"Distance and wof and virus is {cost}")

        self.job_info = f"job no: {job_number}. customer: {customer_name}. fees: {cost}"
        self.jobs_list.append(self.job_info)
        print(self.jobs_list)

    def to_history(self):
        History(self)

class History:
    def __init__(self, partner):
        # Disable New Job Button
        partner.history_button.config(state=DISABLED)

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
        self.job_overview = Label(self.display_frame, text="Job details here",
                                  font="arial 14 bold")
        self.job_overview.grid(row=0)

        # Buttons frame
        self.history_buttons_frame = Frame(self.history_frame)
        self.history_buttons_frame.grid(row=2)

        # Previous Job Button (row 2)
        self.previous_button = Button(self.history_buttons_frame, text="Previous")
        self.previous_button.grid(row=0, column=0)

        # Next Job Button (row 2)
        self.next_button = Button(self.history_buttons_frame, text="Next")
        self.next_button.grid(row=0, column=1)

    def close_history(self, partner):
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Suzy's Mobile Service")
    something = MobileService(root)
    root.mainloop()





