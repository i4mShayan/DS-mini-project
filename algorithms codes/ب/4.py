n = int(input("enter n > "))
# hasDivisor means divisors except 1 and the number itself
hasDivisor = [0 for i in range(n+1)] # from 0 to n
for i in range(2, n + 1):
    someUnsufuleOperations()
    if(hasDivisor[i] == 0):
        for j in range(i * i, n + 1, i): # converted 2*i to i*i for better perfomance
            hasDivisor[j] = 1

print(n - hasDivisor.count(1) - 1) # -1 is for 1
