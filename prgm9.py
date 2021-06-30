#To find the nth smallest integer in an array

def nth_smallest(arr , i):
    arr.sort()

    return arr[i-1]


lst = []
k = int(input("Enter the no. of elements"))

for j in range(k):
    element = int(input())
    lst.append(element)

n = int(input("Which smallest integer is to be found"))
x = nth_smallest(lst , n)

print("The n'th smallest integer in the array is",x)
