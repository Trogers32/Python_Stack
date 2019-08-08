"""Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]"""
def biggie(arr):
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] = "big"
    return arr
testArr = [0,1,2,3,-1,-3,5,-6]
print(biggie(testArr))

"""Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it"""
def countPos(arr):
    count = 0
    for i in range(len(arr)-1):
        if arr[i] > 0:
            count += 1
    arr[len(arr)-1] = count
    return arr
testArr2 = [0,1,2,3,4,5,-1,-2,-3]
print(countPos(testArr2))

"""Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
Example: sum_total([1,2,3,4]) should return 10
Example: sum_total([6,3,-2]) should return 7"""
def sumTotal(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    return total
print(sumTotal(testArr2))

"""Average - Create a function that takes a list and returns the average of all the values.
Example: average([1,2,3,4]) should return 2.5"""
def average(arr):
    ave = 0
    for i in range(len(arr)):
        ave += arr[i]
    return ave/len(arr)
print (average(testArr2))

"""Length - Create a function that takes a list and returns the length of the list.
Example: length([37,2,1,-9]) should return 4
Example: length([]) should return 0"""
def Length(arr):
    return len(arr)
print(Length(testArr2))

"""Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
Example: minimum([37,2,1,-9]) should return -9
Example: minimum([]) should return False"""
def Minimum(arr):
    if len(arr) < 1:
        return False
    small = arr[0]
    for i in range(len(arr)):
        if small > arr[i]:
            small = arr[i]
    return small
print(Minimum(testArr2))

"""Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
Example: maximum([37,2,1,-9]) should return 37
Example: maximum([]) should return False"""
def Maximum(arr):
    if len(arr) < 1:
        return False
    biggest = arr[0]
    for i in range(len(arr)):
        if biggest < arr[i]:
            biggest = arr[i]
    return biggest
print(Maximum(testArr2))

"""Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }"""
def ultA(arr):
    td = {'sumTotal': 0, 'average': 0, 'minimum': arr[0], 'maximum': arr[0], 'length': len(arr)}
    for i in range(len(arr)):
        td["sumTotal"] += arr[i]
        if td["minimum"] > arr[i]:
            td["minimum"] = arr[i]
        if td["maximum"] < arr[i]:
            td["maximum"] = arr[i]
    td["average"] = td["sumTotal"]/len(arr)
    return td
print(ultA(testArr2))

"""Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]"""
def revList(arr):
    arr.append(0)
    for i in range(0,round((len(arr)-1)/2),1):
        arr[len(arr)-1] = arr[i]
        arr[i] = arr[len(arr)-2-i]
        arr[len(arr)-2-i] = arr[len(arr)-1]
    arr.pop()
    return arr
print(revList(testArr2))