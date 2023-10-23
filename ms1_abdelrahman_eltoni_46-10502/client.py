import socket    
import select
import sys  
      
 

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)        
print ("Client Socket successfully created")

port = 6588

          
s.connect(('127.0.0.1',6588))

msg=""
while(msg!="CLOSE SOCKET"):
    msg=input()
    
    s.send(msg.encode())
    print(s.recv(1024).decode())
    
s.close()




