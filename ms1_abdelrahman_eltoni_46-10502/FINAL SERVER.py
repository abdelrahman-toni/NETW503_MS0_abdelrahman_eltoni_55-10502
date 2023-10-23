import socket
import threading

port = 6588
client_counter = 0

def threaded(client, addr):
    print(f'NEW CONNECTION {addr} connected')
    sentence = ''
    while sentence != "CLOSE SOCKET":
        try:
            sentence = client.recv(1024).decode()
            if not sentence:
                break
            print(f'Client {addr}: {sentence}')
            Capital_Sentence = sentence.upper()
            client.send(Capital_Sentence.encode())
        except ConnectionResetError:
            break
    client.close()

def main():
    print('server is starting...')
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', port))
    server_socket.listen(5)
    while True:
        client, addr = server_socket.accept()
        client_thread = threading.Thread(target=threaded, args=(client, addr))
        client_thread.start()
        print(f"[ACTIVE CONNECTIONS] {client_counter}")

if __name__ == "__main__":
    main()