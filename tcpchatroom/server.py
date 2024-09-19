import socket
import threading

ip = '0.0.0.0'
port = 9988
clients = []
username = []

def add_usr(client, clients):
	intro_msg = ("Please provide a username: ")
	client.send(intro_msg.encode())
	userid = client.recv(1024).decode()
	clients.append(client)
	username.append(userid)
	index = clients.index(client)
	usr = username[index]
	print(f"Accepted connection from {usr}!")
	welcome = f"{usr} has joined the chat!"
	broadcast_msg(clients, welcome)


def handle_client(client,addr,clients):
	
	try:
		index = clients.index(client)
		usr = username[index]
		while True:
			try:
				message = client.recv(1024).decode('utf-8')
				if not message:
					break
				msg = (f"{usr}: " + message)
				broadcast_msg(clients, msg)
			except:
				break
	finally:
		msg = f"{usr} has left the room"
		broadcast_msg(clients,msg)
		clients.remove(client)
		
		username.remove(usr)
		

		username.remove(usr)
		print(clients, usr)
		
def broadcast_msg(clients, msg):
	for client in clients:
		if client in clients:
			client.send(msg.encode('utf-8'))
		else:
			continue
def main():
	
	server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_sock.bind((ip,port))
	server_sock.listen()
	print(f"Listening on {ip}:{port}")
	while True:
		

		client, addr = server_sock.accept()
		add_usr(client, clients)
		
			
		client_handler = threading.Thread(target=handle_client, args=(client,addr,clients))
			
		client_handler.start() 


	client.close()
	client_handler.join()
if __name__ == "__main__":
	main()
