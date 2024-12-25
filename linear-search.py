def linear_search(n, arr, target):
    for i in range(n):
        if arr[i] == target:
            print(f"{target} found at index {i}")
            return
    print(f"{target} element not found.")


def main():
    n = int(input("Enter number of elements:"))
    arr = []
    for i in range(n):
        arr.append(int(input("Enter elements:")))
    target = int(input("Enter search element:"))

    linear_search(n, arr, target)


if __name__ == "__main__":
    main()
