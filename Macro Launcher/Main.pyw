import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import time

macro_directory = "data/macro"

def list_ahk_files():
    """Liste tous les fichiers .ahk dans le dossier des macros."""
    if not os.path.exists(macro_directory):
        os.makedirs(macro_directory)
    return [f[:-4] for f in os.listdir(macro_directory) if f.endswith('.ahk')]

def execute_macro():
    """Exécute le fichier .ahk sélectionné."""
    selected_macro = macro_var.get()
    if selected_macro:
        ahk_file = os.path.join(macro_directory, f"{selected_macro}.ahk")
        if os.path.exists(ahk_file):
            messagebox.showinfo("Macro activée", f"La macro '{selected_macro}' a sera activée dans 15 secondes.\n\n-- CTRL+F4 pour quitter la macro --")
            time.sleep(15)
            os.startfile(ahk_file)
        else:
            messagebox.showerror("Erreur", f"Le fichier '{ahk_file}' est introuvable.")
    else:
        messagebox.showwarning("Aucune sélection", "Veuillez sélectionner une macro à activer.")

root = tk.Tk()
root.geometry("400x300")
root.title("Sélectionnez une macro")

label = tk.Label(root, text="Press CTRL + F4 to close ALL macro", font=("Arial", 12), fg="red")
label.pack(pady=10)

macro_var = tk.StringVar()
macros = list_ahk_files()
if macros:
    dropdown = ttk.Combobox(root, textvariable=macro_var, values=macros, state="readonly")
    dropdown.set("Sélectionnez une macro")
    dropdown.pack(pady=10)
else:
    tk.Label(root, text="Aucune macro disponible. Ajoutez des fichiers .ahk dans 'data/macro'.", fg="gray").pack()

activate_btn = tk.Button(root, text="Activer la macro", command=execute_macro)
activate_btn.pack(pady=5)

root.mainloop()
