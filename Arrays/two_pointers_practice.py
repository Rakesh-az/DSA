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