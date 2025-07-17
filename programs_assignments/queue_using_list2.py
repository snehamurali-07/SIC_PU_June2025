# Implement Queue using list, insert front, delete from rear of the list


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.insert(0, value)

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
        return self.queue.pop()

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
        return self.queue[-1]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue (rear -> front):", self.queue)



q = Queue()

def menu(choice):
    match choice:
        case 1:
            ele = int(input("Enter the value to enqueue: "))
            q.enqueue(ele)
        case 2:
            print(f"Dequeued: {q.dequeue()}")
        case 3:
            print(f"Front of Queue: {q.peek()}")
        case 4:
            print("Is Empty:", q.is_empty())
        case 5:
            print("Size of Queue:", q.size())
        case 6:
            q.display()
        case _:
            print("Invalid choice")

while True:
    print('\n1: Enqueue  2: Dequeue  3: Peek  4: Is Empty  5: Size  6: Display  0: Exit')
    choice = int(input('Your choice plz: '))
    menu(choice)