# import modules
import tkinter as tk
import subprocess
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import random


# Define a class for the result page
class ResultPage:
    def __init__(self):
        # Create the main application window
        self.Result_screen = tk.Tk()
        # Set the window title
        self.Result_screen.title("Result page")
        # Set the window size to 350x500 pixels
        self.Result_screen.geometry("350x500")
        # Set the background color to black
        self.Result_screen.configure(bg="black")

        # Load and display the image
        # open image
        self.image = Image.open("Assets\\LogoY13.png")
        # Resize the image to 75x75 pixels
        self.image = self.image.resize((75, 75))
        # Convert the image to a format compatible with Tkinter
        self.image_tk = ImageTk.PhotoImage(self.image)
        # Create a label to display the image
        self.image_label = tk.Label(
            self.Result_screen,
            image=self.image_tk,
            bg="black")
        # Set the position of the image label
        self.image_label.place(x=275, y=5)

        # Create a label to display the app name
        self.app_label = tk.Label(
            self.Result_screen,
            text="Sleep \n Genius",
            bg="black",
            fg="#FFDE59",
            width="6",
            height="2",
            font=(
                "Blinker",
                15,
                "bold"))
        # Set the position of the label
        self.app_label.place(x=200, y=15)

        # Create a label to display the thanks message
        self.Thanks_label = tk.Label(
            self.Result_screen,
            text="Thanks!",
            bg="black",
            fg="white",
            width="10",
            height="2",
            font=(
                "Blinker",
                20,
                "bold"))
        # Set the position of the label
        self.Thanks_label.place(x=20, y=75)

        # Create a label to display the result message
        self.ResultMessage_label = tk.Label(
            self.Result_screen,
            text="Here's your result",
            bg="black",
            fg="#FFDE59",
            width="20",
            height="2",
            font=(
                "Blinker",
                20,
                "bold"))
        # Set the position of the label
        self.ResultMessage_label.place(x=0, y=125)

        # Create a label to display the result message
        self.message_label = tk.Label(
            self.Result_screen,
            text="This is your sleep result",
            bg="black",
            fg="#0CC0DF")
        # Set the position of the label
        self.message_label.place(x=55, y=185)

        # Create a label to tell user to press the button for suggestion
        self.suggestion_label = tk.Label(
            self.Result_screen,
            text="Press for a sleep suggestion",
            bg="black",
            fg="#FFDE59",
            font=(
                "Blinker",
                10,
                "bold"))
        # Set the position of the label
        self.suggestion_label.place(x=70, y=335)

        # Create submit button
        self.submit_button = tk.Button(
            self.Result_screen,
            text="Sleep Suggestion",
            bg="#0CC0DF",
            fg="white",
            height="2",
            width="30",
            cursor="hand2",
            command=self.get_random_tip)
        # Set the position of the button
        self.submit_button.place(x=50, y=360)

        # switch to History page message
        self.msgHistP_label = tk.Label(
            self.Result_screen,
            text="View previous result",
            bg="black",
            fg="#0CC0DF",
            width="20",
            height="1",
            font=(
                "Blinker",
                10,
                "bold"))
        # Set the position of the label
        self.msgHistP_label.place(x=30, y=440)

        # Create the button to switch to History page
        self.switchHisP_button = tk.Button(
            self.Result_screen,
            text="Here",
            bg="#FFDE59",
            fg="#0CC0DF",
            height="1",
            width="10",
            cursor="hand2",
            command=self.open_History_page)
        # Set the position of the button
        self.switchHisP_button.place(x=190, y=440)

        # Create the button to Logout
        self.logout_button = tk.Button(
            self.Result_screen,
            text="Logout",
            bg="#0CC0DF",
            fg="white",
            height="2",
            width="11",
            cursor="hand2",
            command=self.Logout)
        # Set the position of the button
        self.logout_button.place(x=20, y=20)

        # Read username from "UserName.txt"
        with open(r"txt_Files\UserName.txt", "r") as username_file:
            username = username_file.readline().strip()

        # Read hours from "HourInput.txt"
        with open("txt_Files\\HourInput.txt", "r") as hours_file:
            hours_slept = hours_file.readline().strip()
            hours_slept = float(hours_slept)  # Convert to float

        reference_hours = "8"
        reference_hours = float(reference_hours)

        if hours_slept > reference_hours:
            result_text = (f"{username}, You slept {hours_slept} hours,\n"
                           f"which is more than the recommended "
                           f"{reference_hours} hours.")
        elif hours_slept < reference_hours:
            result_text = (f"{username}, You slept {hours_slept} hours, \n"
                           f"which is less than the recommended "
                           f"{reference_hours} hours.")
        else:
<<<<<<< HEAD
            result_text = (f"{username}, You slept {hours_slept} \n"
                           f"which is the recommended amount of sleep.")
=======
            result_text = f"{username}, You slept {hours_slept} \nwhich is the recommended amount of sleep."
>>>>>>> 880fd0e739566e2e44283fb0ef26c45c074fffd9

        # display the result
        result_label = tk.Label(
            self.Result_screen,
            text=result_text,
            anchor="w",
            justify="left",
            bg="black",
            fg="white",
            font=(
                "Blinker",
                8,
                "bold"))
        result_label.place(x=55, y=210)

    # open the data base and insert values into the table
    def make_suggestions(self):
        conn = sqlite3.connect(r'DB\user_credentials.db')
        cursor = conn.cursor()

        # Create a table to store the sleep tips
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Sleep_Suggestions (
            SuggestionID INTEGER PRIMARY KEY,
            Suggestions TEXT
        )
        """)

        # Define the list of sleep tips
        sleep_tips = [
            (1, 'Go to bed at the same time each night and get up '
                'at the same time each morning'),
            (2, 'Make sure your bedroom is quiet, dark and relaxing'),
            (3, 'Recommended room temperature is 16 to 20 degrees '
                'Celsius when going to sleep'),
            (4, 'Do not consume caffeine late in the day'),
            (5, 'Take a relaxing bath or shower')
        ]

        # Insert the sleep tips into the database
        cursor.executemany(
<<<<<<< HEAD
            """
            INSERT INTO Sleep_Suggestions (SuggestionID, Suggestions)
            VALUES (?, ?)
            """,
=======
            "INSERT INTO Sleep_Suggestions (SuggestionID, Suggestions) VALUES (?, ?)",
>>>>>>> 880fd0e739566e2e44283fb0ef26c45c074fffd9
            sleep_tips)

        # Commit the changes and close the connection
        conn.commit()

        conn.close()

    # function to suggest a random suggestion
    def get_random_tip(self):
        # Connect to the database
        conn = sqlite3.connect(r'DB\user_credentials.db')
        cursor = conn.cursor()

        # Get the total number of rows in the table
        cursor.execute("SELECT COUNT(*) FROM Sleep_Suggestions")
        total_rows = cursor.fetchone()[0]

        # Generate a list of all Suggestions IDs
        Suggestions_ids = list(range(1, total_rows + 1))

        # Shuffle the list of Suggestions IDs
        random.shuffle(Suggestions_ids)

        # Retrieve the Suggestions associated with the first ID in the shuffled
        # list
        random_Suggestion_id = Suggestions_ids[0]
        cursor.execute(
            "SELECT Suggestions FROM Sleep_Suggestions WHERE SuggestionID = ?",
            (random_Suggestion_id,
             ))
        random_Suggestion = cursor.fetchone()[0]

        # Close the connection
        conn.close()

        # Show the random tip in a message box
        messagebox.showinfo("Sleep Suggestion", random_Suggestion)

    # function that saves the data of the user into a DB

    def SaveInDB(self):
        # Read name from "UserName.txt"
        with open(r"txt_Files\UserName.txt", "r") as username_file:
            username = username_file.readline().strip()

        # Read hours from "HourInput.txt"
        with open("txt_Files\\HourInput.txt", "r") as hours_file:
            hours_slept = hours_file.readline().strip()
            hours_slept = float(hours_slept)  # Convert to float

        # Connect to the database
        conn = sqlite3.connect(r'DB\user_credentials.db')
        cursor = conn.cursor()

        # Create a table to store user credentials if it doesn't exist
        table_create_query = '''CREATE TABLE IF NOT EXISTS UsersSleepData
                (User_Name TEXT, Hours_Slept1 TEXT, Hours_Slept2 TEXT,
                Hours_Slept3 TEXT, Hours_Slept4 TEXT,
                  Hours_Slept5 TEXT, Hours_Slept6 TEXT, Hours_Slept7 TEXT)
        '''
        conn.execute(table_create_query)

        # Check if the username already exists
        check_query = """
        SELECT User_Name
        FROM UsersSleepData
        WHERE User_Name = ?
        """
        cursor.execute(check_query, (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            # Check if any of the Hours_Slept columns already exist
            check_query = """
            SELECT Hours_Slept1, Hours_Slept2, Hours_Slept3,
            Hours_Slept4, Hours_Slept5, Hours_Slept6, Hours_Slept7
            FROM UsersSleepData WHERE User_Name = ?
            """
            cursor.execute(check_query, (username,))
            hours_data = cursor.fetchone()

            if hours_data is not None:
                # Find the first empty Hours_Slept column
                for i, hours in enumerate(hours_data):
                    if hours is None:
                        update_query = f'UPDATE UsersSleepData SET '
                        f'Hours_Slept{i + 1} = ? WHERE User_Name = ?'
                        update_data = (hours_slept, username)
                        cursor.execute(update_query, update_data)
                        conn.commit()
                        break
            else:
                # No data for the user, insert in the first column
                insert_query = """
                INSERT INTO UsersSleepData
                (User_Name, Hours_Slept1) VALUES (?, ?)
                """
                insert_data = (username, hours_slept)
                cursor.execute(insert_query, insert_data)
                conn.commit()
        else:
            # User does not exist, create a new row with the data
            insert_query = """
            INSERT INTO UsersSleepData
            (User_Name, Hours_Slept1) VALUES (?, ?)
            """
            insert_data = (username, hours_slept)
            cursor.execute(insert_query, insert_data)
            conn.commit()

        # Close the database connection
        conn.close()

    # function that will clear the text file, used when loging out and when
    # switching a file thats a step back

    def clearHoursTXT(self):
        # open the txt file in write mode
        with open("txt_Files\\HourInput.txt", "w") as hoursSlept_file:
            # truncating the file to a size of 0 bytes, which effectively
            # deletes the contents of the file
            hoursSlept_file.truncate(0)

    # function that will clear the text file, used when loging out and when
    # switching a file thats a step back
    def clearUNameTXT(self):
        # open the txt file in write mode
        with open(r"txt_Files\UserName.txt", "w") as username_file:
            # truncating the file to a size of 0 bytes, which effectively
            # deletes the contents of the file
            username_file.truncate(0)

    # function that will delete the data for a user when loging out, only when
    # all the coloumns are filled
    def delete_user_if_all_data_exists(self):
        # Read username from "UserName.txt"
        with open(r"txt_Files\UserName.txt", "r") as username_file:
            username = username_file.readline().strip()

        # Connect to the database
        conn = sqlite3.connect(r'DB\user_credentials.db')
        cursor = conn.cursor()
        # Check if all Hours_Slept columns have data
        check_query = """
        SELECT Hours_Slept1, Hours_Slept2, Hours_Slept3,
        Hours_Slept4, Hours_Slept5, Hours_Slept6, Hours_Slept7
        FROM UsersSleepData WHERE User_Name = ?
        """
        cursor.execute(check_query, (username,))
        hours_data = cursor.fetchone()

        if hours_data is not None and all(hours_data):
            # Convert to float and filter out invalid values
            valid_hours_data = [
                float(value) for value in hours_data if isinstance(
                    value, (int, float, str)) and value.strip()]

            # Calculate average sleep
            average_sleep = sum(valid_hours_data) / len(valid_hours_data)

            # Show a message box with the average sleep
            messagebox.showinfo(
                "Average Sleep",
<<<<<<< HEAD
                f"Your average sleep for this week was: "
                f"{average_sleep:.2f} hours")
=======
                f"Your average sleep for this week was: {average_sleep:.2f} hours")
>>>>>>> 880fd0e739566e2e44283fb0ef26c45c074fffd9

            # All Hours_Slept columns have data, delete the user's data
            delete_query = 'DELETE FROM UsersSleepData WHERE User_Name = ?'
            cursor.execute(delete_query, (username,))
            conn.commit()
        else:
            # do nothing if there are still empty Hours_Slept coloumbs
            pass

        # close database
        conn.close()

    # open the history page and does the SaveInDB function

    def open_History_page(self):
        self.SaveInDB()
        # Open the SG_Version4\History_ResultsV4.py file using subprocess
        subprocess.Popen(["python", "SG_Version4\\History_ResultsV4.py"])
        # Close the main screen
        self.Result_screen.destroy()

    # function to log out
    def Logout(self):
        # save data in db
        self.SaveInDB()
        # check if all cells are filled in
        self.delete_user_if_all_data_exists()
        # delete data from hours txt
        self.clearHoursTXT()
        # delete data from username txt
        self.clearUNameTXT()
        # Open the SG_Version4\landingV4.py file using subprocess
        subprocess.Popen(["python", "SG_Version4\\landingV4.py"])
        # Close the main screen
        self.Result_screen.destroy()

    def run(self):
        # This line starts the event loop and keeps the application running.
        self.Result_screen.mainloop()


if __name__ == "__main__":
    # Create an instance of the ResultPage class
    result_page = ResultPage()
    # Start the Tkinter main event loop by calling the run() method.
    # This line will keep the application responsive to user interactions.
    result_page.run()
