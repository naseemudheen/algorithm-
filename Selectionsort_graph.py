import time

def selection_sort(arr):
    # Loop through all elements in the array
    for i in range(len(arr)):
        # Find the minimum element in the unsorted portion of the array
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # Swap the minimum element with the current element
        arr[i], arr[minIndex] = arr[minIndex], arr[i]

def time_complexity(sort_func, arr):
    # Record the start time
    start_time = time.time()
    # Sort the array
    sort_func(arr)
    # Record the end time
    end_time = time.time()
    # Return the elapsed time
    return end_time - start_time

# Test the selection sort function
arr = [5, 2, 4, 6, 1, 3]
print(selection_sort(arr))  # [1, 2, 3, 4, 5, 6]

# Calculate the time complexity of selection sort
elapsed_time = time_complexity(selection_sort, arr)
print(elapsed_time)  # The time complexity is O(n^2)
