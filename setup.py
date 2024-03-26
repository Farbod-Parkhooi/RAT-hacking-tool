from colorama import init, Fore
init()
def make_exe(ID): 
    make_python(ID=ID)
def make_python(ID):
    from os import system 
    with open("MSTL/Files/info.info", "w") as writer: writer.write(ID)
    print(Fore.GREEN + "Python file is ready in MSTL directory.")
try: id = str(input(Fore.GREEN + "write your telegram user id(with @userinfobot): "))
except ValueError: print(Fore.RED + "You must write str."), exit()
state = str(input(Fore.GREEN + "For make a .exe file wirte EXE and for make a .py file write PY: ")).lower()
if state == "exe": make_exe(ID=id)
else: make_python(ID=id)