#To find all the prime numbers  from 1 to n


n = 7

for num in range(1 , n+1):
    if num>1:
        for j in range(2 , num):
            if (num % j == 0):
                break
        else:
            print(num)
