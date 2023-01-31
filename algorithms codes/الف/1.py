n = int(input("enter n > "))

count = 0
for i in range(2, n + 1):
    isPrime = True
    for j in range(2, i):
        if(i%j == 0):
            isPrime = False
    if(isPrime):
        count += 1

print(count)