import tkinter as tk
from tkinter import filedialog
import os
from main import main as run_main

def select_directory(entry):
    selected_directory = filedialog.askdirectory()
    if selected_directory:
        entry.delete(0, tk.END)
        entry.insert(0, selected_directory)

def start_program(entry):
    home_directory = entry.get()
    if not home_directory:
        home_directory = os.path.expanduser("~") 
    run_main(home_directory if home_directory else None)

def create_gui():
    window = tk.Tk()
    window.title("File Organizer")

    label = tk.Label(window, text="Select your home directory")
    label.pack()

    entry = tk.Entry(window, width=50)
    entry.pack()

    entry.insert(0, os.path.expanduser("~"))

    select_button = tk.Button(window, text="Select Directory", command=lambda: select_directory(entry))
    select_button.pack()

    start_button = tk.Button(window, text="Start Program", command=lambda: start_program(entry))
    start_button.pack()

    window.mainloop()

if __name__ == "__main__":
    create_gui()
