from difference_ops import *

def test_difference_array():
    n = 5
    updates = [
        (1, 3, 10),  # A[1] to A[3] += 10
        (0, 1, 5),   # A[0] to A[1] += 5
    ]
    result = apply_range_updates(n, updates)
    assert result == [5, 15, 10, 10, 0]
    print("Difference array tests passed.")

if __name__ == "__main__":
    test_difference_array()
