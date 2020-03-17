def greeting():
    print("\t","hello word")

greeting()
print("\n",100*"*")
greeting.lang = 'English'
print(greeting.lang)

print("\n",50*"*")
def square(sisi):
    return sisi**2
print("\t","luas kotak adalah: %d "%square(25))

def kotak(a):
    return lambda a : a * a
b = kotak(2)
print("\t","luas persegi adalah: ",b(2))
print("\n",50*"*")

def formalGreeting():
    print("how are you?")
def casual():
    print("what's up?")
def greet(c):
    if c == "formalGreeting":
         formalGreeting()
    else:
         casual()
greet(casual)

print("\n",50*"*")
li1= [1,2,3]
li2= []
for i in li1:
    x= i*2
    li2.append(x)
print(li2)
print("\n",50*"*")
import numpy
li1=numpy.array([1,2,3])
print(li1*2)

print("\n",50*"*")
tahun=numpy.array([1993,1940,1980,1998,1995])
ages=2020-tahun
print(ages)

for i in tahun:
    if i % 2 ==0:
        print(i)
    else:
        print("bukan genap")

