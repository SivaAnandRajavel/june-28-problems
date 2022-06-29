#@execute_log
def multiply(*nums):
    mult = 1
    for n in nums:
        mult *= n
    return mult

#@execute_log
def hello_world():
    return 'hello world!!'

print(multiply(6, 2, 3)) # 36
print(hello_world()) # hello world!!
print(multiply(2.2, 4)) # 8.8
print(hello_world()) # hello world!!