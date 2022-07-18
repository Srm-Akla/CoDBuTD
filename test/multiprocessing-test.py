from multiprocessing import Pool, TimeoutError, Event, Process
import time
import os
import math
import datetime

def f(x):
    x = time.time()
    print("f:", x)

def g(x):
    x = time.time()
    print("g:", x)

    
def task(event, rerun=None):
    proc_id = os.getpid()
    event.wait()  # Wait for an event
    print('timestamp of process id {}: {}'.format(proc_id, time.time()))
    if rerun is not None:
        time.sleep(rerun)
        print('timestamp of process id {}: {}'.format(proc_id, time.time()))


if __name__ == '__main__':

    #e = Event()  # Create event that will be used for synchronization

    #p1 = Process(target=f, args=(e), range(10))
    #p1.start()
    ## Start second task with rerun after 2 seconds
    #p2 = Process(target=g, args=(e), range(10))

    #p2.start()

    #e.set()  # Set event so all processes can start at the same time
    # start 4 worker processes
    with Pool(processes=4) as pool:

        # print "[0, 1, 4,..., 81]"
        pool.map(f, range(10))
        pool.map(g, range(10))

    print("Now the pool is closed and no longer available")
