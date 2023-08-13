#import modules
import tkinter as tk
import subprocess
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3


# Define a class for the login page
class LoginPage:
    def __init__(self):
        # Create the main application window
        self.login_screen = tk.Tk()
        # Set the window title
        self.login_screen.title("Login")
        # Set the window size to 350x500 pixels
        self.login_screen.geometry("350x500")
        # Set the background color to black
        self.login_screen.configure(bg="black")

        # Load and display the image
        # open image 
        self.image = Image.open("Assets\LogoY13.png")
        # Resize the image to 75x75 pixels
        self.image = self.image.resize((75, 75))
        # Convert the image to a format compatible with Tkinter
        self.image_tk = ImageTk.PhotoImage(self.image)
        # Create a label to display the image
        self.image_label = tk.Label(self.login_screen, image=self.image_tk, bg="black")
        # Set the position of the image label
        self.image_label.place(x=275, y=5)  

        # Create a label to display the app name
        self.app_label = tk.Label(self.login_screen, text="Sleep \n Genius", bg="black", fg="#FFDE59", width="6", height="2", font=("Blinker", 15, "bold"))
        # Set the position of the label
        self.app_label.place(x=200, y=15)

        # Create a label to display the Hi message
        self.hi_label = tk.Label(self.login_screen, text="Hi!", bg="black", fg="white", width="5", height="2", font=("Blinker", 20, "bold"))
        # Set the position of the label
        self.hi_label.place(x=25, y=100)
        
        # Create a label to display the welcome message
        self.welcome_label = tk.Label(self.login_screen, text="Welcome", bg="black", fg="#FFDE59", width="10", height="2", font=("Blinker", 20, "bold"))
        # Set the position of the label
        self.welcome_label.place(x=25, y=150)
        
        # Create a label to display the direction message
        self.message_label = tk.Label(self.login_screen, text="Please enter details below to login", bg="black", fg="#0CC0DF")
        # Set the position of the label
        self.message_label.place(x=50, y=220)
       
        # Create StringVar to hold the value of the username entered
        self.username_verify = tk.StringVar()
        # Create StringVar to hold the value of the password entered
        self.password_verify = tk.StringVar()

        # Create a label to display username message
        self.usernme_label = tk.Label(self.login_screen, text="Username * ", bg="black", fg="white")
        # Set the position of the label
        self.usernme_label.place(x=50, y=280)
        # Create a label where username is entered
        self.username_login_entry = tk.Entry(self.login_screen, textvariable=self.username_verify)
        # Set the position of the label
        self.username_login_entry.place(x=160, y=280)

        # Create a label to display password message
        self.usernme_label = tk.Label(self.login_screen, text="Password * ", bg="black", fg="white")
        # Set the position of the label
        self.usernme_label.place(x=50, y=310)
        # Create a label where password is entered
        self.password_login_entry = tk.Entry(self.login_screen, textvariable=self.password_verify, show='*')
        # Set the position of the label
        self.password_login_entry.place(x=160, y=310)

        # Create login button
        self.login_button = tk.Button(self.login_screen, text="Login", bg="#0CC0DF", fg="white", height="2", width="30", cursor="hand2", command=self.login)
        # Set the position of the button
        self.login_button.place(x=50, y=360)

        # Create a label for direction message
        self.question_label = tk.Label(self.login_screen, text="Don't have an account?", bg="black", fg="#0CC0DF", width="20", height="1", font=("Blinker", 10, "bold"))
        # Set the position of the label
        self.question_label.place(x=35, y=435)

        # Create the button to switch to register page
        self.register_button = tk.Button(self.login_screen, text="Register", bg="#FFDE59", fg="#0CC0DF", height="1", width="10", cursor="hand2", command = self.open_register_page)
        # Set the position of the button
        self.register_button.place(x=200, y=435)

    # function to login 
    def login(self):
        # set username to the username input
        username = self.username_login_entry.get()
        # set password to the password input
        password = self.password_login_entry.get()

        # Connect to the database
        conn = sqlite3.connect(r'DB\user_credentials.db')
        # select all data from data base to find the user loging in
        query = 'SELECT * FROM UsersLogin WHERE User_Name = ? AND Password = ?'
        # connect cursor
        cursor = conn.cursor()
        # look for the data in the data base, that matches the username and password
        cursor.execute(query, (username, password))
        # set user to the username that logged in
        user = cursor.fetchone()

        # if there was a match in username and password
        if user:
            # Show a message box that says login successful
            messagebox.showinfo('Login', 'Login successful!')
            
            # open the username text file in write mode
            with open(r"txt_Files\UserName.txt", "w") as file:
                # record the username that has logged in
                file.write(f"{username}")
            
            # open the input page 
            self.open_input_page()

        # if there wasn't
        else:
            # show message box that tells the user that something was wrong
            messagebox.showerror('Login', 'Invalid username or password!')
        
        # close database
        conn.close()

    # function that opens register page
    def open_register_page(self):
        # Open the SG_Version1\Register_Page.py file using subprocess
        subprocess.Popen(["python", "SG_Version1\Register_Page.py"])
        # Close the logi  screen
        self.login_screen.destroy()

    # function that opens input page
    def open_input_page(self):
        # Open the SG_Version1\SleepData_Input.py file using subprocess
        subprocess.Popen(["python", "SG_Version1\SleepData_Input.py"])
        # Close the login screen
        self.login_screen.destroy()

    def run(self):
        # This line starts the event loop and keeps the application running.
        self.login_screen.mainloop()


if __name__ == "__main__":
    # Create an instance of the LoginPage class
    login_page = LoginPage()
    # Start the Tkinter main event loop by calling the run() method.
    # This line will keep the application responsive to user interactions.
    login_page.run()