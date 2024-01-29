import socket

serverIP = 'localhost'
serverPort = 16000
serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSock.bind((serverIP, serverPort))
serverSock.listen(1)
print("TCP server has started and is ready to receive")

while True:
    connection, addr = serverSock.accept()
    # Original: data = connection.recv(1024)
    data = connection.recv(1024).decode()
    if not data: break

    temp = [float(x) for x in data.split(' ')]

    print("Received data:", temp)

    length = len(temp)
    maximum = max(temp)
    minimum = min(temp)
    total = sum(temp)
    mean = total/length
    msg = str(total) + " " + str(minimum) + " " + str(maximum) + " " + str(mean)
    # Original: connection.send(str(msg))
    connection.send(str(msg).encode())