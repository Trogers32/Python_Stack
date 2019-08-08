import random

arr = []
for i in range(1001):
    arr.append(round(random.random()*100))

def selectionSort(arr):
    for i in range(len(arr)):
        temp = arr[i]
        j=i
        ind = i
        for j in range(j,len(arr),1):
            if temp > arr[j]:
                temp = arr[j]
                ind = j
        arr[ind] = arr[i]
        arr[i] = temp
    return arr
print(arr)
print(selectionSort(arr))