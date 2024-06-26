import pickle
import gzip

caps = {'Australia':'Canberra', 'Eire'   : 'Dublin',
        'France'   :'Paris',    'Finland':'Helsinki', 
        'UK'       :'London',   'US'     :'Washington'}

outp = gzip.open('capitals.pgz', 'wb')
pickle.dump(caps, outp)
outp.close()
