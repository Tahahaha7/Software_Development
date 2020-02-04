class MySingleton(object):
    _instance = None
    def __new__(self):
        if not self._instance:
            self._instance=super(MySingleton, self).__new__(self)
            self.y = 10
        return self._instance

x = MySingleton()
#print(x.y)
x.y=20
z = MySingleton()
#print(z.y)

class Singleton_lazy(object):
    __instance = None
    def __init__(self):
        if not Singleton_lazy.__instance:
            print("I have already instance.")
        else:
            print("I do not have an instance")
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton_lazy()
        return cls.__instance

class Singleton_strict(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance=super(Singleton_strict,cls).__new__(cls)
        return cls.instance

sl1 = Singleton_lazy()
sl2 = Singleton_lazy()

print("sl1: %s, sl2: %s"%(sl1.getInstance(), sl2.getInstance()))

ss1 = Singleton_strict()
ss2 = Singleton_strict()

print("ss1: %s, ss2: %s"%(ss1, ss2))