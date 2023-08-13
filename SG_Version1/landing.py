# import modules
import tkinter as tk
import subprocess
from tkinter import *
from PIL import Image, ImageTk


# Define a class for the Landing page
class LandingPage:
    def __init__(self):
        # Create the main application window
        self.main_screen = tk.Tk()
        # Set the window size to 350x500 pixels
        self.main_screen.geometry("350x500")
        # Set the window title
        self.main_screen.title("Landing Page")
        # Set the background color to black
        self.main_screen.configure(bg="black")

        # Load and display the image
        # open image 
        self.image = Image.open("assets\LogoY13.png") 
        # Resize the image to 100x100 pixels
        self.image = self.image.resize((100, 100)) 
        # Convert the image to a format compatible with Tkinter
        self.image_tk = ImageTk.PhotoImage(self.image)
        # Create a label to display the image
        self.image_label = tk.Label(self.main_screen, image=self.image_tk, bg="black")
        # Set the position of the image label
        self.image_label.place(x=160, y=10)

        # Create a label to display the app name
        self.app_label = tk.Label(self.main_screen, text="Sleep \n Genius", bg="black", fg="#FFDE59", width="6", height="2", font=("Blinker", 20, "bold"))
        # Set the position of the label
        self.app_label.place(x=75, y=25)

        # Create a label to display the Hi message
        self.hi_label = tk.Label(self.main_screen, text="Hi!", bg="black", fg="white", width="15", height="2", font=("Blinker", 20, "bold"))
        # Set the position of the label
        self.hi_label.place(x=0, y=130)

        # Create label to display the welcome message
        self.welcome_label = tk.Label(self.main_screen, text="Welcome", bg="black", fg="#FFDE59", width="20", height="2", font=("Blinker", 20, "bold"))
        # Set the position of the label
        self.welcome_label.place(x=0, y=180)

        # Create the login button
        self.login_button = tk.Button(self.main_screen, text="Login", bg="#0CC0DF", fg="white", height="2", width="30", cursor="hand2", command=self.open_login_page)
        # Set the position of the login button
        self.login_button.place(x=60, y=275)

        # Create the register button
        self.register_button = tk.Button(self.main_screen, text="Register", bg="#0CC0DF", fg="white", height="2", width="30", cursor="hand2", command=self.open_register_page)
        # Set the position of the register button
        self.register_button.place(x=60, y=325)

    # function to open login page
    def open_login_page(self):
        # Open the SG_Version1\Login_Page.py file using subprocess
        subprocess.Popen(["python", "SG_Version1\Login_Page.py"])
        # Close the main screen
        self.main_screen.destroy()

    # function to open register page
    def open_register_page(self):
        # Open the SG_Version1\Login_Page.py file using subprocess
        subprocess.Popen(["python", "SG_Version1\Login_Page.py"])
        # Close the main screen
        self.main_screen.destroy()

    def run(self):
        # This line starts the event loop and keeps the application running.
        self.main_screen.mainloop()

if __name__ == "__main__":
    # Create an instance of the LandingPage class
    landing_page = LandingPage()
    # Start the Tkinter main event loop by calling the run() method.
    # This line will keep the application responsive to user interactions.
    landing_page.run()


