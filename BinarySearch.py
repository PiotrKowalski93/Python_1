def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        mid = (first + last)//2

        if list[mid] == target:
            return mid
        elif list[mid] < target:
            first = mid + 1
        else:
            last = mid - 1
    
    return None
        
def verify(index):
    if index is not None:
        print("Found at: ", index)
    else:
        print("Not found")


numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

numbers_unsorted = [7,6,4,3,2,1,8,9,15,0,-1,-4]


result = binary_search(numbers, 15)
verify(result)

numbers_unsorted.sort()
print(numbers_unsorted)
result = binary_search(numbers_unsorted, 8)
verify(result)

result = binary_search(numbers_unsorted, -10)
verify(result)