
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

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

COMMAND_LIST = \
b"""----------------------------
!help list all command. 
!l    list all online user.
!q    leave the chat.
----------------------------
"""

MESSAGE_DASH = b'-'*28 + b'\n'

CLIENT_GREETING_MESSAGE = b"[*] Type Your Name: "
CLIENT_WELCOME_MESSAGE = b"[!] Welcome to Chatroom!\n"
CLIENT_LEAVE_MESSAGE = b"[!] Bye Bye!\n"
CLIENT_HELP_MESSAGE = b"[!] Type !help to see all command.\n"

CHAT_JOIN_MESSAGE = "\n [ {} has Joined the Chat! 🎉 ]\n"
CHAT_LEAVE_MESSAGE = "\n [ {} has leaved the Chat! 🍺 ]\n"