import socket
import sys
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=5666
server_socket.bind(('127.0.0.1',port))
server_socket.listen(5666)
sentence=''
while True :
            client,add = server_socket.accept(); 
            while(sentence!="CLOSE SOCKET"):
                    sentence= client.recv(1024).decode() 
                    print("Client :               ",sentence)
                    Capital_Sentence = sentence.upper()
                    client.send(Capital_Sentence.encode()) 
                    response_byt=Capital_Sentence.encode()
                    client.send(response_byt)
            client.close()        

      
                
                    


                       
