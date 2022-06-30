
def decor_square(func):
    def inner():
        result = func()
        return result

    return decor_square


def square(n):
    print("=========Error!!")
    print("The return type is NOT ", type(str(n)))
    return n ** 2


print(square(6))
# output: =========Error!!
# The return type is NOT <class 'str'>
# 36

# pass in a float


def decor_square(func):
    def inner():
        result = func()
        return result
    return decor_square


def square(n):
    print("The return type is ", type(n))
    return n ** 2

#@check_return_type(float)
def square(n):
    print("The return type ",type(n))
    return n ** 2

print(square(2.9))