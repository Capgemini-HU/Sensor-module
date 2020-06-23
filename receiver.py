import socket
import sys

# HOST needs to be IP of server.
HOST, PORT = "192.168.1.120", 9999
data = " ".join(sys.argv[1:])
print("Host:", HOST)
print("Port:", PORT)
print("sending data:", data)

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(data.encode())

    # Receive data from the server and shut down
    received = sock.recv(1024)
finally:
    sock.close()

print("Sent:     {}".format(data))
print("Received: {}".format(received))
