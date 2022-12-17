def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoit = len(list)//2

        if list[midpoit] == target:
            return True
        else:
            if list[midpoit] < target:
                return recursive_binary_search(list[midpoit + 1:], target)
            else:
                return recursive_binary_search(list[:midpoit], target)


def verify(result):
    print("Target foud: ", result)


numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

numbers_unsorted = [7,6,4,3,2,1,8,9,15,0,-1,-4]


result = recursive_binary_search(numbers, 15)
verify(result)

numbers_unsorted.sort()

result = recursive_binary_search(numbers_unsorted, 8)
verify(result)

result = recursive_binary_search(numbers_unsorted, -10)
verify(result)