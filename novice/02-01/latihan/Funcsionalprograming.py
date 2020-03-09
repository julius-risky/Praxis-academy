list(map(int,["1","2","3"]))

def hello_world(h):
    def world(w):
        print(h,w)
    return world

h = hello_world
x = h("hello")
x
x("world")

function_list = [h,x]
function_list

def naive_sum(list):
    s = 0
    for l in list:
        s += l
    return s

print(naive_sum)