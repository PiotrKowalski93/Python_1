from ast import List
import math
import os
import random
import re
import sys

def isValid(s: str) -> bool:
    if len(s) % 2 != 0:
        return False

    opening = ['{', '[', '(']

    chars = [x for x in s]
    stack = []

    for i in range(0, len(s)):
        if s[i] in opening:
            stack.append(s[i])
        else:
            fromStack = stack.pop()
            if s[i] == '}':
                if fromStack != '{':
                    return False
            if s[i] == ']':
                if fromStack != '[':
                    return False
            if s[i] == ')':
                if fromStack != '(':
                    return False

    return True

def searchInsert(nums, target) -> int:
    middle = 0 
    centre = -1

    while centre != target:
        middle = int(len(nums)/2)
        
        if target == nums[middle]:
            return middle
        if target < nums[middle]:
            nums = nums[0:middle]
        else:
            nums = nums[middle:len(nums)]

    return middle

def sortedSquares(nums):
        for i in range(0, len(nums)):
            nums[i] = nums[i] * nums[i]
        nums.sort()

        return nums

    # print(middle)
    # print(middleLeft, " ", middleRight)
def rotate(nums, k):
    nums = nums[::-1] 
    tmp1 = nums[0:k]
    tmp2 = nums[k:len(nums)]
    tmp1 = tmp1[::-1]
    tmp2 = tmp2[::-1]
    nums = tmp1 + tmp2



if __name__ == '__main__':
    
    table = [1,2,3,4,5,6,7]
    rotate(table,4)
    print(table)

    # print(searchInsert([1,3,4,5,6,7,8], 5))
    # print(searchInsert([1,3,4,5], 5))
    # print(searchInsert([1,3,4,5], 2))

    # print(isValid("[]"))
    # print(isValid("{}"))
    # print(isValid("{}[]{]"))
    # print(isValid("{[()]}"))
    # print(isValid("{[(]]}"))

