def perfect_square(str_param):

    def inner(x):

        res=x**2

        return res
    return inner


@perfect_square
def display_square(a):
    return a ** 2


print(display_square(3.5))


