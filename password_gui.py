import tkinter as tk
from password_generator import generate_password

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

use_upper_var = tk.BooleanVar()
use_symbol_var = tk.BooleanVar()

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

    # Generate Password using imported function
    password = generate_password(password_length, use_upper, use_symbols)

    # Show it in the label
    display_password.config(text=f"Your new password is: {password}")

#Labels
pass_length = tk.Label(root, text="Password Length: ")
pass_length.pack()
pass_length_entry = tk.Entry(root)
pass_length_entry.pack()

uppercase_label = tk.Checkbutton(root, text="Include Uppercase", variable=use_upper_var)
uppercase_label.pack()

symbol_label = tk.Checkbutton(root, text="Include Symbol", variable=use_symbol_var)
symbol_label.pack()

#Button
generate_button = tk.Button(root, text="Generate Password", command=generate_password_gui)
generate_button.pack()

#Label
display_password = tk.Label(root, text=f"Your new password is: ")
display_password.pack()

root.mainloop()