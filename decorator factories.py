def decorator_factory(a,b):
    print("running factories")
    def decorator(fn):
        print("running decorator")
        def inner(*args, **kwargs):
            print("running inner")
            print(a, b)
            result = fn(*args, **kwargs)
            return result
        return inner
    return decorator

decorator = decorator_factory(3, 4)

@decorator
def the_function():
    print("the outer funtion")

the_function()

@decorator_factory(34,23)
def the_other_function():
    print("the other outer factory")

the_other_function = decorator_factory(44, 22)(the_other_function)

the_other_function()
