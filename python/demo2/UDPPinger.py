from socket import *
import time

serverName = '39.106.169.243'  # 服务器地址
serverPort = 12000  # 端口号
clientSocket = socket(AF_INET,SOCK_DGRAM) # 创建UDP套接字,使用IPv4协议
clientSocket.settimeout(1) # 设置套接字超时值 1s

for i in range(0,10):
        sendTime = time.time()
        message = ('Ping %d %s' %(i + 1,sendTime) ).encode() # 生成数据报,编码为bytes以便发送
        try:
            clientSocket.sendto(message,(serverName,serverPort)) # 将信息发送到服务器
            modifiedMessage,serverAddress = clientSocket.recvfrom(1024) # 从服务器接受信息,同时也能得到服务器地址
            rtt = time.time() - sendTime # 计算往返时间
            print('Sequence %d:Reply from %s RTT=%.3fs' %(i+1,serverName,rtt));
        except Exception as e:
            print('Sequence %d:Request timed out' %(i+1))

clientSocket.close() #关闭套接字