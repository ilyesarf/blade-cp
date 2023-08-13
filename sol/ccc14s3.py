############ THIS IS SOLUTION DOESN'T WORK FOR SOME REASON. I DIDNT FULLY UNDERSTAND THE PROBLEM ############ 

t = int(input())
tests = []
for _ in range(t):
    n = int(input())
    test = []
    for _ in range(n):
        test.append(int(input()))
    
    tests.append(list(reversed(test)))

for test in tests:
    lake = test[1::2]
    print()
    branch = list(reversed(test[::2]))

    lake.extend(branch)
    #print(test)
    test.sort()
    #print(lake, test)

    if lake == test:
        print("Y")
    else:
        print("N")
    

     