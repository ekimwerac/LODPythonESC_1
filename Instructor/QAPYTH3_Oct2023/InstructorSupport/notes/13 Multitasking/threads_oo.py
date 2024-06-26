import threading 
import time

class MyThread (threading.Thread):
    def run (self):
        print ("From thread", self.name)
        time.sleep(5)

   
tid1 = MyThread()
tid2 = MyThread()

tid1.start()
tid2.start()
print ("From main")
tid1.join()
tid2.join()