import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname()
local_fqdn = socket.getfqdn()
ip_address = socket.gethostbyname(hostname)
server_port = 33333
server_addr = (ip_address, 33333)
print("Starting upon PORT " + str(server_port) + " on Server: " + str(hostname))
sock.bind(server_addr)
sock.listen()
while True:
    print("Waiting for connection...")
    connection,client_address = sock.accept()
    try:
        print("Connection from: ", client_address)
        while True:
            data = connection.recv(1024)

            if data:
                print("Data Received: ", data.decode("utf-8"))
            else:
                print("No more Data!")
                break
    finally:
        connection.close()
