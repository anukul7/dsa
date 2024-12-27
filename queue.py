def enqueue(queue, element, n):
    if is_full(queue, n):
        print("queue overflow")
        return
    else:
        queue.append(element)
        print(f"Element enqueued")
        return


def dequeue(queue):
    return queue.pop()


def is_empty(queue):
    return len(queue) == 0


def is_full(queue, n):
    return len(queue) == n


def peek(queue):
    return queue[-1]


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
            print(
                "Queue underflow"
                if is_empty(queue)
                else f" {dequeue(queue)} Element dequeued"
            )

        elif choice == 3:
            print("Queue is empty" if is_empty(queue) else "Queue is not empty")

        elif choice == 4:
            print("Queue is full" if is_full(queue, n) else "Queue is not full")

        elif choice == 5:
            print("Queue underflow" if is_empty(queue) else {peek(queue)})

        elif choice == 6:
            display(queue)

        elif choice == 7:
            print("Exiting..")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
