import math
import os
import random
import re
import sys

#n - lenght of arr

def insertionSort2(n, arr):
    for i in range(0, n):
        if arr[i] > arr[i+1]:
            last_value = arr[i+1]
            was_inserted = False

            for j in range(i+1, -1, -1):
                array = ""
                
                if arr[j] > last_value:
                    arr[j+1] = arr[j] # right shift
                    for k in range(0, len(arr)): array += str(arr[k]) + " "
                    print(array)
                else:
                    arr[j+1] = last_value
                    for k in range(0, len(arr)): array += str(arr[k]) + " "
                    print(array)
                    was_inserted = True
                    break
            
            if was_inserted == False :
                arr[0] = last_value
                array = ""
                for j in range(0, len(arr)): array += str(arr[j]) + " "
                print(array)   
                
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
