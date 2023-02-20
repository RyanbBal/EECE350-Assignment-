from socket import *
import uuid
import time
import datetime

# Set up client socket and get destination IP address
PROXY_IP = '127.0.0.1'
PROXY_PORT = 12400
CLIENT_SOCKET = socket(AF_INET, SOCK_STREAM)  # Create a socket object
CLIENT_SOCKET.connect((PROXY_IP, PROXY_PORT))  # Connect to the server
DEST_IP = input('Enter the IP address: ')

# Send request and record response time
START_TIME = time.time()  # Get the current time
REQUEST = f"GET / HTTP/1.1\r\nHost:{DEST_IP}\r\n\r\n"  # Construct the HTTP request
CLIENT_SOCKET.sendall(REQUEST.encode())  # Send the request to the server
print("Sending request to server...")
print(f"Request sent at: {datetime.datetime.now()}") # Print request time

RESPONSE = CLIENT_SOCKET.recv(4096)  # Receive the response from the server
END_TIME = time.time()  # Get the current time

# Print response and round-trip time
print(f"Response from server: {RESPONSE.decode()}")  # Print the response from the server
print(f"Round-trip time: {END_TIME - START_TIME:.4f} seconds")  # Print the round-trip time
print(f"MAC address is: {hex(uuid.getnode())}") # Print the physical MAC address of the client

# Close socket
CLIENT_SOCKET.close()
