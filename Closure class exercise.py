def multiplies_of(n):
    def multiply(k):
        # yield k * n
        for i in range(1,10):
            mul=i*n
            if mul<=29:
                #  print(mul)
                yield mul

    return multiply



m3 = multiplies_of(3)
m3_under30 = m3(30)
m7_under30 = multiplies_of(7)(30)
print(m3(5))
print(type(m3_under30))
print(*m3_under30)
print(*m7_under30)
# print(next(m3))
