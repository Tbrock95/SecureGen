import tkinter as tk
import random
import string
import pyperclip  # Make sure pyperclip is installed by running 'pip install pyperclip' in python console


# Function to generate a password
def generate_password():
    password_length = int(length_var.get())
    password_complexity = complexity_var.get()

    if password_complexity == "Alphanumeric":
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_var.set(password)
    # Change the background color to a random color
    window.configure(bg=random_color())


# Function to copy the password to the clipboard
def copy_to_clipboard():
    password = password_var.get()
    pyperclip.copy(password)


# Function to generate a random background color
def random_color():
    return "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


# Create the main window
window = tk.Tk()
window.title("SecureGen Password Generator")

# Create and set variables
length_var = tk.StringVar()
complexity_var = tk.StringVar()
password_var = tk.StringVar()

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

# Grid layout
length_label.grid(row=0, column=0, padx=10, pady=5)
length_entry.grid(row=0, column=1, padx=10, pady=5)
complexity_label.grid(row=1, column=0, padx=10, pady=5)
complexity_menu.grid(row=1, column=1, padx=10, pady=5)
generate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
password_label.grid(row=3, column=0, padx=10, pady=5)
password_display.grid(row=3, column=1, padx=10, pady=5)
copy_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Initialize background color
window.configure(bg=random_color())

# Start the GUI main loop
window.mainloop()
