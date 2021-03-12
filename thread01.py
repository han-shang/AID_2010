from threading import Thread
from threading import Lock
a=b=1
def fun01():
    while True:
        lock.acquire()
        if a != b:
            print("a= %d,b= %d" %(a,b))
        lock.release()

lock = Lock()
t = Thread(target=fun01)
t.start()

while True:
    with lock:
        a+=1
        b+=1

t.join()