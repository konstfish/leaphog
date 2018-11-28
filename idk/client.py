import socket
import time
import random

def transmission(r, l):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_addr = ('192.168.1.119', 1337)
    client_socket.connect(server_addr)
    x = random.randint(-1000,1000)
    y = random.randint(-1000,1000)
    client_socket.send(str(x) + "." + str(y))
    print("sent" + str(x) + "." + str(y))

i = 0
while True:
    try:
        i += 1
        print("try " + str(i))
        transmission(i, i)
        time.sleep(0.05)
    except:
        print("[H] Connection Lost...")
        time.sleep(2)
'''
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)
try:

    # Send data
    i = 0
    while True:
        print >>sys.stderr
        print(i)
        sock.sendall(str(i))
        i += 1


finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
'''
