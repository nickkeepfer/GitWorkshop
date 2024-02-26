import random
import time

def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

def incredible_sort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)
    return arr

# Numbers I want to sort
numbers_to_sort = [3, 2, 9, 5, 7, 1, 4, 6, 0, 8]

# Time taken to sort
start_time = time.time()
sorted_numbers = incredible_sort(numbers_to_sort)
end_time = time.time()

# Results
print(f"Sorted array: {sorted_numbers}, time taken: {end_time - start_time}")

