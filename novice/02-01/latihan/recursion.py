#prosedural

start = 96
kotak=start **2
increment = kotak + 1
cube = increment ** 3
decrement = cube - 1
result = print(decrement)

#fungsi
def call(x,f):
    return f(x)

square = lambda x : x*x
inc = lambda x : x+1
kubus = lambda x : x*x*x
dec = lambda x: x - 1
funcs=[square,inc,kubus,dec]

from functools import reduce
print(reduce(call,funcs,96))