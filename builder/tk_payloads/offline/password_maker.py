# import librarys
from tkinter import *
from tkinter import messagebox as messagebox
import string, random
# value
root = Tk()
Number_of_Letters__Entry = Entry(root, width = 30)
PasswordText = Text(root, width = 50, height = 33, stat = "disabled")
NameEntry = Entry(root, width = 30)
# Label, Entry and Texts
Label(root, text = "Your words:", bg = "white", fg = "black").place(relx=0.1, rely=0.05)
Label(root, text = "Number of letters:", bg = "white", fg = "black").place(relx = 0.1, rely = 0.1)
Number_of_Letters__Entry.place(relx = 0.35, rely = 0.1)
PasswordText.place(relx = 0.1, rely = 0.15)
NameEntry.place(relx=0.35, rely=0.05)
# defs
def Delete():
    PasswordText.delete("1.0", "end")
def Create():
    Number_of_Letters__Entry_G = Number_of_Letters__Entry.get()
    try:
        NameEntry_G = NameEntry.get()
        Number_of_Letters__Entry_G = int(Number_of_Letters__Entry_G)
        strings = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(strings) for i in range(Number_of_Letters__Entry_G))
        password = f"{NameEntry_G}" + password
        PasswordText.config(stat="normal") 
        Delete()
        PasswordText.insert(1.3, password)
        PasswordText.config(stat="disabled")
    except ValueError:
        messagebox.showerror("Error", "Please enter a number")
def Copy():
    PasswordText_G = PasswordText.get(1.0, END)
    root.clipboard_clear()
    root.clipboard_append(PasswordText_G)
def Exit():
    root.destroy()
    exit()
def Info():
    # value
    InfoWindow = Toplevel()
    NameOfSoftwar = Label(InfoWindow, text='Password Maker', padx=70, pady=30,bg='#A8A8A8', fg='white', font=('Times New Roman', 16))
    NameOfCreator = Label(InfoWindow, text='Created by: Farbod Parkhooi', bg='#A8A8A8', fg='white')
    YearOfConstruction = Label(InfoWindow, text='Year of production: 2023', bg='#A8A8A8', fg='white')
    Myemail = Label(InfoWindow, text='My e-mail: farbod.p1390@gmail.com', bg='#A8A8A8', fg='white')
    thank = Label(InfoWindow, text='Thank you for try!', font=('2  Davat', 16), bg='#A8A8A8', fg='white')
    # .place(s)
    thank.place(relx=0.30, rely=0.7)
    Myemail.place(relx=0.05, rely=0.4)
    YearOfConstruction.place(relx=0.05, rely=0.3)
    NameOfCreator.place(relx=0.05, rely=0.2)
    NameOfSoftwar.place(relx=0.10, rely=0)
    # < InfoWindow > options
    InfoWindow.configure(bg='#A8A8A8')
    InfoWindow.title('Info')
    InfoWindow.geometry('300x450')
    InfoWindow.resizable(False, False)

# Buttons
Button(root, text = "COPY",   bg = "white", fg = "black", command = Copy  ).place(relx = 0.8, rely = 0.96)
Button(root, text = "CREATE", bg = "white", fg = "black", command = Create).place(relx = 0.89, rely = 0.96)

# < root > menu
menubar = Menu(root)
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label="menu", menu=file)
file.add_command(label = "Info", command = Info)
file.add_separator()
file.add_command(label = "Exit", command = Exit) 
root.config(menu=menubar)
# < root > options
root.geometry("500x700")
root.resizable(False, False)
root.title("Password Maker")
root.config(bg = "white")
root.mainloop()
