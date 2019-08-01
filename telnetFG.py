'''import os,re,telnetlib
host = "127.0.0.1"
port = 5401

fg = telnetlib.Telnet()
fg.open(host, port)
fg.write("\r\n")
fg.write("set /controls/flight/elevator 25\r\n")
telnet.close()'''

#! /usr/bin/python
import socket

class FlightGearInterface:

    def __init__(self):
        self.fgfs_sock = None
        self.fgfs_file = None

    def connect(self, host, port):
        self.fgfs_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.fgfs_sock.connect((host, port))
        self.fgfs_file = self.fgfs_sock.makefile()
        self.fgfs_sock.sendall("data\r\n")

    def setprop(self, prop, value):
        self.fgfs_sock.sendall("set {0} {1}\r\n".format(prop, value))

    def getprop(self, prop):
        self.some_value = self.fgfs_sock.sendall("get {0}\r\n".format(prop))

        #return self.fgfs_file.readline().strip()

fgfs = FlightGearInterface()
fgfs.connect("127.0.0.1", 5401)
fgfs.setprop("/sim/messages/atc", "teeest")
fgfs.getprop("/orientation/heading-deg")
print(fgfs.some_value)