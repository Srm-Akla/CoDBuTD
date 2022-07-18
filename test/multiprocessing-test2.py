from multiprocessing import Process, Lock
import time

def f(l, i):
    l.acquire()
    print('f: ', time.time())
    l.release()

def g(l, i):
    l.acquire()
    print('g: ', time.time())
    l.release()

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()
        Process(target=g, args=(lock, num)).start()
