#classes and methods
class person:
    def say_hi(self):
        print('hello')
P= person()
P.say_hi()

def scope_test ():
    def do_local ():
        spam = "local spam"
    
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"
    
    spam = "test spam"
    do_local()
    print("after local assgnmen:", spam)
    do_nonlocal()
    print("after nonlocal assignmen:",spam)
    do_global()
    print("after global assignment:", spam)

scope_test ()
print("in global scope:",spam)

