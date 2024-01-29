import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

name = input("Enter your name ")
choice = int(input("Enter choice:\n1. Start a chatroom 2. Connect to existing chatroom "))

if (choice == 1):
    port = int(input("Enter port number "))
    ip = socket.gethostname()
    sock.bind((ip, port))
    sock.listen()
    print(f"Started a chatroom at port {port}. Waiting for chatter")
    conn_sock, client_addr = sock.accept()

    peer_name = conn_sock.recv(1024).decode()
    print(f"Connected with {peer_name} at {str(client_addr)}")
    conn_sock.send(name.encode())

    while True:
        message = conn_sock.recv(1024).decode()
        if message == "-exit":
            print(f"{peer_name} left the chat")
            sock.close()
            break
        print(f"{peer_name}: {message}")
        message = input("Me: ")
        conn_sock.send(message.encode())
        if message == "-exit":
            conn_sock.close()
            break
else:
    port = int(input("Enter port number of chatroom "))
    ip = socket.gethostname()
    sock.connect((ip, port))

    sock.send(name.encode())
    peer_name = sock.recv(1024).decode()
    print(f"Connected with {peer_name}")

    while True:
        message = input("Me: ")
        sock.send(message.encode())
        if message == "-exit":
            sock.close()
            break
        message = sock.recv(1024).decode()
        if message == "-exit":
            print(f"{peer_name} left the chat")
            sock.close()
            break
        print(f"{peer_name}: {message}")