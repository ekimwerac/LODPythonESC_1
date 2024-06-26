from multiprocessing import Process, Queue
import os

def myfunc(*args):
    print ("From proc", args[1])
    queue = args[0]
    
    word = ''
    while 1:
        word = queue.get()
        if len(word) == 7:
            print (os.getpid(),":",word)
        queue.task_done()
        
    
    
if __name__ == '__main__': 
    queue = Queue()
    p1 = Process(target=myfunc, args=(queue,'1'))
    p2 = Process(target=myfunc, args=(queue,'2'))

    p1.start()
    p2.start()

    for line in open('words'):
        queue.put(line[:-1])

    #queue.put ('END')
    #queue.put ('END')
    queue.close()
    #queue.close()
    
    
    print ("From main:", os.getpid())        
    p1.join()
    p2.join()
    print ("All done")
