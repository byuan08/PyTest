import socket
server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
server_sock.bind((host,port))

server_sock.listen(5)
while True:
	client_sock,address = server_sock.accept()
	print('got connection from', address)
	client_sock.send('Thank you for connecting')
	client_sock.close()
