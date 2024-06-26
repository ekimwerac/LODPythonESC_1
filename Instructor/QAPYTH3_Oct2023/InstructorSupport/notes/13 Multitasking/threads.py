from threading import Thread
import time

def myfunc(*args):
    print ("From thread", args)
    time.sleep(5)
   
tid1 = Thread(target=myfunc, args='T1')
tid2 = Thread(target=myfunc, args='T2')
tid1.start()
tid2.start()
print ("From main")
tid1.join()
tid2.join()