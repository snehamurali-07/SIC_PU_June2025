import sys

stack = []

choice = 0

menu = {
    1: "Insert",
    2: "Delete",
    3: "Display Stack",
    4: "End of program" ,
    5: "Invalid Choice"
}

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



while True:
    print('1: Insert  2: Delete  3: Display Stack  4: Exit')
    choice = int(input('Your choice plz: '))
    menu.get((choice))
        
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        display_stack()
    elif choice == 4:
        exit_program()
    elif choice == 5:
        invalid_choice()