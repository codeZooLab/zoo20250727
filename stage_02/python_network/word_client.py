#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import *

ADDR = ('127.0.0.1',5555)
sockfd = socket(AF_INET,SOCK_DGRAM)
while True:
    data = input("单词:")
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR)
    data,addr = sockfd.recvfrom(1024)
    print(data.decode())

sockfd.close()