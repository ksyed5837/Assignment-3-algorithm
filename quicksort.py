import random
from typing import List

def randomized_quicksort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    mid  = [x for x in arr if x == pivot]
    right= [x for x in arr if x > pivot]
    return randomized_quicksort(left) + mid + randomized_quicksort(right)

def deterministic_quicksort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr if x < pivot]
    mid  = [x for x in arr if x == pivot]
    right= [x for x in arr if x > pivot]
    return deterministic_quicksort(left) + mid + deterministic_quicksort(right)

def is_sorted(a: List[int]) -> bool:
    return all(a[i] <= a[i+1] for i in range(len(a)-1))

def demo():
    data = [5,3,8,4,2,2,9,1]
    print("Original:", data)
    print("Randomized:", randomized_quicksort(data))
    print("Deterministic:", deterministic_quicksort(data))

if __name__ == "__main__":
    demo()
