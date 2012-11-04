#!/usr/bin/python

import socket
import sys
from ctypes import *
import re

class WP(Structure):
	_fields_ = [("x",c_double),("y",c_double)]

def newMovementCommand(command, option):
	return "<MOVCMD>{0} {1}</MOVCMD>\n".format(command,option);

if len(sys.argv) == 3:
	TCP_IP = sys.argv[1]
	TCP_PORT = int(sys.argv[2])
else:
	TCP_IP = "127.0.0.1"
	TCP_PORT = 5006

BUFFER_SIZE = 1024
MESSAGE = "Hello, World!\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Connecting to " + TCP_IP + " on port " + str(TCP_PORT)
s.connect((TCP_IP, TCP_PORT))
#s.send(MESSAGE)
#s.send(newMovementCommand("FWD", 2*pow(10,6)))
s.send(newMovementCommand("TURN", 46.204))
data = s.recv(BUFFER_SIZE)
print "received data:", data
s.close()
