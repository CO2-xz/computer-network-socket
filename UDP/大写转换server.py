from socket import *
#创建服务器端套接字对象
server_socket=socket(AF_INET,SOCK_DGRAM)
#绑定端口
server_socket.bind(('192.168.31.136',8888))
while True:
    #接收客户端的消息
    recv_data=server_socket.recv(1024)
    print('客户端说：',recv_data.decode('utf-8'))
    if recv_data.decode('utf-8') == 'bye':
        break
    #先将其转换成字符串
    s = recv_data.decode('utf-8')
    #再将其变成大写
    msg=s.upper()
    #发送消息
    server_socket.sendto(msg.encode('utf-8'),('192.168.31.136',8989))
server_socket.close()
