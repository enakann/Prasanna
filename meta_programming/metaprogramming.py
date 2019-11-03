class __FactoryMeta(type):

    ressources = {}

    def __getitem__(cls, key):
        if key not in cls.ressources:
            cls.ressources[key] = cls.load(key)
        return cls.ressources[key]

    def load(cls, key):
        raise NotImplementedError


class ConcreteFactory(metaclass=__FactoryMeta):

    @classmethod
    def load(cls, key):
        return "toto"


a = ConcreteFactory["mykey"]
print(a)