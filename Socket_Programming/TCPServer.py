from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM) # 创建欢迎套接字
serverSocket.bind(('',serverPort))
serverSocket.listen(1) # 等待有人"敲门" 建立
print("The server is ready to receive")
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    sentence = sentence.upper()
    connectionSocket.send(sentence.encode())
    connectionSocket.close()