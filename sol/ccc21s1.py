n = int(input())

hs = list(map(int, input().split(' ')))
ws = list(map(int, input().split(' ')))

acc = 0
for i in range(n):
    w = ws[i]
    h = hs[i:i+2]
    acc += w * sum(h)/2

print(acc) 
