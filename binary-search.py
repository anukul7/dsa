def binary_search(n, arr, target):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            print(f"{target} found at index {mid}.")
            return
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    print(f"{target} not found.")


def main():
    arr = []
    n = int(input("Enter number of elements:"))
    for i in range(n):
        arr.append(int(input("Enter elements:")))
    target = int(input("Enter search elements:"))

    binary_search(n, arr, target)


if __name__ == "__main__":
    main()
