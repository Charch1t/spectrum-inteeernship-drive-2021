def triplet(arr,l,val):
    for i in range(0, l-2):
        for j in range(i+1 , l-1):
            for k in range(j+1 , l):
                if arr[i] + arr[j] + arr[k] == val:
                    print("Triplet is", arr[i],"," , arr[j], "," , arr[k])


arr = []
n = int(input("Enter the no. of elements"))

for x in range(n):
    element = int(input())
    arr.append(element)

val = int(input("Enter the value"))
l = len(arr)
triplet(arr , l , val)
        
