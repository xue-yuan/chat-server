# Chat Room Server

## About
This script implement the basic function of the chat room. 

**Note**
It is unsecure, unflexible in this version.

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
* Use Config File to Manage Configurations of Socket.

## Issue
* Does not catch the exception while launch the server.