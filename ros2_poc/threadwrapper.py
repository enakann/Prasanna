import threading
import traceback


class ThreadWrapper(threading.Thread):

    def __init__(self,obj,methodName,*args):
        super(ThreadWrapper, self).__init__()
        self.obj=obj
        self.methodName=methodName
        self.args=args
        self.result=None
        self._stop_event = threading.Event()
        #self.daemon=True

    def stop(self):
        self._stop_event.set()
        #self.join()

    def stopped(self):
        return self._stop_event.is_set()


    def run(self):
        print('In %s' % self.name)
        try:
            while not self.stopped():
                getattr(self.obj, self.methodName)(*self.args)
        except Exception as e:
            print("error in thread {}".format(str(self)))
            errorStack = traceback.format_exc()
            print(errorStack)

    def get_result(self):
        return self.result

    def getObject(self):
        return self.obj

    def getMethodName(self):
        return self.methodName

    def getName(self):
        return self.name

    def __str__(self):
        return "tid: " + self.getName() + ", object: " + str(self.getObject()) + ", method: " + self.getMethodName()
