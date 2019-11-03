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