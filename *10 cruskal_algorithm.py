def find_parent(parent, x):
    if parent[x] != x:
        find_parent(parent, parent[x])
    return parent[x]


def uniom_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# node, edge
v, e = map(int, input().split())
parent = [0] * (v + 1)

# all edge list, value
edges = []
result = 0

for i in range(1, v + 1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    # if it's not cycle, union
    if find_parent(parent, a) != find_parent(parent, b):
        uniom_parent(parent, a, b)
        result += cost

print(result)