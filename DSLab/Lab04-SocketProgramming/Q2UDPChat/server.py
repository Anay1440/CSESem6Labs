import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_ip = socket.gethostname()
server_port = 12345

sock.bind((server_ip, server_port))

while True:
    print("## Server is listening ##")
    data, client_addr = sock.recvfrom(1024)
    print("Server received:", data.decode())
    inp = input("Enter text to send ")
    sock.sendto(inp.encode(), client_addr)
    print("Server sent:", inp)