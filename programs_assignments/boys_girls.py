def check_arrangement(b, g):
    b.sort()
    g.sort()
    
    if all(g[i] >= b[i] for i in range(len(b))) or all(b[i] >= g[i] for i in range(len(b))):
        return "yes"
    else:
        return "no"

n = int(input())
boys = list(map(int, input().split()))
girls = list(map(int, input().split()))

print(check_arrangement(boys, girls))