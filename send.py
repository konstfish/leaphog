import socket
import time
import random
import sys

def transmission(r, l):
    print("sent" + str(r) + "." + str(l))
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_addr = ('192.168.1.10', 1337)
    client_socket.connect(server_addr)
    client_socket.send(str(r) + "." + str(l))
    print("Sent -> R: " + str(r) + " L:" + str(l))

transmission(str(sys.argv[1]), str(sys.argv[2]))
