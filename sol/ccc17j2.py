n = int(input())
k = int(input())

acc = 0
for i in range(k+1):
    acc += n * 10**i

print(acc)