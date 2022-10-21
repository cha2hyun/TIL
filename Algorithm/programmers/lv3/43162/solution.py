
def solution(n, computers):
    visited = [False for i in range(n)]
    answer = 0
    # 트리의 갯수=n
    for node in range(n):
        if visited[node] == False:
            DFS(n, computers, node, visited)
            answer += 1 
    return answer

def DFS(n, computers, node, visited):
	# 현재 노드를 방문 처리
    visited[node] = True
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for connect in range(n):
        if connect != node and computers[node][connect] == 1:
            if visited[connect] == False:
                DFS(n, computers, connect, visited)
            

solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])