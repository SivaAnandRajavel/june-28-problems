def give_name(greet):
    def wrapper(*args):
        modified=print(greet())
        return modified
    return wrapper

@give_name('Theresa')
def greeting():
    return 'Hello'

print(greeting())