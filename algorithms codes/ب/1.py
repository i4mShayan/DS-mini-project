n = int(input("enter n > "))

count = 0
for i in range(2, n + 1):
    someUnsufuleOperations()
    isPrime = 1
    for j in range(2, i):
        if(i%j == 0):
            isPrime = 0
    if(isPrime == 1):
        count += 1

print(count)