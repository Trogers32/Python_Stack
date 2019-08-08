import random

def bubbleSort(arr):
    for j in range(len(arr)-1):
        for i in range(len(arr)-1-j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

arr = []
for i in range(101):
    arr.append(round(random.random()*100))
#print(bubbleSort(arr))

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