import socket
import threading


def process_connection(client):
    data = b''
    while True:
        chunk = client.recv(1024)
        data += chunk
        if len(chunk) < 1024:
            break

    # 打印从客户端接收的数据
    print(f'data: {data}')
    # 给客户端发送响应数据
    return_data = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<!DOCTYPE html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /></head><h1>肖子虹 20195515</h1><h1>多线程webserver</h1><h1>计算机网络实验报告二</h1>'
    client.sendall(return_data.encode('utf-8'))
    # 关闭客户端连接对象
    client.close()

def main():
    # 创建 socket 对象
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 允许端口复用
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定 IP 和端口
    sock.bind(('127.0.0.1', 8001))
    # 开始监听
    sock.listen(5)

    while True:
        # 等待客户端请求
        client, addr = sock.accept()
        print(f'client type: {type(client)}\naddr: {addr}')
        t = threading.Thread(target=process_connection, args=(client,))
        t.start()


if __name__ == '__main__':
    main()