from socket import *
# Port and server info
serverName = 'localhost'
serverPort = 12000

#Connectig
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

# User input
#sentence = input("Input lowercase sentence:").encode()
#sentence = "set ploy 1".encode()
sentence = "get ploy".encode()

#sending it to sever
clientSocket.send(sentence)

#This is where you receive info from server after connecting and sendint to server
modifiedSentence = clientSocket.recv(1024)#
print("From Server:", modifiedSentence)
clientSocket.close()