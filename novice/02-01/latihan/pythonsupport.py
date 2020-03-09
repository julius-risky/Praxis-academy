def add(a, b):
    return a + b

plus = add

plus(3, 4)  # returns 7
plus(9,10)

print(plus(9,10))

#lamda
(lambda c,d:c+d)(3,4)

add = lambda c,d: c + d
print(add(3,4))

#menyortir struktur data
authors=['octa','isa','intan']
sorted(authors,key=len)
e = sorted(authors,key=lambda name: name.split()[-1])
print(e)


#val = [1, 2, 3, 4, 5, 6]

# Multiply every item by two
#list(map(lambda x: x * 2, val)) # [2, 4, 6, 8, 10, 12]
# Take the factorial by multiplying the value so far to the next item
#reduce(lambda: x, y: x * y, val, 1)

#def power (base, exp):
    #return base ** exp

#cube = partial(power, exp=3)
#print(cube(5))