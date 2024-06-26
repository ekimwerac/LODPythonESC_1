import pickle

inp = open('capitals.p', 'rb')
caps = pickle.load(inp)
inp.close()

print (caps)
