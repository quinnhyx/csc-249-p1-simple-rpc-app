# #!/usr/bin/env python3

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

def decode_request(request_bytes):
    request = request_bytes.decode()
    parts = request.split()
    operation = parts[0]
    args = parts[1:]
    return operation, args

def process_request(operation, args):
    if operation == "concat":
        return "".join(args)
    elif operation == "reverse":
        concatenated = ''.join(args)
        return concatenated[::-1]
    else:
        return "Invalid operation"

def main():
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected established with {addr}")
                data = conn.recv(1024)
                operation, args = decode_request(data)
                response = process_request(operation, args)
                if not data:
                    break
                print(f"Received client message: '{data!r}' [{len(data)} bytes]")
                print(f"echoing '{data!r}' back to client")
                conn.sendall(response.encode())

    print("server is done!")

    conn.close()

if __name__ == "__main__":
    main()
