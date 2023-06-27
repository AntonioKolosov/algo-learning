"""
The simple implementation of binary search
"""


def binary_search(lst, target):
    """"""
    # Lowest num
    left = 0
    # Higher num
    right = len(lst) - 1

    while left <= right:
        # Chek the middle element
        mid = (left + right) // 2

        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def main():
    """"""
    # Create a sorted list
    my_list = [2, 4, 7, 10, 13, 20, 25, 30]
    # Need to search this number
    target = 20
    result = binary_search(my_list, target)

    if result != -1:
        print(f"Element {target} found at index {result}.")
    else:
        print("Element not found.")


if __name__ == "__main__":
    main()
