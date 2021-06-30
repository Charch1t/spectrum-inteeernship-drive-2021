# To print first n perfect numbers

n = int(input("Enter a number"))

c = 1

while n!=0:
    sum1 = 0
    for i in range(1,c):
        if (c % i == 0):
            sum1 = sum1 + i
    if (sum1 == c):
        print(c)
        n = n - 1
    c = c + 1
        
