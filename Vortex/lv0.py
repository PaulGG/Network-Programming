#!/usr/bin/python3
import socket
import struct
HOST = "vortex.labs.overthewire.org"
PORT = 5842
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
sum = 0
for i in range(0,4):
    oof = s.recv(4)
    oof = int.from_bytes(oof, byteorder="little")
    sum += oof
# number must be converted to 32 bit which is why we have the sum & 0Xffffffff
# data sent must be packed into little endian format
packed = struct.pack("<I", (sum & 0Xffffffff)) 
s.send(packed)
print(s.recv(1024))
s.close()                       