class Myclass:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __call__(self, fn):
        def inner(*args, **kwargs):
            print("{0} and {1} is allowed".format(self.a, self.b))
            return fn(*args, **kwargs)
        return inner


obj = Myclass(2, 4)

@obj
def thefunc():
    print("coming home")

thefunc()