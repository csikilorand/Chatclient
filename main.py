import socket
import enum

class MessageType(enum.Enum):
    server = f"{0}"
    private = f"{1}"
    group = f"{2}"
    file = f"{3}"

class ServerTypeMessage(enum.Enum):
    connected = f"{0}"
    disconnected = f"{1}"

HOST = "127.0.0.1"
PORT =  27015

SENDER = "Peter"
RECIPIENT = "Batman"



connectMessage = MessageType.server.value + ServerTypeMessage.connected.value + str(len(SENDER)) + SENDER
#disconnectMessage = str(MessageType.server.value) + ServerTypeMessage.disconnected.value + str(len(SENDER)) + SENDER

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((HOST, PORT))

clientSocket.send(connectMessage.encode('utf-8'))

msg = clientSocket.recv(20)
print(msg)
msg = msg.decode('utf-8')

