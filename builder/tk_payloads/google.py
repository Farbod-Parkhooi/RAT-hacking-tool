import webview
root = Tk()
root.geometry("800x450")
webview.create_window('Google', 'https://www.google.com')
webview.start()