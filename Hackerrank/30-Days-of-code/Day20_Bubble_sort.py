import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
arr = a
total_swap=0
num_swap=0
for i in range(0,n,1):
    total_swap += num_swap
    num_swap = 0
    for j in range(0,n-1,1):
        if arr[j]>arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            num_swap+=1
    if num_swap==0:
        break
print("Array is sorted in "+str(total_swap)+" swaps.")
print("First Element: "+str(arr[0]))
print("Last Element: "+str(arr[len(arr)-1]))
