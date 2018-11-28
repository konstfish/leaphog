import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 1337))
server_socket.listen(1)
i = 0
while True:
    (client_socket, addr) = server_socket.accept()
    msg = client_socket.recv(1024)
    #print(str(msg))
    i += 1
    isL = False
    r = ""
    l = ""
    for char in msg:
        if(char == "."):
            isL = True
        else:
            if(isL):
                l += char
            else:
                r += char

    l = int(l)
    r = int(r)

    print("R: " + str(r) + " L: " + str(l))

'''
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print >>sys.stderr, 'received "%s"' % data

    finally:
        # Clean up the connection
        connection.close()
'''
