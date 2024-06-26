import pickle
import gzip

inp = gzip.open('capitals.pgz', 'rb')
caps = pickle.load(inp)
inp.close()

print (caps)
