def push(stack, n, element):
    if is_full(stack, n):
        print("Stack overflow")
        return
    else:
        stack.append(element)
        print(f"{element} pushed to the stack")
        return


def pop(stack):
    if is_empty(stack):
        print("Stack underflow")
        return
    else:
        stack.pop()
        print("Popped")
        return


def is_full(stack, n):
    return len(stack) == n


def is_empty(stack):
    return len(stack) == 0


def top(stack):
    if is_empty(stack):
        print("Stack underflow.")
    else:
        print(f"Top element is {stack[-1]}")


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
        print("6. Display")
        print("7. Exit")

        choice = int(input("Enter your choice:"))
        clear_screen()
        if choice == 1:
            element = int(input("Enter element to insert:"))
            push(stack, n, element)

        elif choice == 2:
            pop(stack)

        elif choice == 3:
            print("Stack is empty" if is_empty(stack) else "Stack is not empty")

        elif choice == 4:
            print("Stack is full" if is_full(stack, n) else "Stack is not full")

        elif choice == 5:
            top(stack)

        elif choice == 6:
            display(stack)

        elif choice == 7:
            print("Exiting..")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
