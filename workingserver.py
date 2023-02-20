from socket import *
import datetime

# Set up server socket
PROXY_PORT = 12400
PROXY_SOCKET = socket(AF_INET, SOCK_STREAM)
PROXY_SOCKET.bind(("", PROXY_PORT))
PROXY_SOCKET.listen(1)
print('Server is ready to receive connections.')

while True:
    # Accept incoming connection
    CONNECTION_SOCKET, ADDR = PROXY_SOCKET.accept()

    # Receive request and extract IP address
    REQUEST = CONNECTION_SOCKET.recv(1077).decode()
    DEST_IP = REQUEST.split("Host:")[1].split("\r\n")[0]

    # Print received message, IP address and time
    print(f"Received request for IP address {DEST_IP}")
    print(f"Request received at: {datetime.datetime.now()}")

    # Connect to destination IP address and forward request
    try:
        DESTINATION_SOCKET = socket(AF_INET, SOCK_STREAM)
        DESTINATION_SOCKET.connect((DEST_IP, 80))
        DESTINATION_SOCKET.send(REQUEST.encode())
        print(f"Request sent at: {datetime.datetime.now()}")

        # Receive response from the destination server
        RESPONSE = DESTINATION_SOCKET.recv(4096)
        print(f"Response received at: {datetime.datetime.now()}")
        DESTINATION_SOCKET.close()

        # Send the response back to the client
        CONNECTION_SOCKET.send(RESPONSE)

    # Handle errors
    except:
        print("Error occurred while forwarding request")
        CONNECTION_SOCKET.send("Something went wrong.".encode())
        CONNECTION_SOCKET.close()

# Close server socket
PROXY_SOCKET.close()
