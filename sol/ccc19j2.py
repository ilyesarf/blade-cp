l = input()
inp = []
for i in range(int(l)):
    x = input()
    inp.append([int(x.split(' ')[0]), x.split(' ')[1]])

for x in inp:
    print(x[1] * x[0])
