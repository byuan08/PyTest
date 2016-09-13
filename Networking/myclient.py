import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
client_sock.connect((host,port))

resp = client_sock.recv(1024)
print(resp)
client_sock.close()