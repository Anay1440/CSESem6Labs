import socket
import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_ip = socket.gethostname()
server_port = 12345

sock.bind((server_ip, server_port))

while True:
    print("Waiting for client at port:", server_port)
    data, client_addr = sock.recvfrom(1024)
    currtime = str(datetime.datetime.now())
    sock.sendto(currtime.encode(), client_addr)