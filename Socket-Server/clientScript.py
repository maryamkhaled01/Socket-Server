import socket
import sys

# CLIENT SIDE

# Define the host's name and port
HOST, PORT = "localhost", 9999  

# Take the command-line argument (data that will be sent)
data = " ".join(sys.argv[1:])

# Create a socket 
# (AF_INET means the socket will use IPv4 addresses and SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock: 
    # Connect to server 
    sock.connect((HOST, PORT))
    
    # Send data to server
    sock.sendall(bytes(data, "utf-8"))

    # Receive data from the server and shut down
    received = str(sock.recv(1024), "utf-8") # Decode recieved data to string using unicode character set

# Get the server IP
server_ip = socket.gethostbyname(HOST)

# Print the message sent to the server the received one
print(f"Sent Message To ({server_ip}): {data}")
print(f"Received Message From ({server_ip}): {received}")