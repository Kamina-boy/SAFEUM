from rich.panel import Panel as cm
from rich import print as CM 
import webbrowser
import time

texts = ['               Telegram Channel :- Haxkx', '                Tool Status :- Paid', '              Script Type :- SafeUm Account Maker', '              Script Expire Time :- Unlimted', '              Script Owner Telegram Id :- @Toxic_Tanji ', '             Script Price :- Free For Now']
colors = ['red', 'yellow', 'blue', 'green', 'purple', 'cyan']

formatted_texts = [cm(text, style=f"bold {color}") for text, color in zip(texts, colors)]

for formatted_text in formatted_texts:
    CM(formatted_text)
    
def to(s):
    for char in s + "\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(500.0 / 8000)
        
webbrowser.open("https://t.me/haxkx")

import os
from os import system, name
from ssl import CERT_NONE
from gzip import decompress
from random import choice, choices
from concurrent.futures import ThreadPoolExecutor
from json import dumps

try:
    from websocket import create_connection
except:
    system('pip install websocket-client')
    from websocket import create_connection

failed = 0
success = 0
retry = 0
accounts = []


def work():
    global failed, success, retry
    username = choice('qwertyuiooasdfghjklzxcvpbnm1234567890') + ''.join(choices(list('qwertyuioasdfghjklzxcvbnpm1234567890'), k=16))
    try:
        con = create_connection("wss://195.13.182.213/Auth",
                                header={"app": "com.safeum.android", "host": None, "remoteIp": "195.13.182.213",
                                        "remotePort": str(8080), "sessionId": "b6cbb22d-06ca-41ff-8fda-c0ddeb148195",
                                        "time": "2024-04-11 11:00:00", "url": "wss://51.79.208.190/Auth"},
                                sslopt={"cert_reqs": CERT_NONE})
        con.send(dumps(
         {"action":"Register","subaction":"Desktop","locale":"en_IN","gmt":"+05","password":{"m1x":"06ba394f929f19b1b8e9f78ce47936f3eb1b5b1c6c0eca058ad2181415f3fbfd","m1y":"858e7d2671b24f51627cd3ea992c53096faf23c32a978eb9c6b82fdea57ffb0a","m2":"227ce813ea7adc4c4e716e848bf90c52e822f57fa06ce6d0f15693c31c499fda","iv":"7426098f0ea323abfcf7920e921ebfee","message":"81e52c1ea15c1a328f5427fe3cb7e564a989a32a67132e947d09090c02718c3589e1c041e1c932a21dd7e3224acf3b702c7c937e8bdaec31429af46d91dd09ed85e20145e91c99e92a37c2c5cbfa94f6"},"magicword":{"m1x":"466b3e495488e17355d1360d0c8438e7a86ac57fc959a7b9f438ddd7732063a9","m1y":"0a0258eb5d20b9e51edefe6347d5a24becc05560c6613963d7a4c9ca463304ab","m2":"0ea16a9ef18974858d8f17be997bd839110225d0c3f698b7d5d2600495f21ab7","iv":"17dcf4732b2ebb779e31259d578fc29b","message":"a8605599aaee84c1f1080522e7a7a0f3"},"magicwordhint":"0000","login":str(username),"devicename":"Xiaomi 220733SPH","softwareversion":"1.1.0.1640","nickname":"ndjskms338hd","os":"AND","deviceuid":"b0c55c7c17fddd4b","devicepushuid":"*cYwQmtN0GC4:APA91bGdy73ku9qhNJi8Inhe01e2pXa_dp-CiVULHhPMkcqgi4JFOTCMS-jHhJzxhoO5ZdmGhjFgy-qxGQFSB86l0A1iQGM9RSl3c6X33zPAqxkRQ6C1qm2Gfx94e72joG2twLFbh61E","osversion":"and_12.0.0","id":"311339024"}))
        gzip = decompress(con.recv()).decode('utf-8')
        if '"status":"Success"' in gzip:
            success += 1
            b = accounts.append(username + ':hugg')
            print(b)
            with open('SafeUM_XD.txt', 'a') as f:
                f.write(username + ":hugg \n")

        else:
            failed += 1
    except:
        retry += 1


start = ThreadPoolExecutor(max_workers=1000)

while True:
    start.submit(work)
    print('\n\n\n' + ' ' * 25 + 'Success : ' + str(success) + '\n\n\n' + ' ' * 25 + 'Failed : ' + str(
        failed) + '\n\n\n' + ' ' * 25 + 'ReTry : ' + str(retry))
    hh = str(failed) + str(success) + str(retry)
    if int(success) >= 1000:
        
        print("Created Accounts Successfully Sent To Owner Group")
        
    
    if int(success) > int(0):
        z = "\n".join(accounts)
        
        print("ACCOUNTS GENERATED>>\n", z)
        

    os.system('clear')
    