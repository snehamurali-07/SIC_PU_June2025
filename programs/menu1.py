choice = 0

menu = {
    1: "Yummy Amul ice cream",
    2: "Spicy masala puri",
    3: "Mango milkshake",
    4: "Lots of pepsi and kurkure",
    5: "End of program"
}
while True:
    print("1. Ice Cream  2. Chats  3. Milshakes  4. Junk  5.Exit")
    choice = int(input("Enter your choice: "))
    print(menu.get(choice))
    if choice == 5:
        break