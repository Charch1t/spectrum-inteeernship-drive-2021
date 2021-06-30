#To find the GCD of an array of integers

def find_gcd(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            gcd = i
    return gcd

lst = []
n = int(input("Enter the no. of elements in the list"))

for i in range(n):
    element = int(input())
    lst.append(element)

num1 = lst[0]
num2 = lst[1]

gcd = find_gcd(num1 , num2)

for j in range(2 , len(lst)):
    gcd = find_gcd(gcd , lst[j])

print("The GCD of the numbers is",gcd)







