n = int(input("enter n > "))

# hasDivisor means divisors except 1 and the number itself
hasDivisor = [False for i in range(n+1)] # from 0 to n
for i in range(2, n + 1):
    for j in range(2 * i, n + 1, i):
        hasDivisor[j] = True
        
print(n - hasDivisor.count(True) - 1) # -1 is for 1