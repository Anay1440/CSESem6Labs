import sys
import threading
import socket
import time

'''
    How to execute:
    Open n number of terminals
    Execute the file with i = 0 to n - 1 in each terminal. Then type anything in any one of the terminals to start the election from that node
    $ python Q1BullyAlgorithm.py i 

    Ex:
    Terminal 1: $ python Q1BullyAlgorithm.py 0
    Terminal 2: $ python Q1BullyAlgorithm.py 1
    Terminal 3: $ python Q1BullyAlgorithm.py 2
    Type anything in Terminal 2 to start the election algorithm from Node index 1
'''

BASE_PORT = 2000

class Node:

    def __init__(self) -> None:
        args = sys.argv
        self.process_ind = int(args[1])
        self.sockets = {}
        self.election_message_received = False

        self.connect_to_lower_nodes()

        threading.Thread(target=self.listen_to_higher_nodes).start()
        threading.Thread(target=self.wait_for_start).start()

    def connect_to_lower_nodes(self):
        for i in range(self.process_ind):
            addr = ('localhost', BASE_PORT + i)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(addr)
            print("Connected to node", i)
            sock.send(str(self.process_ind).encode())
            self.sockets[i] = sock
            threading.Thread(target=self.listen_to_messages_from_lower_nodes, args=(i, )).start()

    def listen_to_messages_from_lower_nodes(self, ind):
        sock = self.sockets[ind]
        data = sock.recv(1024)
        if (data.decode() == "Election"):
            print("Received election message from node", ind)
            time.sleep(1)
            sock.send("OK".encode())
            print("Send OK to node", ind)
            self.start_election()

    def start_election(self):
        ret = []
        for ind in self.sockets.keys():
            if ind > self.process_ind:
                sock = self.sockets[ind]
                sock.send("Election".encode())
                print("Started election")
                thread = threading.Thread(target=self.wait_for_OK, args=(ind, ret, ))
                thread.start()
                thread.join(5)

                if (len(ret) > 0):
                    break
        
        if (len(ret) == 0):
            print("This node is the coordinator")
            for ind in self.sockets.keys():
                sock = self.sockets[ind]
                sock.send("Coordinator".encode())
                sock.close()

            sys.exit()

    def wait_for_OK(self, ind, ret):
        sock = self.sockets[ind]
        data = sock.recv(1024)
        if (data.decode() == "OK"):
            print("Received OK from node", ind, "\nDropping out of election")
            ret.append(1)

    def listen_to_higher_nodes(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', BASE_PORT + self.process_ind))
        sock.listen(10)
        while True:
            conn_sock, client_addr = sock.accept()
            data = conn_sock.recv(1024).decode()
            client_ind = int(data)
            print("Connected to node", client_ind)
            self.sockets[client_ind] = conn_sock
            threading.Thread(target=self.listen_to_messages_from_higher_nodes, args=(client_ind, )).start()

    def listen_to_messages_from_higher_nodes(self, ind):
        sock = self.sockets[ind]
        data = sock.recv(1024)
        if (data.decode() == "Coordinator"):
            print(f"Node {self.process_ind} received coordinator from node {ind}")

            for ind in self.sockets.keys():
                sock = self.sockets[ind]
                sock.close()

            sys.exit()

    def wait_for_start(self):
        inp = input("Enter something if this node should start election\n")
        self.start_election()

if __name__ == '__main__':
    obj = Node()
