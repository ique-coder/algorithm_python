import operator


def dfs(check):
    global result
    if len(check) == m:
        sort_check = sorted(check)
        if tuple(sort_check) not in result:
            result.add(tuple(check))
    else:
        for i in range(n):
            if d[i] not in check:
                dfs(check + [d[i]])


n, m = map(int, input().split())
d = [i for i in range(1, n + 1)]

result = set([])
dfs([])
result = list(result)
result.sort(key=lambda x:(x[i] for i in range(n)))

for x in result:
    for xx in x:
        print(xx, end=' ')
    print()
print(len(result))