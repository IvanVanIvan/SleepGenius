# import modules
import tkinter as tk
import subprocess
from PIL import Image, ImageTk
import sqlite3


# Define a class for the history page
class HistoryResults:
    def __init__(self):
        # Create the main application window
        self.HistoryScreen = tk.Tk()
        # Set the window size to 350x500 pixels
        self.HistoryScreen.geometry("350x500")
        # Set the window title
        self.HistoryScreen.title("History")
        # Set the background color to black
        self.HistoryScreen.configure(bg="black")

        # Load and display the image
        # open image 
        self.image = Image.open("assets\LogoY13.png") 
        # Resize the image to 100x100 pixels
        self.image = self.image.resize((75, 75)) 
        # Convert the image to a format compatible with Tkinter
        self.image_tk = ImageTk.PhotoImage(self.image)
        # Create a label to display the image
        self.image_label = tk.Label(self.HistoryScreen, image=self.image_tk, bg="black")
        # Set the position of the image label
        self.image_label.place(x=275, y=5)

        # Create a label to display the app name
        self.app_label = tk.Label(self.HistoryScreen, text="Sleep \n Genius", bg="black", fg="#FFDE59", width="6", height="2", font=("Blinker", 15, "bold"))
        # Set the position of the label
        self.app_label.place(x=200, y=15)

        # Create a label to display "Your"
        self.Your_label = tk.Label(self.HistoryScreen, text="Your", bg="black", fg="white", width="8", height="2", font=("Blinker", 20, "bold"))
        # Set the position of the label
        self.Your_label.place(x=25, y=85)

        # Create a label to display "Results"
        self.Results_label = tk.Label(self.HistoryScreen, text="Results", bg="black", fg="#FFDE59", width="10", height="2", font=("Blinker", 20, "bold"))
        # Set the position of the label
        self.Results_label.place(x=25, y=135)

        # Create a label to display message
        self.message_label = tk.Label(self.HistoryScreen, text="Previous results", bg="black", fg="#0CC0DF")
        # Set the position of the label
        self.message_label.place(x=60, y=200)

        # Create the button to Logout
        self.logout_button = tk.Button(self.HistoryScreen, text="Logout", bg="#0CC0DF", fg="white", height="2", width="11", cursor="hand2", command = self.Logout)
        # Set the position of the button
        self.logout_button.place(x=20, y=20)

        # switch to Input page message
        self.msgInptP_label = tk.Label(self.HistoryScreen, text="Input another result", bg="black", fg="#0CC0DF", width="20", height="1", font=("Blinker", 10, "bold"))
        # Set the position of the label
        self.msgInptP_label.place(x=30, y=440)

        # Create the button to input another sleep result
        self.logout_button = tk.Button(self.HistoryScreen, text="here", bg="#FFDE59", fg="#0CC0DF", height="1", width="10", cursor="hand2", command = self.input_another_result)
        # Set the position of the button
        self.logout_button.place(x=190, y=440)

        # Read username from "UserName.txt"
        with open(r"txt_Files\UserName.txt", "r") as username_file:
            # set username to to the text from txt file
            username = username_file.readline().strip()

        # Connect to the database
        conn = sqlite3.connect(r'DB\user_credentials.db')
        # connect cursor
        cursor = conn.cursor()

        # select all data from the table to check for existing data
        cursor.execute("SELECT * FROM UsersSleepData WHERE User_Name=?", (username,))
        # get the rows
        row = cursor.fetchone()
        # close database
        conn.close()

        # check each row, if null or not
        if row:
            # Check if the second column is NULL
            if row[1] is None:
                # display no data message when that cell is null (same for all other rows)
                hours1 = "Hours slept: No Sleep Data" 
                # Create a label for the message (same for all other rows)
                self.Hours_Slept1 = tk.Label(self.HistoryScreen, text = hours1, bg="black", fg="white", font=("Blinker", 8, "bold"))
                # Set the position of the label
                self.Hours_Slept1.place(x=55, y=240)
            else:
                # set the text to the data red from that cell (same for all other row)
                hours1 = "Hours slept: " + str(row[1])
                # Create a label for the message (same for all other rows)
                self.Hours_Slept1 = tk.Label(self.HistoryScreen, text = hours1, bg="black", fg="white", font=("Blinker", 8, "bold"))
                # Set the position of the label
                self.Hours_Slept1.place(x=55, y=240)

            # Check if the third column is NULL
            if row[2] is None:
                hours2 = "Hours slept: No Sleep Data"
                self.Hours_Slept2 = tk.Label(self.HistoryScreen, text = hours2, bg="black", fg="white", font=("Blinker", 8, "bold"))
                # Set the position of the label
                self.Hours_Slept2.place(x=55, y=270)
            else:
                hours2 = "Hours slept: " + str(row[2])
                self.Hours_Slept2 = tk.Label(self.HistoryScreen, text = hours2, bg="black", fg="white", font=("Blinker", 8, "bold"))
                # Set the position of the label
                self.Hours_Slept2.place(x=55, y=270)

            # Check if the fourth column is NULL
            if row[3] is None:
                hours3 = "Hours slept: No Sleep Data"
                self.Hours_Slept3 = tk.Label(self.HistoryScreen, text = hours3, bg="black", fg="white", font=("Blinker", 8, "bold"))
                # Set the position of the label
                self.Hours_Slept3.place(x=55, y=300)
            else:
                hours3 = "Hours slept: " + str(row[3])
                self.Hours_Slept3 = tk.Label(self.HistoryScreen, text = hours3, bg="black", fg="white", font=("Blinker", 8, "bold"))
                # Set the position of the label
                self.Hours_Slept3.place(x=55, y=300)

            # Check if the 5th column is NULL
            if row[4] is None:
                hours4 = "Hours slept: No Sleep Data"
                self.Hours_Slept4 = tk.Label(self.HistoryScreen, text = hours4, bg="black", fg="white", font=("Blinker", 8, "bold"))
                # Set the position of the label
                self.Hours_Slept4.place(x=55, y=330)
            else:
                hours4 = "Hours slept: " + str(row[4])
                self.Hours_Slept4 = tk.Label(self.HistoryScreen, text = hours4, bg="black", fg="white", font=("Blinker", 8, "bold"))
                # Set the position of the label
                self.Hours_Slept4.place(x=55, y=330)

            # Check if the 6th column is NULL
            if row[5] is None:
                hours5 = "Hours slept: No Sleep Data"
                self.Hours_Slept5 = tk.Label(self.HistoryScreen, text = hours5, bg="black", fg="white", font=("Blinker", 8, "bold"))
                # Set the position of the label
                self.Hours_Slept5.place(x=55, y=360)
            else:
                hours5 = "Hours slept: " + str(row[5])
                self.Hours_Slept5 = tk.Label(self.HistoryScreen, text = hours5, bg="black", fg="white", font=("Blinker", 8, "bold"))
                # Set the position of the label
                self.Hours_Slept5.place(x=55, y=360)

            # Check if the 7th column is NULL
            if row[6] is None:
                hours6 = "Hours slept: No Sleep Data"
                self.Hours_Slept6 = tk.Label(self.HistoryScreen, text = hours6, bg="black", fg="white", font=("Blinker", 8, "bold"))
                # Set the position of the label
                self.Hours_Slept6.place(x=55, y=390)
            else:
                hours6 = "Hours slept: " + str(row[6])
                self.Hours_Slept6 = tk.Label(self.HistoryScreen, text = hours6, bg="black", fg="white", font=("Blinker", 8, "bold"))
                # Set the position of the label
                self.Hours_Slept6.place(x=55, y=390)

            # Check if the 8th column is NULL
            if row[7] is None:
                hours7 = "Hours slept: No Sleep Data"
                self.Hours_Slept7 = tk.Label(self.HistoryScreen, text = hours7, bg="black", fg="white", font=("Blinker", 8, "bold"))
                # Set the position of the label
                self.Hours_Slept7.place(x=55, y=420)
            else:
                hours7 = "Hours slept: " + str(row[7])
                self.Hours_Slept7 = tk.Label(self.HistoryScreen, text = hours7, bg="black", fg="white", font=("Blinker", 8, "bold"))
                # Set the position of the label
                self.Hours_Slept7.place(x=55, y=420)
        else:
            # Display "No sleep Data entered this week" message
            self.no_data_label = tk.Label(self.HistoryScreen, text="No sleep Data entered this week", bg="black", fg="white", font=("Blinker", 8, "bold"))
            # Set the position of the label
            self.no_data_label.place(x=55, y=240)


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

    # function that will delete the data for a user when loging out, only when all the coloumns are filled
    def delete_user_if_all_data_exists(self):
        # Read username from "UserName.txt"
        with open(r"txt_Files\UserName.txt", "r") as username_file:
            username = username_file.readline().strip()

        # Connect to the database
        conn = sqlite3.connect(r'DB\user_credentials.db')
        # connect cursor
        cursor = conn.cursor()
        # Check if all Hours_Slept columns have data
        check_query = 'SELECT Hours_Slept1, Hours_Slept2, Hours_Slept3, Hours_Slept4, Hours_Slept5, Hours_Slept6, Hours_Slept7 FROM UsersSleepData WHERE User_Name = ?'
        # check for the username that is logged in
        cursor.execute(check_query, (username,))
        # set the hours data to the data of the user
        hours_data = cursor.fetchone()

        # check if every cell is is filled
        if hours_data is not None and all(hours_data):
            # All Hours_Slept columns have data, delete the user's data
            delete_query = 'DELETE FROM UsersSleepData WHERE User_Name = ?'
            cursor.execute(delete_query, (username,))
            conn.commit()
        else:
            # do nothing if there are still empty Hours_Slept coloumbs 
            pass
        
        # close database
        conn.close()

    # function to switch to input page
    def input_another_result(self):
        # check if all cells are empty
        self.delete_user_if_all_data_exists()
        # clear the hours txt file
        self.clearHoursTXT()
        # Open the SG_Version1\SleepData_Input.py file using subprocess
        subprocess.Popen(["python", "SG_Version1\SleepData_Input.py"])
        # Close the HistoryScreen screen
        self.HistoryScreen.destroy()

    # function to logout
    def Logout(self):
        # check if all cells are empty
        self.delete_user_if_all_data_exists()
        # clear the data from hours txt file
        self.clearHoursTXT()
        # clear the data from username txt file
        self.clearUNameTXT()
        # Open the SG_Version1\landing.py file using subprocess
        subprocess.Popen(["python", "SG_Version1\landing.py"])
        # Close the HistoryScreen screen
        self.HistoryScreen.destroy()

    def run(self):
        # This line starts the event loop and keeps the application running.
        self.HistoryScreen.mainloop()

if __name__ == "__main__":
    # Create an instance of the LandingPage class
    History_Results = HistoryResults()
    # Start the Tkinter main event loop by calling the run() method.
    # This line will keep the application responsive to user interactions.
    History_Results.run()