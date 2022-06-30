def printing(func):
    def wrapper():
        res = func()
        return res

    return wrapper
def greeting():
    return 'Hello'


decorate = printing(greeting)
print(decorate(),"Theresa")