from socket import *
import threading
from threading import Lock

#Socket info and conenction
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("127.0.0.1",serverPort))
serverSocket.listen(1)

# Will print this out if server is running smoothly
print("The server is ready to receive")

'''
    Hashtable would go here
'''
## sentence = "set ploy 1"
## sentence = "get ploy"

#Yuu get connected 
kvstore = {}
file = open('ploytest.txt', 'a+')
while 1:
    connectionSocket, addr = serverSocket.accept()
    #Client input received here
    sentence = connectionSocket.recv(1024).decode()

    request_type = sentence.split()[0]
    print(str(request_type))
    if str(request_type) == "set":
        ## set ops
        print(str(request_type))
        kvstore[sentence[1]] = sentence[2]

        # locks.acquire()

        file.write(key, value)

        # print(kvstore[sentence[1]])
        connectionSocket.send('successfully saved!'.encode())


        #lock.release()

    elif str(request_type) == "get":
        key_val = sentence[1]
        if key_val in kvstore.keys():
            val = str(kvstore[key_val])
            connectionSocket.send(val.encode())

    ''''
    Code for get and set would go here
    Memcache txt file or json
    1. Set Key Value
    If set, add key to txt file to value
    2. Get Key
    Return value based on key that I imported

    Concurrency and compatibility

    '''
    #modified the input
    #capitalizedSentence = sentence.upper()
    #sending it back to client 
   # connectionSocket.send(capitalizedSentence)
    #closing connection of the client, server will still run. Another client can join and connect
    connectionSocket.close()


'''
1. Set 
2. Get



'''