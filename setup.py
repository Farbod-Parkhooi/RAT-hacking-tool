from colorama import init, Fore
init()
def make_python(ID):
    from os import system 
    with open("MSTL/Files/info.info", "w") as writer: writer.write(ID)
    print(Fore.GREEN + "Python file is ready in MSTL directory.")
try: id = str(input(Fore.GREEN + "write your telegram user id(with @userinfobot): "))
except ValueError: print(Fore.RED + "You must write str."), exit()
make_python(ID=id)
