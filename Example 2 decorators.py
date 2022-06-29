def decorator_function(original_function):
    def wrapper_function():
        print("my_func is running...  ")
        return original_function()
    return wrapper_function

# output: my_func is running...

#Python is fun
@decorator_function
def my_func():
    print('Python is fun!!')

my_func()