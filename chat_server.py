#! /usr/bin/python3

import socket
import threading
import argparse

# Argument Parse

# Constant Variable
HOST = '0.0.0.0' if True else None
PORT = 5000
PAR = 5
SIZE = 1024
SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind((HOST, PORT))


BANNER = R"""
--------------------------------------------------------------
_________ .__                __________                       
\_   ___ \|  |__ _____ ______\______   \ ____   ____   _____  
/    \  \/|  |  \\__  \\_  __ \       _//  _ \ /  _ \ /     \ 
\     \___|   Y  \/ __ \|  | \/    |   (  <_> |  <_> )  Y Y  \
 \______  /___|  (____  /__|  |____|_  /\____/ \____/|__|_|  /
        \/     \/     \/             \/                    \/ 
--------------------------------------------------------------
""".encode('utf-8')
COMMAND_LIST = b"!help\tlist all command.     \
				!l   \tlist all online user. \
				!q   \tleave the chat."

CLIENT_GREETING_MESSAGE = b"[*] Type Your Name: "
CLIENT_WELCOME_MESSAGE = b"[!] Welcome to Chatroom!\n"
CLIENT_LEAVE_MESSAGE = b"[!] Bye Bye!\n"

CHAT_JOIN_MESSAGE = "\n [ <{}> has Joined the Chat! 🎉 ]\n"
CHAT_HELP_MESSAGE = "\n [Type !help to see all command.] \n"
CHAT_LEAVE_MESSAGE = "\n [ <{}> has leaved the Chat! 🍺 ]\n"

# Static Variable
ClientList = {}
ClientAddress = {}

def LOG(message) -> None:
	print("[LOG]:", message)

def acceptClient() -> None:
	while True:
		client_socket, client_address = SERVER.accept()
		LOG("Connected From {}:{}".format(client_address[0], client_address[1]))
		client_socket.send(BANNER)
		client_socket.send(CLIENT_GREETING_MESSAGE)
		ClientAddress[client_socket] = client_address
		threading.Thread(target=handleClient, args=(client_socket, client_address)).start()
	pass

def handleClient(client_socket, client_address) -> None:
	display_name = client_socket.recv(SIZE).decode('utf-8').strip()
	client_socket.send(CLIENT_WELCOME_MESSAGE)
	broadcastMessage(CHAT_JOIN_MESSAGE.format(display_name).encode('utf-8'))
	ClientList[client_socket] = display_name
	name_tag = "[{}]: ".format(display_name).encode('utf-8')

	while True:
		message = client_socket.recv(SIZE)
		LOG('-'*20)
		LOG(message)

		if message == b"!help\n":
			client_socket.send(COMMAND_LIST)
		elif message == b"!q\n":
			client_socket.send(CLIENT_LEAVE_MESSAGE)
			client_socket.close()
			del ClientList[client_socket]
			broadcastMessage(message=CHAT_LEAVE_MESSAGE.format(display_name).encode('utf-8'))
			LOG("{}:{} is Leaved".format(client_address[0], client_address[1]))
			break
		elif message == b'!l\n':
			# print(ClientList)
			client_socket.send('-'.encode('utf-8')*20 + b'\n')
			for k, v in ClientList.items():
				client_socket.send(b'- ' + v.encode('utf-8') + b'\n')
			client_socket.send('-'.encode('utf-8')*20 + b'\n')
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
