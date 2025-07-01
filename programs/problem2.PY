numOfReq = int(input())
arrayOfReq = list(map(int, input().split()))

server1 = 0

for i in range(numOfReq):
    if i % 2 == 0:
        server1 += arrayOfReq[i]
print(server1)