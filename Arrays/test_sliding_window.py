from sliding_window import max_sum_subarray_of_size_k, min_subarray_len, longest_substring_with_k_distinct

def test_fixed_size_window():
    print("Testing fixed-size sliding window...")
    assert max_sum_subarray_of_size_k([2, 1, 5, 1, 3, 2], 3) == 9
    assert max_sum_subarray_of_size_k([1, 1, 1, 1, 1], 2) == 2
    assert max_sum_subarray_of_size_k([10, 20, 30, 40], 2) == 70
    assert max_sum_subarray_of_size_k([4, 3, 2, 1], 1) == 4
    try:
        max_sum_subarray_of_size_k([1, 2, 3], 5)
    except ValueError:
        print("✅ Correctly raised ValueError for invalid k")
    print("✅ Fixed-size window tests passed.\n")

def test_variable_size_window():
    print("Testing variable-size sliding window...")
    assert min_subarray_len([2, 3, 1, 2, 4, 3], 7) == 2  # [4, 3]
    assert min_subarray_len([1, 1, 1, 1, 1], 11) == 0
    assert min_subarray_len([1, 4, 4], 4) == 1
    assert min_subarray_len([1, 2, 3, 4, 5], 11) == 3  # [3, 4, 5]
    assert min_subarray_len([], 5) == 0
    print("✅ Variable-size window tests passed.\n")

def test_k_distinct_size():
    assert longest_substring_with_k_distinct("eceba", 2) == 3  # "ece"
    assert longest_substring_with_k_distinct("aa", 1) == 2      # "aa"
    assert longest_substring_with_k_distinct("abcadcacacaca", 3) == 11  # "cadcacacaca"

if __name__ == "__main__":
    test_fixed_size_window()
    test_variable_size_window()
    test_k_distinct_size()
    print("🎉 All sliding window tests passed!")
