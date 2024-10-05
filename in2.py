import re
import os
import tkinter as tk
from tkinter import filedialog, messagebox
import time

# Polish to Python mapping
command_mapping = {
    'drukuj': 'print',
    'wejście': 'input',
    'jeśli': 'if',
    'inaczej': 'else',
    'dopóki': 'while',
    'dla': 'for',
    'funkcja': 'def',
    'zwróć': 'return',
    'przerwij': 'break',
    'kontynuuj': 'continue',
    'importuj': 'import',
    'Prawda': 'True',
    'Fałsz': 'False',
    'Nic': 'None',
    'klasa': 'class',
    'konstruktor': '__init__',
    'czas': 'time',
}

def translate_to_python(cobra_code):
    """Translates COBRA code with Polish commands to Python code."""
    for cobra_cmd, python_cmd in command_mapping.items():
        cobra_code = re.sub(r'\b' + cobra_cmd + r'\b', python_cmd, cobra_code)
    return cobra_code

def execute_cobra_file(file_path):
    """Executes the COBRA (.cob) file after translation to Python."""
    try:
        # Read COBRA file
        with open(file_path, 'r', encoding='utf-8') as cob_file:
            cobra_code = cob_file.read()

        # Translate to Python code
        python_code = translate_to_python(cobra_code)

        # Execute the Python code
        exec(python_code)

    except Exception as e:
        messagebox.showerror("Execution Error", f"Error while executing the COBRA code: {e}")

def open_file_with_tkinter():
    """Opens a file dialog to select a .cob file and execute it."""
    # Set up Tkinter window (without showing a full GUI window)
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Open file dialog to select a .cob file
    file_path = filedialog.askopenfilename(filetypes=[("COBRA files", "*.cob")])

    # If a valid file is selected, execute it
    if file_path and file_path.endswith(".cob"):
        execute_cobra_file(file_path)
    else:
        messagebox.showwarning("Invalid File", "Please select a valid .cob file.")

if __name__ == "__main__":
    open_file_with_tkinter()
