#!/usr/bin/env python3
import tkinter as tk
from turtle import bgcolor, left
import create_mailing_list as cm
import os
from tkinter import LEFT, messagebox 
import getpass

#place current version number here (as global variable)
current_version = float(1.0)
appName = 'Corsaire Mailing List'
USER = getpass.getuser()

def build_window():
    window = tk.Tk()
    window.title(f"Corsaire Mailing List        ver{current_version}")
    window.geometry("400x150")

    label1 = tk.Label(window, text="Create a mailing list from a .csv file")
    label1.pack()

    button1 = tk.Button(window, text="Click to run", command=run)
    button1.pack()

    window.mainloop()
    

def run():
    verify = cm.create_list()
    if verify.lower() == 'yes':
        messagebox.showinfo("Info", "A new list was created")
    else:
        messagebox.showerror("Error", "Error: A list could not be created.")

def load_updates(answer):
    if answer == 'yes':
        #display a messagebox with the option to install updates
        msgBox = messagebox.askquestion(f"{appName}", "Updates are ready. Would you like to install now?")
        if msgBox == 'yes':
            return 'yes'
        elif msgBox == 'no': 
            return None 
        else: 
            return None 
    else: 
        return None

def main():
    answer = cm.check_for_updates(current_version)
    update = load_updates(answer)
    if update == 'yes':
        print()
        os.system('open "/Applications/DO NOT DELETE/Corsaire_update_installer"')
    elif update == None:
        build_window()

        

if __name__ == "__main__":
    main()


