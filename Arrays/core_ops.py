def traverse_array(arr):
    for i in range(len(arr)):
        print(f"Index {i}: {arr[i]}")

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def insert_at_index(arr, index, value):
    if index < 0 or index > len(arr):
        raise IndexError("Index out of bounds")
    arr.insert(index, value)  # O(n) due to shift
    return arr

def delete_at_index(arr, index):
    if index < 0 or index >= len(arr):
        raise IndexError("Index out of bounds")
    arr.pop(index)  # O(n) due to shift
    return arr
