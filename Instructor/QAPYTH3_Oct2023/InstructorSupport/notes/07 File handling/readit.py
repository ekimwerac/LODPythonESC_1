#!/usr/local/bin/python
"""
typedef struct {
    int a;
    int b;
    double c;
    char name[80];
} data;
"""
import struct
import re

fIn = open("bindata","rb")
data = fIn.read(1024);
fIn.close()
print(len(data))
clean = struct.unpack("iid80s",data)
print(clean)
txt = clean[3].decode().rstrip('\x00')
print(txt)
