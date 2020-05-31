a=1
b=0
for i in range(20):
    c = b + a
    b = a
    a = c
    print(c)