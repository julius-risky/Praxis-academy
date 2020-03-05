class A:
    def truth(self):
        return 'All number are even'

class B (A):
    pass

class C(A):
    def truth(self):
        return 'some number are even'

class D(B,C):
    def truth(self,num):
        if num%2 == 0:
            return A.truth(self)
        else:
            return super().truth()
            
d=D()
d.truth(6)
d.truth(5)