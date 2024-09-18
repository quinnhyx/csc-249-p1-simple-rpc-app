# #!/usr/bin/env python3

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

def encode_request(operation, *args):
    request = f"{operation} {' '.join(map(str, args))}"
    return request.encode()

def main():
    print("client starting - connecting to server at IP", HOST, "and port", PORT)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        operation = input("Enter the operation (concat/reverse): ")
        args = input("Enter words separated by space:").split()
        request = encode_request(operation, *args)
        s.sendall(request)
        print("message sent, waiting for reply")
        data = s.recv(1024)
        print(f"Received: {data.decode()}")
        s.close()

if __name__ == "__main__":
    main()
