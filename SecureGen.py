import tkinter as tk
import random
import string
import pyperclip  # Make sure pyperclip is installed with pip install pyperclip in console
from tkinter import PhotoImage
import os
script_dir = os.path.dirname(os.path.realpath(__file__))
# Define the directory containing images
image_dir = os.path.join(script_dir, "images")

# Function to generate a password
def generate_password():
    # Get the input password length
    password_length_str = length_var.get()

    # Check if the input is a valid number and if it's within the specified range
    if password_length_str.isdigit():
        password_length = int(password_length_str)
        if 12 <= password_length <= 20:
            password_complexity = complexity_var.get()
            if password_complexity == "Alphanumeric":
                characters = string.ascii_letters + string.digits
            else:
                characters = string.ascii_letters + string.digits + string.punctuation

            password = ''.join(random.choice(characters) for _ in range(password_length))
            password_var.set(password)
            pass
        else:
            error_message_var.set("Password length must be between 12 and 20")
            show_error_message()
    else:
        error_message_var.set("Please enter a valid number")
        show_error_message()

    # Change the background color to a random color
    window.configure(bg=random_color())

#Input validation as an error message
def show_error_message():
        error_window = tk.Toplevel(window)
        error_window.title("Error Message")
        error_label = tk.Label(error_window, textvariable=error_message_var)
        error_label.pack()
    # Function to open a separate window for the generated password
def show_password():
        top = tk.Toplevel(window)
        top.title("Generated Password")
        password_label = tk.Label(top, text="Generated Password:")
        password_display = tk.Entry(top, textvariable=password_var, state="readonly")
        password_label.grid(row=0, padx=10, pady=5)
        password_display.grid(row=1, padx=10, pady=5)


# Function to copy the password to the clipboard
def copy_to_clipboard():
    password = password_var.get()
    pyperclip.copy(password)


# Function to generate a random background color
def random_color():
    return "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


# Create the main window
window = tk.Tk()
window.title("SecureGen Password")

#Set application icons
script_dir = os.path.dirname(os.path.realpath(__file__))
# Define the directory containing your icons
icon_dir = os.path.join(script_dir, "icons")

# Construct path to icons
icon_path = os.path.join(icon_dir, "icon.ico")

# Set the application icon
window.iconbitmap(icon_path)

# Load the taskbar icon
taskbar_icon_path = os.path.join(icon_dir, "Padlock.gif")
taskbar_icon = PhotoImage(file=taskbar_icon_path)

# Create and set variables
length_var = tk.StringVar()
complexity_var = tk.StringVar()
password_var = tk.StringVar()
error_message_var = tk.StringVar()

#Set images
key_image_path = os.path.join(image_dir, "key.gif")
padlock_image_path = os.path.join(image_dir, "padlock.gif")
key_image = PhotoImage(file=key_image_path)
padlock_image = PhotoImage(file=padlock_image_path)
key_image = key_image.subsample(3)
padlock_image = padlock_image.subsample(3)

# Create widgets
length_label = tk.Label(window, text="Password Length (12-20):")
length_entry = tk.Entry(window, textvariable=length_var)
complexity_label = tk.Label(window, text="Password Complexity:")
complexity_options = ["Alphanumeric", "Alphanumeric + Special"]
complexity_menu = tk.OptionMenu(window, complexity_var, *complexity_options)
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
password_label = tk.Label(window, text="Generated Password:")
password_display = tk.Entry(window, textvariable=password_var, state="readonly")
copy_button = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard)
key_label = tk.Label(window, image=key_image)
padlock_label = tk.Label(window, image=padlock_image)
show_password_button = tk.Button(window, text="Show Password", command=show_password)
error_label = tk.Label(window, textvariable=error_message_var, fg="red")




# Grid layout
length_label.grid(row=0, column=0, padx=10, pady=5)
length_entry.grid(row=0, column=1, padx=10, pady=5)
complexity_label.grid(row=1, column=0, padx=10, pady=5)
complexity_menu.grid(row=1, column=1, padx=10, pady=5)
key_label.grid(row=1, column=2, padx=10, pady=5)
generate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
password_label.grid(row=3, column=0, padx=10, pady=5)
password_display.grid(row=3, column=1, padx=10, pady=5)
padlock_label.grid(row=3, column=2, padx=10, pady=5)
copy_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
show_password_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Initialize background color
window.configure(bg=random_color())

# Start the GUI main loop
window.mainloop()
