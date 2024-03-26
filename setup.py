from colorama import init, Fore
init()
def make_exe(): pass
def make_python(): pass
try: input = int(input(Fore.GREEN + "write your telegram user id(with @userinfobot): "))
except ValueError: print(Fore.RED + "You must write int."), exit()
state = str(input(Fore.GREEN + "For make a .exe file wirte EXE and for make a .py file write PY: ")).lower()
if state == "exe": make_exe()
else: make_python()