#import modules
import tkinter as tk
from tkinter import messagebox
import subprocess
import os
from tkinter import *
from PIL import Image, ImageTk
import sqlite3
import re


# Define a class for the registration page
class RegisterPage:
    def __init__(self):
        # Create the main application window
        self.registration_screen = tk.Tk()
        # Set the window title
        self.registration_screen.title("Registration")
        # Set the window size to 350x500 pixels
        self.registration_screen.geometry("350x500")
        # Set the background color to black
        self.registration_screen.configure(bg="black")

        # Load and display the image
        # open image
        self.image = Image.open("Assets\LogoY13.png")
        # Resize the image to 75x75 pixels
        self.image = self.image.resize((75, 75))
        # Convert the image to a format compatible with Tkinter
        self.image_tk = ImageTk.PhotoImage(self.image) 
        # Create a label to display the image
        image_label = tk.Label(self.registration_screen, image=self.image_tk, bg="black")
        # Set the position of the image label
        image_label.place(x=275, y=5)  

        # Create a label to display the app name
        self.app_label = tk.Label(self.registration_screen, text="Sleep \n Genius", bg="black", fg="#FFDE59", width="6", height="2", font=("Blinker", 15, "bold"))
        # Set the position of the label
        self.app_label.place(x=200, y=15)

        # Create a label to display Hi
        self.hi_label = tk.Label(self.registration_screen, text="Hi!", bg="black", fg="white", width="5", height="2", font=("Blinker", 20, "bold"))
        # Set the position of the label
        self.hi_label.place(x=25, y=110)

        # Create a label to display the welcome message
        self.welcome_label = tk.Label(self.registration_screen, text="Welcome", bg="black", fg="#FFDE59", width="10", height="2", font=("Blinker", 20, "bold"))
        # Set the position of the label
        self.welcome_label.place(x=25, y=160)
        
        # Create a label to display the message
        self.message_label = tk.Label(self.registration_screen, text="Please enter details below to register", bg="black", fg="#0CC0DF")
        # Set the position of the label
        self.message_label.place(x=50, y=230)
       
        # Holds the value entered in the username entry field
        self.username_verify = tk.StringVar()
        # Holds the value entered in the password entry field
        self.password_verify = tk.StringVar()

        # Create a label to display username*
        self.usernme_label = tk.Label(self.registration_screen, text="Username * ", bg="black", fg="white")
        # Set the position of the label
        self.usernme_label.place(x=50, y=285)
        # Create an Entry widget
        self.username_register_entry = tk.Entry(self.registration_screen, textvariable=self.username_verify)
        # Set the position of the label
        self.username_register_entry.place(x=160, y=285)

        # Create a label to display password*
        self.password_label = tk.Label(self.registration_screen, text="Password * ", bg="black", fg="white")
        # Set the position of the label
        self.password_label.place(x=50, y=315)
        # Create an Entry widget
        self.password_register_entry = tk.Entry(self.registration_screen, textvariable=self.password_verify, show='*')
        # Set the position of the label
        self.password_register_entry.place(x=160, y=315)

        # Create register button
        self.register_button = tk.Button(self.registration_screen, text="Register", bg="#0CC0DF", fg="white", height="2", width="30", cursor="hand2", command=self.register_user)
        # Set the position of the button
        self.register_button.place(x=50, y=365)

        # switch to login page message
        self.question_label = tk.Label(self.registration_screen, text="Have an account?", bg="black", fg="#0CC0DF", width="20", height="1", font=("Blinker", 10, "bold"))
        # Set the position of the label
        self.question_label.place(x=30, y=440)

        # Create the button to switch to login page
        self.login_button = tk.Button(self.registration_screen, text="Login", bg="#FFDE59", fg="#0CC0DF", height="1", width="10", cursor="hand2", command=self.open_login_page)
        # Set the position of the button
        self.login_button.place(x=190, y=440)

    
    # function to register
    def register_user(self):
        # set username to the username input
        username = self.username_register_entry.get()
        # set password to the password input
        password = self.password_register_entry.get()

        # Connect to the database or create a new one if it doesn't exist
        conn = sqlite3.connect(r'DB\user_credentials.db')

        # Create a table to store user credentials if it doesn't exist
        table_create_query = '''CREATE TABLE IF NOT EXISTS UsersLogin
                (User_Name TEXT, Password TEXT)
        '''
        # execute the query
        conn.execute(table_create_query)

        # Check if the username alredy has a table with previous results 
        check_query = 'SELECT User_Name FROM UsersLogin WHERE User_Name = ?'
        # connect cursor
        cursor = conn.cursor()
        # compare the username entered by the user
        cursor.execute(check_query, (username,))
        # username that exists
        existing_user = cursor.fetchone()

        # Check if the username is longer than 15 characters
        if len(username) > 15:
            # message box desplays erorr 
            messagebox.showerror('Registration', 'Username cannot be more than 15 characters!')
            return
        
        # Check if the password is longer than 20 characters
        if len(password) > 20:
            # message box desplays erorr 
            messagebox.showerror('Registration', 'Username cannot be more than 20 characters!')
            return

        # Validate the username to allow only letters
        if not re.match("^[a-zA-Z]+$", username):
            # Show an error message if the username contains non-letter characters
            messagebox.showerror('Registration', 'Username should only contain letters!')
            return

        # Validate the password to contain a capital letter and a number
        if not (re.search(r"[A-Z]", password) and re.search(r"\d", password)):
            # Show an error message if the password doesn't meet the criteria
            messagebox.showerror('Registration', 'Password must contain a capital letter and a number!')
            return

        # Validate the password to not contain spaces
        if ' ' in password:
            # Show an error message if the password contains spaces
            messagebox.showerror('Registration', 'Password cannot contain spaces!')
            conn.close()
            return

        # Validate the password to contain at least 8 characters
        if len(password) < 8:
            # Show an error message if the password is too short
            messagebox.showerror('Registration', 'Password must contain at least 8 characters!')
            conn.close()
            return

        # check if the username user entered is taken
        if existing_user:
            # Show an error message if the username already exists
            messagebox.showerror('Registration', 'Username already exists!')
        else:
            # Insert the new user into the database
            insert_query = 'INSERT INTO UsersLogin (User_Name, Password) VALUES (?, ?)'
            insert_data = (username, password)
            cursor.execute(insert_query, insert_data)
            conn.commit()
            # Show a success message
            messagebox.showinfo('Registration', 'Registration successful!')
            self.open_login_page()

        # Close the database connection
        conn.close()

    # function to switch to login page
    def open_login_page(self):
        # Open the SG_Version2\Login_PageV2.py file using subprocess
        subprocess.Popen(["python", "SG_Version2\Login_PageV2.py"])
        # Close the main screen
        self.registration_screen.destroy()

    def run(self):
        # This line starts the event loop and keeps the application running.
        self.registration_screen.mainloop()


if __name__ == "__main__":
    # Create an instance of the RegisterPage class
    register_page = RegisterPage()
    # Start the Tkinter main event loop by calling the run() method.
    # This line will keep the application responsive to user interactions.
    register_page.run()