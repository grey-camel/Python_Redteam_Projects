import socket


ip_address = '0.0.0.0'
port = 9899

def main():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((ip_address,port))
	server.listen(5)
	print(f'Listening on {ip_address} : {port}')
	client_socket, addr = server.accept()
	print(f"Accepted message from {addr}")
	response = client_socket.recv(4096)
	print(f"Msg: {response.decode('utf-8')}")
	

if __name__ == '__main__':
	main()
