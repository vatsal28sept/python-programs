username = "Vatsal"

def func():
    # username = "Patel"
    print(username)

print(username)
func()

x = 99
def func2(y):
    z = x+y
    return z

print(func2(1))

def f1():
    x = 88
    def f2():
        print(x)
    return f2()
f1()

def coder(num):
    def actual(x):
        return x**num
    return actual
f = coder(2)
g = coder(3)

print(f(3))
print(g(3))


