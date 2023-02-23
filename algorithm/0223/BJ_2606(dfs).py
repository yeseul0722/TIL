
N = int(input())
connect = int(input())
node = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
for __ in range(connect):
    data = list(map(int, input().split()))
    idx = data[0]
    node[idx].append(data[1])
    node[data[1]].append(idx)

visit = [1]
visited[1] = True

answer = -1
while visit:
    now = visit.pop()

    answer += 1

    for next_node in node[now]:
        if visited[next_node]:
            continue

        visited[next_node] = True
        visit.append(next_node)


print(answer)



