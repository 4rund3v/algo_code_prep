
from typing import List
import math

def binary_search(arr: List[int], n: int) -> bool:
    print(arr, n)
    res = False
    low = 0
    high = len(arr)
    while low<high:
        mid = math.floor(low + (high-low)//2)
        val = arr[mid]
        print(low, mid, high, val)
        if val == n:
            res = True
            break
        elif val > n:
            high = mid
        else:
            low = mid + 1
    return res

print(binary_search([1,2,3,4,5,6,7,8,9,10], 5))
print(binary_search([1,2,3,4,5,6,7,8,9,10], 6))
print(binary_search([1,2,3,4,5,6,7,8,9,10], 12))
