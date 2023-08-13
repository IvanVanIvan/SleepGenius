# import modules
import tkinter as tk
import subprocess
from tkinter import messagebox
from PIL import Image, ImageTk


# Define a class for the input page
class InputPage:
    def __init__(self):
        # Create the main application window
        self.Input_screen = tk.Tk()
        # Set the window title
        self.Input_screen.title("Input Page")
        # Set the window size to 350x500 pixels
        self.Input_screen.geometry("350x500")
        # Set the background color to black
        self.Input_screen.configure(bg="black")


        # Load and display the image
        # open image
        self.image = Image.open("assets\LogoY13.png")
        # Resize the image to 75x75 pixels
        self.image = self.image.resize((75, 75)) 
        # Convert the image to a format compatible with Tkinter
        self.image_tk = ImageTk.PhotoImage(self.image)
        # Create a label to display the image
        self.image_label = tk.Label(self.Input_screen, image=self.image_tk, bg="black")
        # Set the position of the image label
        self.image_label.place(x=275, y=5)  


        # Create a label to display the app name
        self.app_label = tk.Label(self.Input_screen, text="Sleep \n Genius", bg="black", fg="#FFDE59", width="6", height="2", font=("Blinker", 15, "bold"))
        # Set the position of the label
        self.app_label.place(x=200, y=15)


        # Create a label to display the let's message
        self.lets_label = tk.Label(self.Input_screen, text="Let's", bg="black", fg="white", width="10", height="2", font=("Blinker", 20, "bold"))
        # Set the position of the label
        self.lets_label.place(x=5, y=100)


        # Create a label to display get started message
        self.start_label = tk.Label(self.Input_screen, text="Get started", bg="black", fg="#FFDE59", width="10", height="2", font=("Blinker", 20, "bold"))
        # Set the position of the label
        self.start_label.place(x=45, y=150)


        # Create a label to display the message
        self.message_label = tk.Label(self.Input_screen, text="Please enter your sleep data below", bg="black", fg="#0CC0DF")
        # Set the position of the label
        self.message_label.place(x=60, y=220)


        # Create a label to display number of hrs message
        self.numHrs_label = tk.Label(self.Input_screen, text="Number of hours \n slept* ", bg="black", fg="white")
        # Set the position of the label
        self.numHrs_label.place(x=50, y=290)
        # Create an Entry widget
        self.hours_entry = tk.Entry(self.Input_screen)
        # Set the position of the label
        self.hours_entry.place(x=160, y=290)

        # Create the button to Logout
        self.logout_button = tk.Button(self.Input_screen, text="Logout", bg="#0CC0DF", fg="white", height="2", width="11", cursor="hand2", command = self.Logout)
        # Set the position of the button
        self.logout_button.place(x=20, y=20)

        # Create Submit button
        self.submit_button = tk.Button(self.Input_screen, text="Submit", bg="#0CC0DF", fg="white", height="2", width="30", cursor="hand2", command= self.save_sleep_data)
        # Set the position of the button
        self.submit_button.place(x=50, y=380)

        # switch to History page message
        self.msgHistP_label = tk.Label(self.Input_screen, text="View previous result", bg="black", fg="#0CC0DF", width="20", height="1", font=("Blinker", 10, "bold"))
        # Set the position of the label
        self.msgHistP_label.place(x=30, y=440)

        # Create the button to switch to History page
        self.switchHisP_button = tk.Button(self.Input_screen, text="Here", bg="#FFDE59", fg="#0CC0DF", height="1", width="10", cursor="hand2", command = self.open_History_page)
        # Set the position of the button
        self.switchHisP_button.place(x=190, y=440)
        

    # save sleep data function 
    def save_sleep_data(self):
        try:
            hours_slept = float(self.hours_entry.get())
            if 1 <= hours_slept <= 24:
                # Round to two decimal places
                hours_slept = round(hours_slept, 2)
                # display the syccess message
                messagebox.showinfo("Success", "Your result has been recorded")

                # record the hours into text file for later use
                with open("txt_Files\HourInput.txt", "w") as hours_file:
                    hours_file.write(f"{hours_slept}")

                # open the result file
                self.open_result_page()
            else:
                # show error message when the number is too big
                messagebox.showwarning("Invalid Input", "The number of hours slept should be between 1 and 24.")
        except ValueError:
            # show error message when user doesnt input a number
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    
    # function that will clear the text file, used when loging out and when switching a file thats a step back
    def clearHoursTXT(self):
        # open the txt file in write mode
        with open("txt_Files\HourInput.txt", "w") as hoursSlept_file:
            # truncating the file to a size of 0 bytes, which effectively deletes the contents of the file
            hoursSlept_file.truncate(0)
    
    # function that will clear the text file, used when loging out and when switching a file thats a step back
    def clearUNameTXT(self):
        # open the txt file in write mode
        with open(r"txt_Files\UserName.txt", "w") as username_file:
            # truncating the file to a size of 0 bytes, which effectively deletes the contents of the file
            username_file.truncate(0)
    

    def open_result_page(self):
        # Open the SG_Version3\Result_PageV3.py file using subprocess
        subprocess.Popen(["python", "SG_Version3\Result_PageV3.py"])
        # Close the main screen
        self.Input_screen.destroy()
    
    # open the history page
    def open_History_page(self):
        # Open the SG_Version3\History_ResultsV3.py file using subprocess
        subprocess.Popen(["python", "SG_Version3\History_ResultsV3.py"])
        # Close the main screen
        self.Input_screen.destroy()
    
    # function to logout
    def Logout(self):
        # delete data from username txt file
        self.clearUNameTXT()
        # Open the SG_Version3\landingV3.py file using subprocess
        subprocess.Popen(["python", "SG_Version3\landingV3.py"])
        # Close the Input_screen screen
        self.Input_screen.destroy()

    def run(self):
        # This line starts the event loop and keeps the application running.
        self.Input_screen.mainloop()

if __name__ == "__main__":
    # Create an instance of the InputPage class
    input_page = InputPage()
    # Start the Tkinter main event loop by calling the run() method.
    # This line will keep the application responsive to user interactions.
    input_page.run()