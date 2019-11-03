class Singleton(type):
    _instance={}
    def __call__(cls,*args,**kwargs):
        if not cls in cls._instance:
            instance=super().__call__(*args,**kwargs)
            cls._instance[cls]=instance
        return cls._instance[cls]

# class Singleton(object):
#     _instance = None
#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = super(Singleton, cls).__new__(
#                                 cls, *args, **kwargs)
#         return cls._instance
