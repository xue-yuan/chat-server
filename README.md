# Chat Room Server

## About
This script implement the basic function of the chat room. 

**Note:** It is unsecure, unflexible version. Wait for update!

## Usage

* Server-Side:
```python
python chatroom_server.py [PORT]
```
Default Port is 5000.

* Client-Side:
```bash
nc IP PORT
```

## Future Feature
* Client's Application Instead of `nc`.
* Colored Text.
* Private Channel.
* File Transmit.
* Use Configer File to Manage Configurations of Server's Socket.

## Issue
* Does not catch the exception while launch the server.
