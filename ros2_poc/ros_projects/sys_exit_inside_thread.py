import sys, time
from threading import Thread
from functools import lru_cache

def testexit():
    time.sleep(5)
    sys.exit()
    print("post thread exit")

t = Thread(target = testexit)
t.start()
t.join()
print("pre main exit, post thread exit")
sys.exit()
print("post main exit")

