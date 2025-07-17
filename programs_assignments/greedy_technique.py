coins = [1, 2, 5, 10, 20]

n = 96
temp = n
i = 1
num_of_coins = 0
used_coins = []

while temp != 0:
    coin = coins[-i]
    count = temp // coin
    num_of_coins += count
    used_coins.extend([coin] * count)  # track each coin used
    temp = temp % coin
    i += 1

print(f"Total coins used: {num_of_coins}")
print(f"Coins used: {used_coins}")