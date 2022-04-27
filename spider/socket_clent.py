#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Untitled-1.py
@Time    :   2022/01/01 00:24:32
@Author  :   辛酉
@Version :   1.0
@Desc    :   socket客户端
'''
# here put the import lib
import socket
#新建套接字
client = socket.socket()

# 链接
client.connect(('192.168.1.184', 8000))

# client.send(b'bobby')
server_data = client.recv(1024)
print("server response: {}".format(server_data.decode("utf8")))
while True:
    input_data = input()
    client.send(input_data.encode("utf8"))
    server_data = client.recv(1024)
    print("server response: {}".format(server_data.decode("utf8")))


# client.close()

