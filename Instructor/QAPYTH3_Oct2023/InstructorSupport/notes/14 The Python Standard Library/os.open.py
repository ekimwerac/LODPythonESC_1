import os


fd = os.open ('a file', os.O_CREAT|os.O_WRONLY, 0o640)
print ("fd:",fd)
buffer = b'This is some text\r\nanother line\r\n'
bytes = os.write (fd, buffer)
os.close (fd)
print (bytes,"bytes written")
