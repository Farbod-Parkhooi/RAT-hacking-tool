# # # def encode_string(s):
# # #     encoded = ""
# # #     count = 1

# # #     for i in range(1, len(s)):
# # #         if s[i].startswith(s[i-1]:
# # #             count += 1
# # #         else:
# # #             if count > 2:
# # #                 encoded += s[i-1] + str(count)
# # #             else:
# # #                 encoded += s[i-1] * count 
# # #             count = 1

# # #     if count > 2:
# # #         encoded += s[-1] + str(count)
# # #     else:
# # #         encoded += s[-1] * count 
# # #     return encoded


# # # def decode_string(encoded):
# # #     decoded = ""
# # #     i = 0

# # #     while i < len(encoded):
# # #         char = encoded[i]
# # #         count = 1
# # #         if i + 1 < len(encoded) and encoded[i + 1].isdigit():
# # #             count = int(encoded[i + 1])
# # #             i += 1 
# # #         decoded += char * count
# # #         i += 1

# # #     return decoded


# # # original_string = "hello budddy im farbod and this is test of you?"
# # # encoded_string = encode_string(original_string)
# # # decoded_string = decode_string(encoded_string)

# # # print("Original String:", original_string)
# # # print("Encoded String:", encoded_string)
# # # print("Decoded String:", decoded_string)

# # # import asyncio

# # # loop = asyncio.new_event_loop()
# # # asyncio.set_event_loop(loop)
# # # loop.run_until_complete(activity(client))
# # # loop.close()

# # import win32gui
# # from time import sleep as sp


# # # sp(2)

# # # current_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
# # # print(current_window)

# # import requests
# # filename="requirements.txt"
# # response = requests.post('https://www.transfernow.net/en', files={"file"):  open(filename, "rb")})#.json()["link"]
# # print(response)
# # print("[*] Command successfuly executed")


# # mouse_listener.stop()
# # keyboard_listener.stop()

import requests
from bs4 import BeautifulSoup

url = 'https://notes.io/short.php'
data = {'txt': 'i want to tell you how it works thank to OXISI'}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Referer': 'https://notes.io/',  # Add the correct referer, if required
}

response = requests.post(url, data=data, headers=headers, timeout=50)

if response.status_code == 200:
    soup = BeautifulSoup(response.content.decode(), "html.parser")
    find_tag = soup.find("a").findAll("div")
    link = "https://www.notes.io/"

    code = str(find_tag[-1]).replace('<div class="key">', "").replace("</div>", "")
    link += code
