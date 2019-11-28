#! /usr/bin/python3

import socket
import threading
import argparse

import chat_message as msg
import chat_command as cmd

# Argument Parse

# Constant Variable
HOST = '0.0.0.0' if True else None
PORT = 5000
PAR = 5
SIZE = 1024
SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind((HOST, PORT))

# Static Variable
ClientList = {}
ClientAddress = {}

def LOG(message) -> None:
	print("[LOG]:", message)

def acceptClient() -> None:
	while True:
		client_socket, client_address = SERVER.accept()

		LOG(f"Connected From {client_address[0]}:{client_address[1]}")
		
		client_socket.send(msg.BANNER)
		client_socket.send(msg.CLIENT_GREETING_MESSAGE)
		ClientAddress[client_socket] = client_address
		threading.Thread(target=handleClient, args=(client_socket, client_address)).start()
	pass

def handleClient(client_socket, client_address) -> None:
	display_name = client_socket.recv(SIZE).decode('utf-8').strip()
	client_socket.send(msg.CLIENT_WELCOME_MESSAGE)
	client_socket.send(msg.CLIENT_HELP_MESSAGE)
	broadcastMessage(msg.CHAT_JOIN_MESSAGE.format(display_name).encode('utf-8'))
	ClientList[client_socket] = display_name
	name_tag = f"[{display_name}]: ".encode('utf-8')

	while True:
		try:
			message = client_socket.recv(SIZE)
		except OSError:
			broadcastMessage(message=msg.CHAT_LEAVE_MESSAGE.format(display_name).encode('utf-8'))
			break

		LOG('-'*20)
		LOG(message)

		if message == b"!help\n":
			cmd.help(client_socket)
		elif message == b"!q\n":
			cmd.quit(client_socket, ClientList)
			broadcastMessage(message=msg.CHAT_LEAVE_MESSAGE.format(display_name).encode('utf-8'))
			LOG(f"{client_address[0]}:{client_address[1]} is Leaved")
			break
		elif message == b'!g\n':
			cmd.greet()
		elif message == b'!l\n':
			cmd.list(client_socket, ClientList)
		elif not message.isspace():
			broadcastMessage(name_tag, message)
	pass

def broadcastMessage(NameTag=b"", message=b"") -> None:
	for client in ClientList:
		client.send(NameTag + message)
	pass

def mainProcess() -> None:
	MAIN_THREAD = threading.Thread(target=acceptClient).start().join()
	pass

if __name__ == '__main__':
	SERVER.listen(PAR)
	LOG("Waiting for Connection...\n")
	mainProcess()
	LOG("Server Shutdown...\n")
	SERVER.close()
