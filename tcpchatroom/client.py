import socket
import threading

ip = "0.0.0.0"
port = 9988

def listen():
	while True:
		try:
			response = client_socket.recv(1024)
			if response:
				print(response.decode())
		except:
			print("error")
			client_socket.close()
			break
		
def write():
	while True:
		
		message = input('')
		client_socket.send(message.encode('utf-8'))



client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	client_socket.connect((ip, port))
	print(f"successfully connected to {ip}:{port}")
	login = client_socket.recv(1024).decode()
	if login:
		print(login)
		usrname = input("Enter Username: ")
		client_socket.send(usrname.encode('utf-8'))
	listen_thread = threading.Thread(target = listen)
	listen_thread.start()
	writing_thread = threading.Thread(target = write)
	writing_thread.start()
except:
	print('terminated')
	client_socket.close()
	
