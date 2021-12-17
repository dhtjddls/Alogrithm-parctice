n,m = map(int, input().split())

no_listen = [input() for i in range(n)]
no_see = [input() for i in range(m)]
no_listen = set(no_listen)
no_see = set(no_see)
result = sorted(list(no_see & no_listen))

print(len(result))
for i in result:
    print(i)

