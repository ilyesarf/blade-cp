n = int(input())

out = set()

for i in range(0, n):
    if n-i > 5 or i > 5:
        continue
    hands = (max([n-i, i]), min([n-i, i]))
    out.add(hands)

#print(out)
print(len(out))