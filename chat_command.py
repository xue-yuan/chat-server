import chat_message as msg

def help(client_socket):
	client_socket.send(msg.COMMAND_LIST)
	pass

def list(client_socket, ClientList):
	message = b""
	message += msg.MESSAGE_DASH
	for k, v in ClientList.items():
		message += b'- ' + v.encode('utf-8') + b'\n'
	
	message += msg.MESSAGE_DASH
	client_socket.send(message)
	pass

def greet():
	pass

def quit(client_socket, ClientList):
	client_socket.send(msg.CLIENT_LEAVE_MESSAGE)
	client_socket.close()
	del ClientList[client_socket]
	pass