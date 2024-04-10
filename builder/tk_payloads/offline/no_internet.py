from tkinter import Tk, Label
root = Tk()
Label(root, text="Check Your internet connection", font=("", 15)).pack()
root.title("Survey")
root.geometry("300x300")
# picture = PhotoImage(file = fr'{cwd}\MSTL\Files\icon.ico')
# root.iconphoto(False, picture) 
root.resizable(False, False)
root.mainloop()