import socket
import time
import random
import sys

IP = '192.168.1.70'
PORT = 1337

def transmission(r, l):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_addr = (IP, PORT)
    client_socket.connect(server_addr)
    client_socket.send(str(r) + "." + str(l))
    print("Sent -> R: " + str(r) + " L:" + str(l))

transmission(str(sys.argv[1]), str(sys.argv[2]))
