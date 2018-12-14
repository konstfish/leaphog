#!/usr/bin/env python

import socket
from hedgehog.client import connect

print("run")

IP = "" # blank if you want it to listen to every adress - clients ip if it should only listen to the client
PORT = 1337

# garbage but i dont care

with connect(emergency=15) as hedgehog:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen(1)
    while True:
        (client_socket, addr) = server_socket.accept()
        msg = client_socket.recv(1024)
        #print(str(msg))
        test = str(msg)

        isL = False
        r = ""
        l = ""

        i = 2

        while(i < len(test) - 1):
            #print(test[i])
            if(str(test[i]) == "."):
                isL = True
                i += 1
            if(isL):
                l += str(test[i])
            else:
                r += str(test[i])
            i += 1
        l = int(l)
        r = int(r)

        # cloud have done this in one line with split() but i wrote this about
        # 6 monts ago and i dont want to change it without being able to test it

        print("R: " + str(r) + " L: " + str(l))

        hedgehog.move(0,r)
        hedgehog.move(1,l)
