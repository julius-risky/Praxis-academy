class Person:
    def __init__(self,name):
        self.name=name

    def say_hi(self):
        print('halo namaku',self.name)

p = Person('juki')
p.say_hi()