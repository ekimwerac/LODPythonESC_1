from multiprocessing import Process

#p = Pool(5)
#
#def f(x):
#    return x*x
#
#p.map(f, [1,2,3])

import time

def myfunc(*args):
    print ("From proc", args)
    time.sleep(5)

print (__name__)
if __name__ == '__main__':   
    p1 = Process(target=myfunc, args='1')
    p2 = Process(target=myfunc, args='2')

    p1.start()
    p2.start()
    print ("From main")
    p1.join()
    p2.join()
