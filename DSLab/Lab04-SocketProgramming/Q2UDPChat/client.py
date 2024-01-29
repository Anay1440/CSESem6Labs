import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_ip = socket.gethostname()
server_port = 12345

while True:
    inp = input("Enter text to send ")
    sock.sendto(inp.encode(), (server_ip, server_port))
    print("Client sent:", inp)
    data, server_addr = sock.recvfrom(1024)
    print("Client received:", data.decode())