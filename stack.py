def push(stack, n, element):
    if is_full(stack, n):
        print("Stack overflow")
    else:
        stack.append(element)
        print(f"{element} pushed to the stack")
        display(stack)


def pop():
    if is_empty(stack):
        print("Stack underflow")
    else:
        stack.pop()
        print("Popped")
        display(stack)


def is_full(stack, n):
    if len(stack) >= n:
        print("Stack is full")
        return True
    else:
        print("Stack is not full")
        return False


def is_empty(stack):
    if not stack:
        print("Stack is empty")
        return True
    else:
        print("Stack is not empty")
        return False


def top(stack):
    if is_empty(stack):
        print("Stack underflow.")
    else:
        print(f"{len(stack)-1}")


def display(stack):
    print(stack)


def clear_screen():
    import os

    os.system("clear")


def main():
    stack = []
    n = int(input("Enter number of elements that can be inserted in the stack:"))

    while True:
        print("\n Stack operations")
        print("1. Push")
        print("2. Pop")
        print("3. Is empty")
        print("4. Is full")
        print("5. Top")
        print("6. Exit")

        choice = int(input("Enter your choice:"))
        if choice == 1:
            element = int(input("Enter element to insert:"))
            push(stack, n, element)

        elif choice == 2:
            pop(stack)

        elif choice == 3:
            is_empty(stack)

        elif choice == 4:
            is_full(stack, n)

        elif choice == 5:
            top(stack)

        elif choice == 6:
            print("Exiting..")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
