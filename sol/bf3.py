import math

def isPrime(num):
    if num > 1:
        for i in range(2, math.floor(math.sqrt(num)+1)):
            if (num % i) == 0:
                return False
        
    else:
        return False

    return True

min = int(input())

while not isPrime(min):
    min += 1

print(min)