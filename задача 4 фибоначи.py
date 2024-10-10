fib = [1,1]
for i in range(int(input())-1):
    fib.append(fib[-1]+fib[-2]) # sum(fib[-1:-2])
print(*fib)