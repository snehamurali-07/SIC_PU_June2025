import sys as s

def ice_cream():
    print('Yummy Amul icecream')

def chats():
    print('Spicy masala puri')

def milk_shake():
    print('Chocolate milkshake')

def junk():
    print('Chips and coke')

def exit_program():
    s.exit('End of program')

def invalid_choice():
    print('Invalid Choice entered')

menu = {
    1 : ice_cream,
    2 : chats,
    3 : milk_shake,
    4 : junk,
    5 : exit_program
}

while True:
    print('1: IceCream  2: Chats  3: MilkShake  4: Junk  5: Exit')
    choice = int(input('Your choice plz: '))
    menu.get(choice, invalid_choice) ()