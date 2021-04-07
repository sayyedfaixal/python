import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
local_hostname = socket.gethostname()
ip_address = socket.gethostbyname(local_hostname)
server_addr = (ip_address, 33333)
sock.connect(server_addr)
temp_data = [15,22,21,23,22,25]

for entry in temp_data:
    print("Data: '%s' Sent." %entry)
    new_data = str("Temperature: " + str(entry)).encode("utf-8")
    sock.sendall(new_data)
    time.sleep(2)

sock.close()
