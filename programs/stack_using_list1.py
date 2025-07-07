# Implement Stack using list, insert and delete from rear of the list


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            print("Empty Stack")
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack (top -> bottom):", self.stack[::-1])


s = Stack()
def menu(choice):
    match choice:
        case 1:
            ele = int(input("Enter the value to insert:"))
            s.push(ele)
        case 2:
            print(f"Popped element:{s.pop()}")
        case 3:
            print(f"Top of the stack:{s.peek()}")
        case 4:
           print(f"Is stack empty:{s.is_empty()}")
        case 5:
            print(f"Size of the stack:{s.size()}")
        case 6:
            s.display()
        case _:
            print("Invalid choice")

while True:
    print('\n1: Insert  2: Delete  3: Peek the top of stack  4: Is Empty  5: Size  6: Display')
    choice = int(input('Your choice plz: '))
    menu(choice)
