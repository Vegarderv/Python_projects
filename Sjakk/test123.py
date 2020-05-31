def f(x):
    return 4*(x**3)-14*x-2
def g(x):
    return 12*(x**2)-14

def newton(f,g, x):
    return x-(f(x)/g(x))

a = 0
b = 1.75
while True:
    a = b
    b = newton(f, g, a)
    c = abs(b-a)
    if c < 0.001:
        break
print(b)
