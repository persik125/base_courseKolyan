a, b = 1, 1
c = 0
n =int(input())
print(a)
print(b)
for i in range(n):
    c = a + b
    print(c)
    a = b
    b = c