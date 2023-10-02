import tkinter as tk
import secrets
import string
import pyperclip

def generate_password(length, include_digits, include_special_chars):
    characters = string.ascii_letters
    
    if include_digits:
        characters += string.digits
    
    if include_special_chars:
        characters += string.punctuation
    
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def copy_to_clipboard(password):
    pyperclip.copy(password)

def generate_and_copy_password():
    password_length = int(length_var.get())
    include_digits = include_digits_var.get()
    include_special_chars = include_special_chars_var.get()
    
    password = generate_password(password_length, include_digits, include_special_chars)
    password_var.set(password)
    
    copy_to_clipboard(password)

def main():
    root = tk.Tk()
    root.title("Random Password Generator")

    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    # Password Length
    length_label = tk.Label(frame, text="Number of Characters (12-20):")
    length_label.pack()
    length_var = tk.StringVar(value="12")
    length_entry = tk.Entry(frame, textvariable=length_var)
    length_entry.pack()

    # Include Digits
    include_digits_var = tk.BooleanVar()
    include_digits_checkbox = tk.Checkbutton(frame, text="Include Digits (0-9)", variable=include_digits_var)
    include_digits_checkbox.pack()

    # Include Special Characters
    include_special_chars_var = tk.BooleanVar()
    include_special_chars_checkbox = tk.Checkbutton(frame, text="Include Special Characters", variable=include_special_chars_var)
    include_special_chars_checkbox.pack()

    # Generate and Copy Password Button
    generate_button = tk.Button(frame, text="Generate and Copy Password", command=generate_and_copy_password)
    generate_button.pack()

    # Display Password
    password_var = tk.StringVar()
    password_label = tk.Label(frame, textvariable=password_var)
    password_label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
