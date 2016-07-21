import socket
import sys

HOST, PORT = "192.168.1.25", 10101
data = " ".join(sys.argv[1:])


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5)

try:
    sock.connect((HOST, PORT))
    sock.sendall('date' + "\n")

    received = sock.recv(1024)

finally:
  sock.close()

print "Received: {}".format(received)


