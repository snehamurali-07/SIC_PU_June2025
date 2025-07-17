import sys

queue = []
def enqueue():
    item = input("Enter the item to insert: ")
    queue.append(item)      # insert at last 
    print(f"'{item}' inserted to queue.")

def dequeue():
    if not queue:
        print("Queue is empty. Nothing to delete.")
    else:
        item = queue.pop(0)   # delete at first
        print(f"Deleted item: '{item}'")

def display_queue():
    if not queue:
        print("Queue is empty.")
    else:
        for item in reversed(queue):
            print(f"| {item} |")

def exit_program():
    sys.exit('End of program')

def invalid_choice():
    print('Invalid Choice entered')

def menu(choice):
    match(choice):
        case 1:
            enqueue()
        case 2:
            dequeue()
        case 3:
            display_queue()
        case 4:
            exit_program()
        case _:
            print('Invalid choice')

while True:
    print('1: Insert  2: Delete  3: Display Queue  4: Exit')
    choice = int(input('Your choice plz: '))
    menu(choice)