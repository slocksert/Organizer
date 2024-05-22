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
        home_directory = os.path.expanduser("~")  # Obtém a pasta home do usuário
    run_main(home_directory if home_directory else None)

def create_gui():
    # Criar janela principal
    window = tk.Tk()
    window.title("File Organizer")

    # Criar rótulo
    label = tk.Label(window, text="Select your home directory")
    label.pack()

    # Criar entrada de texto
    entry = tk.Entry(window, width=50)
    entry.pack()

    # Definir a pasta home do usuário como valor padrão para a entrada
    entry.insert(0, os.path.expanduser("~"))

    # Criar botão para selecionar diretório
    select_button = tk.Button(window, text="Select Directory", command=lambda: select_directory(entry))
    select_button.pack()

    # Criar botão para iniciar o programa
    start_button = tk.Button(window, text="Start Program", command=lambda: start_program(entry))
    start_button.pack()

    # Rodar aplicação
    window.mainloop()

if __name__ == "__main__":
    create_gui()
