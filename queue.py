def enqueue(queue, element, n):
    if is_full(queue, n):
        print("queue overflow")
        return
    else:
        queue.append(element)
        print(f"Element enqueued")
        return


def dequeue(queue):
    if is_empty(queue):
        print("Queue underflow")
        return
    else:
        queue.pop()
        print(f"Element dequeued")
        return


def is_empty(queue):
    return len(queue) == 0


def is_full(queue, n):
    return len(queue) == n


def peek(queue):
    if is_empty(stack):
        print("Queue underflow.")
        return
    else:
        print(f"Top element is {queue[-1]}")
        return


def display(queue):
    print(queue)


def clear_screen():
    import os

    os.system("clear")


def main():
    queue = []
    n = int(input("enter number of elements"))
    while True:
        print("Queue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Is empty")
        print("4. Is full")
        print("5. Peek")
        print("6. Display")
        print("7. Exit")

        choice = int(input("Enter your choice: "))
        clear_screen()

        if choice == 1:
            element = int(input("Enter element to enqueue:"))
            enqueue(queue, element, n)

        elif choice == 2:
            dequeue(queue)

        elif choice == 3:
            print("Queue is empty" if is_empty(queue) else "Queue is not empty")

        elif choice == 4:
            print("Queue is full" if is_full(queue, n) else "Queue is not full")

        elif choice == 5:
            peek(queue)

        elif choice == 6:
            display(queue)

        elif choice == 7:
            print("Exiting..")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
