import sys

def func():
    try:
        i = 5
        while i > -1:
            print(i)
            1/i
            i-=1
    except Exception as e:
        raise e




try:
    func()
except Exception as e:
    print(e)
    #sys.exit(1)
    raise SystemExit
finally:
    print("clean up process")
    for i in range(10):
        print(i)
        import time;time.sleep(4)