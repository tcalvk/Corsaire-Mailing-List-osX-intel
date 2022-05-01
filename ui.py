#!/usr/bin/env python3
import tkinter as tk
import create_mailing_list as cm
import os
from tkinter import messagebox 
import getpass

#place current version number here (as global variable)
current_version = float(1.0)
appName = 'Email List App'
USER = getpass.getuser()

def build_window():
    window = tk.Tk()
    window.title("Create Mailing List")
    window.geometry("300x150")
    create_buttons()  
    window.mainloop()

def create_buttons():
    button1 = tk.Button(text="Click to run", command=run)
    button1.pack()

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


