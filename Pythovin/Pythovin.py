
import webbrowser
import os
import tkinter as tk
from tkinter import filedialog

def open_file_explorer():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    root.attributes('-topmost', True)  # Asegura que la ventana esté al frente
    folder_selected = filedialog.askdirectory(title="Selecciona una carpeta")
    if folder_selected:
        os.startfile(folder_selected)

open_file_explorer()
webbrowser.open("url_de_tu_repositorio")