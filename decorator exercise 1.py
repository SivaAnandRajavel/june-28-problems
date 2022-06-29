def uppercase(func):
    def wrapper():
        result = func()
        modified = result.upper()
        return modified

    return wrapper


def hello_world():
    return 'hello young, good day!!'


decorate = uppercase(hello_world)
print("After changing the code to upper case ", decorate())  # output: HELLO YOUNG, GOOD DAY!!