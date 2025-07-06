def apply_range_updates(n, updates):
    diff = [0] * n

    for l, r, val in updates:
        diff[l] += val
        if r + 1 < n:
            diff[r + 1] -= val

    # Build final array using prefix sum
    result = [0] * n
    result[0] = diff[0]
    for i in range(1, n):
        result[i] = result[i - 1] + diff[i]

    return result
