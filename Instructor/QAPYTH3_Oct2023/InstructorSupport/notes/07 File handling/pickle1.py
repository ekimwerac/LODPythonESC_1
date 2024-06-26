import pickle

caps = {'Australia':'Canberra', 'Eire'   : 'Dublin',
        'France'   :'Paris',    'Finland':'Helsinki', 
        'UK'       :'London',   'US'     :'Washington'}

outp = open('capitals.p', 'wb')
pickle.dump(caps, outp)
outp.close()
