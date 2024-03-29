# MSTL Bot Normal Token: 6622962602:AAERgZlXugMGZIA5vqkIpv5KKAAsDUrA6is
from colorama import init, Fore
from os import system
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
def make_python(ID, TOKEN, NAME):
    with open("builder/build.py", "r") as read: 
        text = read.readlines()
        text = "".join(text).replace("TELEGRAM_ID", ID).replace("BOT_TOKEN", f'"{TOKEN}"')
    system("mkdir output")
    with open(f"output/{NAME}.py", "w") as write:
        write.write(text)
    print(Fore.GREEN + "File is created in /output directory.")
def make_exe(NAME, ICON): 
    system("mkdir output/exe")
    system(f"pyinstaller --name {NAME} --onefile -i {icon} --noconsole --distpath output/exe output/mstl.py")
    print(Fore.GREEN + ".exe application is created in /output/exe/mstl")
banner()
try: 
    id = str(input(Fore.GREEN + "[+]" + Fore.WHITE + " write your telegram user id(with @userinfobot): "))
    tok = str(input(Fore.GREEN + "[+]" + Fore.WHITE + " If you want to use custome token write C if not press enter: ")).lower()
    name = str(input(Fore.GREEN + "[+]" + Fore.WHITE + " If you want to use custome name write C if not press enter: ")).lower()
    icon = str(input(Fore.GREEN + "[+]" + Fore.WHITE + " If you want to use custome icon write C if not press enter: ")).lower()    
    if name == "c": 
        name = input("Write your app name(ex: mstl): ")
    else: 
        name = "mstl"
    if tok == "c":
        token = input("Write your bot token: ")
    else: 
        token = "6622962602:AAERgZlXugMGZIA5vqkIpv5KKAAsDUrA6is"
    if icon == "c":
        icon = input("write your icon file address(.ico file): ")
        if icon.endswith(".ico"): pass
        else: icon = "Files/icon.ico"
    make_python(ID=id, TOKEN=token, NAME=name)
    opt = input(Fore.YELLOW + "Make it exe(Y for yes and N for no)? " + Fore.RESET).lower()
    if opt == "y": 
        make_exe(NAME=name, ICON=icon)
    else: 
        exit(Fore.CYAN + "\n\n Good Luck \n\n" + Fore.RESET)
except ValueError: print(Fore.RED + "You must write str."), exit()
except KeyboardInterrupt: exit("\n\n\nGood Luck\n\n")
