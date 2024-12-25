def insert(arr, target, position):
    arr.insert(position, target)
    print(f"Element {target} inserted at index {position}")
    display(arr)


def display(arr):
    print("Array:")
    for i in range(len(arr)):
        print({arr[i]})


def delete(arr, target):
    position = find_index(arr, target)
    if position == -1:
        print(f"Element {target} not found")
        return
    for i in range(position, len(arr) - 1):
        arr[i] = arr[i + 1]
    arr.pop()
    print(f"{target} deleted")
    display(arr)


def search(arr, target):
    position = find_index(arr, target)
    if position == -1:
        print(f"Element {target} not found in the array")
    else:
        print(f"Element {target} found at index {position}")


def update(arr, old_val, new_val):
    position = find_index(arr, old_val)
    if position == -1:
        print(f"Element {old_val} not found in the array")
    else:
        arr[position] = new_val
        print(f"Element {old_val} updated to {new_val} at index {position}")
        display(arr)


def find_index(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def main():
    n = int(input("Enter number of elements:"))
    arr = []
    for i in range(n):
        arr.append(int(input("Enter elements:")))
    while True:

        print("Array Operations:")
        print("1. Insert")
        print("2. Display")
        print("3. Delete")
        print("4. Search")
        print("5. Update")
        print("6. Exit")
        choice = int(input("Enter your choice:"))
        import os

        os.system("clear")

        if choice == 1:
            target = int(input("Enter element to insert:"))
            position = int(
                input("Enter the position at which you want to insert the element:")
            )
            insert(arr, target, position)
        elif choice == 2:
            display(arr)
        elif choice == 3:
            target = int(input("Enter the element to delete: "))
            delete(arr, target)
        elif choice == 4:
            target = int(input("Enter the element to search: "))
            search(arr, target)
        elif choice == 5:
            old_val = int(input("Enter the element to update: "))
            new_val = int(input("Enter the new element: "))
            update(arr, old_val, new_val)
        elif choice == 6:
            print("Exit")
            break

        else:

            print("Invalid choice")


if __name__ == "__main__":
    main()
