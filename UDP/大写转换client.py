from socket import *
udp_client=socket(AF_INET,SOCK_DGRAM)
# 绑定一个固定的端口，不然主机发送的时候端口是随机的，接收数据的时候就麻烦了
udp_client.bind(('',8989)) #绑定的是本机，端口是8989
addr=('192.168.31.136',8888)
while True:
    data = input('>')
    udp_client.sendto(data.encode('utf-8'),addr)
#设置最大接收字节
    recv_data=udp_client.recvfrom(1024)
    print("服务器端说",(recv_data[0].decode('utf-8')))

udp_client.close()
#  这个注意一下：recvfron  返回的结果是以元组为返回结果（内容，（IP+port））