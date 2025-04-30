#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   Untitled-1.py
@Time    :   2022/01/01 00:24:32
@Author  :   辛酉
@Version :   1.0
@Desc    :   socket服务端
"""

# here put the import lib
import socket
import threading

server = socket.socket()
# 绑定ip 与 端口
server.bind(('0.0.0.0', 8000))
# 监听
server.listen()


def handle_sock(sock, addr):
    while True:
        # sock.send("welcome to server!".encode("utf8"))
        tmp_date = sock.recv(1024)
        print(tmp_date.decode('utf8'))
        input_date = input()
        sock.send(input_date.encode('utf8'))


# 获取客户端并启动线程去处理
while True:
    # 阻塞等待链接
    sock, addr = server.accept()
    # 启动一个线程去处理新的用户
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()

date = ""

while True:
    if tmp_date:
        date += tmp_date.decode("utf8")
        if tmp_date.decode("utf8").endswith("#"):
            break
    else:
        break

print(date)

sock.close()
