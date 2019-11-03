import threading
import sys
import time
import os
import signal
import multiprocessxing

open()
def func():
    i=5
    while i > -1:
        try:
            print(i)
            1/i
            time.sleep(1)
        except Exception as e:
            raise e
        i-=1


def tread():
    for i in range(100):
        print(i)
        time.sleep(1)


def main():
    try:
        t1 = threading.Thread(target=tread)
        t1.start()
        func()
    except Exception as e:
        print(e)
        sys.exit(1)
        #os.kill(os.getpid(),9)
        #os.kill(os.getpid(), signal.SIGINT)

    finally:
        print("cleaning operating")



main()


"""

import threading
import time

class MyThread(threading.Thread):

    # Thread class with a stopme() method.
    # The thread itself has to check
    # regularly for the stopped() condition.

    def __init__(self, *args, **kwargs):
        super(MyThread, self).__init__(*args, **kwargs)
        self.stopme = threading.Event()

        # function using stopme function

    def stop(self):
        self.stopme.set()

    def stopped(self):
        return self.stopme.isSet()

    def run(self):
        while True:
            if self.stopped():
                return
            print("Hello, world!")
            time.sleep(1)


t1 = MyThread()

t1.start()
time.sleep(5)
t1.stop()
t1.join()

"""




