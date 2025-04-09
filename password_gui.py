import tkinter as tk
from password_generator import generate_password

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

use_upper_var = tk.BooleanVar()
use_symbol_var = tk.BooleanVar()
use_nums_var = tk.BooleanVar()

def copy_password():
    password = display_password.cget("text")
    root.clipboard_clear()
    root.clipboard_append(password)
    display_password.config(text="Password Copied!")

def generate_password_gui():
    length_str = pass_length_entry.get().strip()

    # Convert it to an int, with a fallback or error handling
    try:
        password_length = int(length_str)
    except ValueError:
        display_password.config(text="Please enter a valid number")
        return

    # Get checkbox values
    use_upper = use_upper_var.get()
    use_symbols = use_symbol_var.get()
    use_nums = use_nums_var.get()

    # Generate Password using imported function
    password = generate_password(password_length, use_upper, use_symbols, use_nums)

    # Show it in the label
    display_password.config(text=password)

#Labels
password_frame = tk.Frame(root)
password_frame.pack()
pass_length = tk.Label(password_frame, text="Password Length: ")
pass_length.pack()
pass_length_entry = tk.Entry(password_frame)
pass_length_entry.pack()

uppercase_label = tk.Checkbutton(root, text="Include Uppercase", variable=use_upper_var)
uppercase_label.pack()

symbol_label = tk.Checkbutton(root, text="Include Symbol", variable=use_symbol_var)
symbol_label.pack()

nums_label = tk.Checkbutton(root, text="Include Numbers", variable=use_nums_var)
nums_label.pack()

tk.Label(root, text="Your new password:").pack()
display_password = tk.Label(root, text="", font=("Helvetica", 14))
display_password.pack(pady=10)

generate_button = tk.Button(root, text="Generate Password", command=generate_password_gui)
generate_button.pack()

clipboard_button = tk.Button(root, text="Copy to Clipboard", command=copy_password)
clipboard_button.pack()


root.mainloop()