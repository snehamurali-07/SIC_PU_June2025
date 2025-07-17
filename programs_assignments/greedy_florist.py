def getMinimumCost(k, c):
    c.sort()
    i = 1
    j = 1
    min_cost = 0
    while i <= len(c):
        if i <= k:
            min_cost += c[-i]
        else:
            min_cost += (j + 1) * c[-i]
            if i % k == 0:
                j += 1
        i += 1
    print("The minimum cost is", min_cost)

if __name__ == '__main__':
    nk = input("Enter space seperated value for n and k: ").split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input("Enter the cost: ").rstrip().split()))
    minimumCost = getMinimumCost(k, c)