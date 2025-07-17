import sys

queue = []

choice = 0

menu = {
    1: "Insert",
    2: "Delete",
    3: "Display Queue",
    4: "End of program" ,
    5: "Invalid Choice"
}

def enqueue():
    item = input("Enter the item to insert: ")
    queue.append(item)
    print(f"'{item}' inserted to queue.")

def dequeue():
    if not queue:
        print("Queue is empty. Nothing to delete.")
    else:
        item = queue.pop(0)
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



while True:
    print('1: Insert  2: Delete  3: Display queue  4: Exit')
    choice = int(input('Your choice plz: '))
    menu.get((choice))
        
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display_queue()
    elif choice == 4:
        exit_program()
    elif choice == 5:
        invalid_choice()