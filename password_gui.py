import tkinter as tk
from password_generator import generate_password
import tkinter.messagebox as messagebox
import csv

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x600")

use_upper_var = tk.BooleanVar()
use_symbol_var = tk.BooleanVar()
use_nums_var = tk.BooleanVar()

password_history = []

MAX_LENGTH = 30

def save_history_to_file():
    with open("passwords.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for entry in password_history:
            if " -> " in entry:
                site, username, password = entry.split(" -> ")
                writer.writerow([site, username, password])

def on_close():
    save_history_to_file()
    root.destroy()

def clear_history():
    password_history.clear()
    # Need to clear history listbox
    history_listbox.delete(0, tk.END)
    display_password.config(text="")
    password_label.config(text="History Cleared!")

def copy_password():
    site = site_entry.get().strip()
    username = username_entry.get().strip()
    password = display_password.cget("text")
    root.clipboard_clear()
    root.clipboard_append(password)
    password_label.config(text="Password Copied!")

    entry = f"{site} | {username} -> {password}"
    password_history.append(entry)
    history_listbox.insert(tk.END, entry)


def generate_password_gui():
    length_str = pass_length_entry.get().strip()
    password_label.config(text="Your new password:")
    clipboard_button.config(state=tk.NORMAL)

    # Convert it to an int, with a fallback or error handling
    try:
        password_length = int(length_str)
        if password_length < 4:
            messagebox.showwarning("Too Short", "Password length must be at least 4.")
            return
        if password_length > MAX_LENGTH:
            messagebox.showwarning("Too Long", f"Password length must be less than {MAX_LENGTH}")
            return
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
#Site Label and Entry
site_label = tk.Label(root, text="Website/App: ")
site_label.pack()
site_entry = tk.Entry(root)
site_entry.pack()

#Username Label and Entry
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

#Password Label and Entry
pass_length = tk.Label(root, text="Password Length: ")
pass_length.pack()
pass_length_entry = tk.Entry(root)
pass_length_entry.pack()

uppercase_label = tk.Checkbutton(root, text="Include Uppercase", variable=use_upper_var)
uppercase_label.pack()

symbol_label = tk.Checkbutton(root, text="Include Symbol", variable=use_symbol_var)
symbol_label.pack()

nums_label = tk.Checkbutton(root, text="Include Numbers", variable=use_nums_var)
nums_label.pack()

password_label = tk.Label(root, text="Your new password:")
password_label.pack()
display_password = tk.Label(root, text="", font=("Helvetica", 14))
display_password.pack(pady=10)

generate_button = tk.Button(root, text="Generate Password", command=generate_password_gui)
generate_button.pack()

clipboard_button = tk.Button(root, text="Copy to Clipboard", command=copy_password)
clipboard_button.pack()
clipboard_button.config(state=tk.DISABLED)

clear_history_button = tk.Button(root, text="Clear History", command=clear_history)
clear_history_button.pack()

history_label = tk.Label(root, text="Password History:")
history_label.pack()

history_listbox = tk.Listbox(root, width=50, height=8)
history_listbox.pack(pady=5)

root.protocol("WM_DELETE_WINDOW", on_close)

def load_history_from_file():
    try:
        with open("passwords.csv", "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 3:
                    site, username, password = row
                    entry = f"{site} | {username} -> {password}"
                    password_history.append(entry)
                    history_listbox.insert(tk.END, entry)
    except FileNotFoundError:
        pass

load_history_from_file()
root.mainloop()