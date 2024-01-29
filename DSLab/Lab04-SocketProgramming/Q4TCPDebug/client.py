import socket
serverIP = 'localhost'
serverPort = 16000
clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSock.connect((serverIP, serverPort))

message = input("Input integers with space in between: ").encode()
# Original: message2 = input("Enter the length of the set: ").encode()

clientSock.send(message)
# Original: clientSock.send(message2)

# Original: data = clientSock.recv(1024)
data = clientSock.recv(1024).decode()

temp = [float(x) for x in data.split(' ')]

print("The total of all numbers is: " + str(temp[0]))
print("The lowest number is: " + str(temp[1]))
print("The highest number is: " + str(temp[2]))
print("The mean is: " + str(temp[3]))

clientSock.close()