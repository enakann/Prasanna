import multiprocessing
import time
import traceback

class Worker(multiprocessing.Process):

    def __init__(self,obj,methodName,*args):
        super(Worker, self).__init__()
        self.obj=obj
        self.methodName=methodName
        self.args=args
        self.result=None


    def run(self):
        print('In %s' % self.name)
        try:
            print("Working on {}".format(self.methodName))
            while self.is_alive():
                getattr(self.obj,self.methodName)(*self.args)
        except Exception as e:
            errorStack = traceback.format_exc()
            print(errorStack)

    def stop(self):
        self.terminate()
        self.join()

    def get_result(self):
        return self.result

    def getObject(self):
        return self.obj

    def getMethodName(self):
        return self.methodName

    def getOutput(self):
        return self.output

    def getRetVal(self):
        return self.ret_val

    def getName(self):
        return self.name

    def __str__(self):
        return "tid: " + self.getName() + ", object: " + str(self.getObject()) + ", method: " + self.getMethodName()


class A:
    def __init__(self,a):
        self.a=a
        self.ls=[]

    def work(self,i,j):
        while self.a:
            self.a+=i
            print(self.a)
            i+=1
            time.sleep(1)
            self.ls.append(self.a)
        return self.ls

class B:
    def __init__(self,a):
        self.a=a
    def work(self):
        return 1/self.a


def main():
    obj = A(1)
    process = []
    for i in range(2):
        p = Worker(obj, 'work', i, i + 1)
        p.start()
        process.append(p)
    time.sleep(5)
    for p in process:
        print(p.get_result())
        p.stop()

if __name__ == '__main__':
    main()
