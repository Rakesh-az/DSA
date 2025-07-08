def has_pair_with_sum(arr, target):
    l,r = 0,len(arr) - 1
    while l < r:
        pair_sum = arr[l] + arr[r]
        if pair_sum > target:
            r -= 1
        elif pair_sum < target:
            l += 1
        else:
            return True
    return False

def reverse_string(arr: list[str]) -> None:
    """
    Reverse the characters of arr in-place using two pointers.
    Input: ['h', 'e', 'l', 'l', 'o']
    Output: ['o', 'l', 'l', 'e', 'h']
    """
    l,r = 0,len(arr) - 1
    while l < r:
        arr[l],arr[r] = arr[r],arr[l]
        l += 1
        r -= 1

def remove_duplicates(arr: list[int]) -> int:
    """
    Return new length of array after removing duplicates in-place.
    Also modify the array to hold only unique elements at the front.
    Input: [1,1,2,2,3]
    Output: length=3, arr = [1,2,3,...]
    """
    if not arr:
        return 0

    l = 0  # points to last unique
    for r in range(1, len(arr)):
        if arr[r] != arr[l]:
            l += 1
            arr[l] = arr[r]

    return l + 1

def sorted_squares(arr: list[int]) -> list[int]:
    """
    Given sorted array with negative numbers, return sorted array of squares.
    Input: [-4, -1, 0, 3, 10]
    Output: [0, 1, 9, 16, 100]
    """
    n = len(arr)
    sq_arr = [0] * n
    l, r = 0, n - 1

    for i in range(n - 1, -1, -1):
        l2 = arr[l] ** 2
        r2 = arr[r] ** 2
        if l2 >= r2:
            sq_arr[i] = l2
            l += 1
        else:
            sq_arr[i] = r2
            r -= 1

    return sq_arr
