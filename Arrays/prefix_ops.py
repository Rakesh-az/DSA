def build_prefix_sum(arr):
    """
    Build a prefix sum array from the given array.
    
    :param arr: List of integers
    :return: List of prefix sums
    """
    prefix = [0] * (len(arr) + 1)
    prefix[0] = arr[0] if arr else 0
    for i in range(1, len(arr)):
        prefix[i] = prefix[i - 1] + arr[i]
    return prefix

def range_sum(prefix, l, r):
    """
    Calculate the sum of elements in the range [l, r) using the prefix sum array.
    
    :param prefix: List of prefix sums
    :param l: Start index (inclusive)
    :param r: End index (exclusive)
    :return: Sum of elements in the range [l, r)
    """
    if l < 0 or r > len(prefix) - 1 or l >= r:
        raise IndexError("Invalid range")
    if r == 0:
        return prefix[r]
    return prefix[r] - prefix[l - 1]