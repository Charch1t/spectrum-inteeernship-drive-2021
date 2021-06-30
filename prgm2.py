#To find the trailing zeroes of the factorial of a number

n = int(input("Enter a number"))
i = 5
count = 0

while((n / i) >= 1):
    count = count + int((n / i))
    i = i*5

print("The no. of trailing zeroes in the factorial of a number is",count)

