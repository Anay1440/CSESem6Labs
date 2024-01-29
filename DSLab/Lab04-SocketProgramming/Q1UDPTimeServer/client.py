import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_ip = socket.gethostname()
server_port = 12345

sock.sendto("Hello".encode(), (server_ip, server_port))
data, server_addr = sock.recvfrom(1024)
print("Time received:", data.decode())