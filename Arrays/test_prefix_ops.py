from prefix_ops import *

def test_prefix_sum():
    arr = [3, 5, 2, 6, 4]
    prefix = build_prefix_sum(arr)
    assert range_sum(prefix, 0, 2) == 10  # 3+5+2
    assert range_sum(prefix, 1, 3) == 13  # 5+2+6
    assert range_sum(prefix, 2, 4) == 12  # 2+6+4

    print("Prefix sum tests passed.")

    try:
        range_sum(prefix, 3, 2)
    except IndexError:
        print("Correctly caught invalid range (l > r)")

    try:
        range_sum(prefix, -1, 2)
    except IndexError:
        print("Correctly caught negative index")

    try:
        range_sum(prefix, 0, 10)
    except IndexError:
        print("Correctly caught out-of-bounds r")


if __name__ == "__main__":
    test_prefix_sum()
