from core_ops import *

def test_all():
    arr = [10, 20, 30, 40, 50]
    traverse_array(arr)

    assert linear_search(arr, 30) == 2
    assert linear_search(arr, 100) == -1

    assert insert_at_index(arr, 2, 25) == [10, 20, 25, 30, 40, 50]
    assert delete_at_index(arr, 3) == [10, 20, 25, 40, 50]

    traverse_array(arr)

    print("All tests passed!")

if __name__ == "__main__":
    test_all()
