from socket import *
serverName = '43.143.164.206'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_STREAM) # TCP套接字 SOCK_STREAM IPv4 AF_INET
clientSocket.connect((serverName,serverPort)) # 三次握手 建立
sentence = input("Input lowercase sentence:")
clientSocket.send(sentence.encode()) # 直接send内容，不需要send分组信息
modifiedSentence = clientSocket.recv(1024)
print('From Server: ', modifiedSentence.decode())
clientSocket.close()