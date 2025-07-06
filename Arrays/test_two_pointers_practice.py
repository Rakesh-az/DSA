from two_pointers_practice import has_pair_with_sum

def test_has_pair_with_sum():
    assert has_pair_with_sum([1, 2, 4, 7, 11, 15], 15) == True  # 4 + 11
    assert has_pair_with_sum([1, 2, 4, 7, 11, 15], 10) == False
    assert has_pair_with_sum([], 5) == False
    assert has_pair_with_sum([5], 10) == False

if __name__ == "__main__":
    test_has_pair_with_sum()
    print("All test cases Passed")
