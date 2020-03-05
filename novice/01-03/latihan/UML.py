class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        raise NotImplementedError("subclass must implemen abstract metode")

class Dog(Animal):
    def speak(self):
        return self.name+' say swoof!'

class Cat(Animal):
    def speak(self):
        return self.name+' says meaw!'

fido = Dog('fido')
isis = Cat('isis')

print(fido.speak())
print(isis.speak())
