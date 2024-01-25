# logo
# 코딩테스트 연습
# 완전탐색
# 피로도
# 도움말
# 컴파일 옵션
# 피로도
# 문제 설명
# XX게임에는 피로도 시스템(0 이상의 정수로 표현합니다)이 있으며, 일정 피로도를 사용해서 던전을 탐험할 수 있습니다. 이때, 각 던전마다 탐험을 시작하기 위해 필요한 "최소 필요 피로도"와 던전 탐험을 마쳤을 때 소모되는 "소모 피로도"가 있습니다. "최소 필요 피로도"는 해당 던전을 탐험하기 위해 가지고 있어야 하는 최소한의 피로도를 나타내며, "소모 피로도"는 던전을 탐험한 후 소모되는 피로도를 나타냅니다. 예를 들어 "최소 필요 피로도"가 80, "소모 피로도"가 20인 던전을 탐험하기 위해서는 유저의 현재 남은 피로도는 80 이상 이어야 하며, 던전을 탐험한 후에는 피로도 20이 소모됩니다.

# 이 게임에는 하루에 한 번씩 탐험할 수 있는 던전이 여러개 있는데, 한 유저가 오늘 이 던전들을 최대한 많이 탐험하려 합니다. 유저의 현재 피로도 k와 각 던전별 "최소 필요 피로도", "소모 피로도"가 담긴 2차원 배열 dungeons 가 매개변수로 주어질 때, 유저가 탐험할수 있는 최대 던전 수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# k는 1 이상 5,000 이하인 자연수입니다.
# dungeons의 세로(행) 길이(즉, 던전의 개수)는 1 이상 8 이하입니다.
# dungeons의 가로(열) 길이는 2 입니다.
# dungeons의 각 행은 각 던전의 ["최소 필요 피로도", "소모 피로도"] 입니다.
# "최소 필요 피로도"는 항상 "소모 피로도"보다 크거나 같습니다.
# "최소 필요 피로도"와 "소모 피로도"는 1 이상 1,000 이하인 자연수입니다.
# 서로 다른 던전의 ["최소 필요 피로도", "소모 피로도"]가 서로 같을 수 있습니다.
# 입출력 예
# k	dungeons	result
# 80	[[80,20],[50,40],[30,10]]	3
# 입출력 예 설명
# 현재 피로도는 80입니다.

# 만약, 첫 번째 → 두 번째 → 세 번째 던전 순서로 탐험한다면

# 현재 피로도는 80이며, 첫 번째 던전을 돌기위해 필요한 "최소 필요 피로도" 또한 80이므로, 첫 번째 던전을 탐험할 수 있습니다. 첫 번째 던전의 "소모 피로도"는 20이므로, 던전을 탐험한 후 남은 피로도는 60입니다.
# 남은 피로도는 60이며, 두 번째 던전을 돌기위해 필요한 "최소 필요 피로도"는 50이므로, 두 번째 던전을 탐험할 수 있습니다. 두 번째 던전의 "소모 피로도"는 40이므로, 던전을 탐험한 후 남은 피로도는 20입니다.
# 남은 피로도는 20이며, 세 번째 던전을 돌기위해 필요한 "최소 필요 피로도"는 30입니다. 따라서 세 번째 던전은 탐험할 수 없습니다.
# 만약, 첫 번째 → 세 번째 → 두 번째 던전 순서로 탐험한다면

# 현재 피로도는 80이며, 첫 번째 던전을 돌기위해 필요한 "최소 필요 피로도" 또한 80이므로, 첫 번째 던전을 탐험할 수 있습니다. 첫 번째 던전의 "소모 피로도"는 20이므로, 던전을 탐험한 후 남은 피로도는 60입니다.
# 남은 피로도는 60이며, 세 번째 던전을 돌기위해 필요한 "최소 필요 피로도"는 30이므로, 세 번째 던전을 탐험할 수 있습니다. 세 번째 던전의 "소모 피로도"는 10이므로, 던전을 탐험한 후 남은 피로도는 50입니다.
# 남은 피로도는 50이며, 두 번째 던전을 돌기위해 필요한 "최소 필요 피로도"는 50이므로, 두 번째 던전을 탐험할 수 있습니다. 두 번째 던전의 "소모 피로도"는 40이므로, 던전을 탐험한 후 남은 피로도는 10입니다.
# 따라서 이 경우 세 던전을 모두 탐험할 수 있으며, 유저가 탐험할 수 있는 최대 던전 수는 3입니다.


def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end="")
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def solution(k, dungeons):
    answer = 0
    stack = []
    for i in range(len(dungeons)):
        # 시작 피로도로 입장 가능한 던전만 stack에 포함
        if dungeons[i][0] <= k:
            stack.append([k - dungeons[i][1], i])
    print("stack", stack)
    order = []
    while stack:
        print(order, "\t", stack)
        order = stack.pop()
        value = order[0]  # 남은 피로도
        size = len(order) - 1
        answer = max(answer, size)
        # print(order, "\t", value, size, answer)
        # 모든 던전 방문하는 순서를 찾았기에 탐색을 중지
        if size == len(dungeons):
            break
        for i in range(len(dungeons)):
            # 방문한적 없으며, 남은 피로도로 방문 가능한 던전
            if i not in order[1:] and dungeons[i][0] <= value:
                temp = order[:]
                temp[0] -= dungeons[i][1]
                temp.append(i)
                stack.append(temp)
    # print(answer, order, value, size, answer)
    return answer


# def solution(k, dungeons):
#     answer = -1
#     return answer


solution(80, [[80, 20], [50, 40], [30, 10]])  # 3


def solution(k, dungeons):
    answer = -1
    return answer


solution(80, [[80, 20], [50, 40], [30, 10]])  # 3
