import io
import gzip

outp = gzip.open('capitals.gz', 'wb')
outp.write ("To boldly go where no one has\n")
outp.write ("gone previously\n")
outp.close()

bline  = gzip.open('capitals.gz', 'rb').readline()
print (bline)
fh   = io.StringIO(bline.decode())
line = fh.readline ()
print (line)


fh.close()
