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

server = socket.socket()
# 绑定ip 与 端口
server.bind(('0.0.0.0', 8000))
# 监听
server.listen()

# 阻塞等待链接
sock,addr = server.accept()

date = ""
while True:
    sock.send("welcome to server!".encode("utf8"))
    tmp_date = sock.recv(1024)
    print(tmp_date.decode('utf8'))
    input_date = input()
    sock.send(input_date.encode('utf8'))
    # print(tmp_date)
    if tmp_date:
        date += tmp_date.decode("utf8")
        if tmp_date.decode("utf8").endswith("#"):
            break
    else:
        break

print(date)

sock.close()
