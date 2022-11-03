import heapq

def dikjstra(start, distance, graph):
    q = []
    # 시작노드 정보 우선순위 큐에 삽입
    heapq.heappush(q, (0, start))
    # 시작노드->시작노드 거리 기록
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        # 큐에서 뽑아낸 거리가 이미 갱신된 거리보다 클 경우(=방문한 셈) 무시
        if distance[now]<dist:
            continue
        # 큐에서 뽑아낸 노드와 연결된 인접노드들 탐색
        for i in graph[now]:
            # 시작->node거리 + node->node의인접노드 거리
            cost = dist+i[1]
            # cost < 시작 일때 node의인접노드 거리
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

def solution(n, edge):
    answer = 0
    distance = [n+1] * (n+1)
    graph = [[] for _ in range(n+1)]

    # 양방향이므로 그래프 양쪽에 추가한다.
    for i in edge:
        graph[i[0]].append((i[1],1))
        graph[i[1]].append((i[0],1))

    # 다익스트라 알고리즘
    dikjstra(1, distance, graph)
    distance.pop(0)
    for dis in distance:
        if dis == max(distance):
            answer += 1
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])) #3

