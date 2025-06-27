import sys

stack = []
def push():
    item = input("Enter the item to insert: ")
    stack.append(item)
    print(f"'{item}' inserted to stack.")

def pop():
    if not stack:
        print("Stack is empty. Nothing to pop.")
    else:
        item = stack.pop()
        print(f"Deleted item: '{item}'")

def display_stack():
    if not stack:
        print("Stack is empty.")
    else:
        for item in reversed(stack):
            print(f"| {item} |")

def exit_program():
    sys.exit('End of program')

def invalid_choice():
    print('Invalid Choice entered')

def menu(choice):
    match(choice):
        case 1:
            push()
        case 2:
            pop()
        case 3:
            display_stack()
        case 4:
            exit_program()
        case _:
            print('Invalid choice')

while True:
    print('1: Insert  2: Delete  3: Display Stack  4: Exit')
    choice = int(input('Your choice plz: '))
    menu(choice)