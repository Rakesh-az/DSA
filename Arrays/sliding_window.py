def max_sum_subarray_of_size_k(arr, k):
#static sliding window technique to find the maximum sum of a subarray of size k
    if k <= 0 or k > len(arr):
        raise ValueError("Invalid size of subarray")
    
    if not arr:
        return 0
    
    if k == 1:
        return max(arr)

    sub_sum =0
    for i in range(k):
        sub_sum += arr[i]
    
    max_sum = sub_sum

    for i in range(k, len(arr)):
        sub_sum = sub_sum - arr[i - k] + arr[i]
        if sub_sum > max_sum:
            max_sum = sub_sum
    
    return max_sum

def min_subarray_len(arr, target):
    """
    Find the length of the smallest contiguous subarray
    with sum >= target using variable-size sliding window.
    """
    if not arr or target <= 0:
        return 0
    
    l = 0
    cur_sum = 0
    min_len = float('inf')

    for r in range(len(arr)):
        cur_sum += arr[r]
        while cur_sum >= target:
            min_len = min(min_len, r - l + 1)
            cur_sum -= arr[l]
            l += 1
    
    return min_len if min_len != float('inf') else 0

def longest_substring_with_k_distinct(s, k):
    if k <= 0 or not s:
        return 0

    left = 0
    max_len = 0
    char_map = {}

    for right in range(len(s)):
        char = s[right]
        char_map[char] = char_map.get(char, 0) + 1

        while len(char_map) > k:
            left_char = s[left]
            char_map[left_char] -= 1
            if char_map[left_char] == 0:
                del char_map[left_char]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len

    

