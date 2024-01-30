"""
You will be given a list of integers, , and a single integer . You must create an array of length  from elements of  such that its unfairness is minimized. Call that array . Unfairness of an array is calculated as

Where:
- max denotes the largest integer in 
- min denotes the smallest integer in 

Example



Pick any two elements, say .

Testing for all pairs, the solution  provides the minimum unfairness.

Note: Integers in  may not be unique.

Function Description

Complete the maxMin function in the editor below.
maxMin has the following parameter(s):

int k: the number of elements to select
int arr[n]:: an array of integers
Returns

int: the minimum possible unfairness
Input Format

The first line contains an integer , the number of elements in array .
The second line contains an integer .
Each of the next  lines contains an integer  where .

Constraints




Sample Input

Sample Input #01

10
4
1
2
3
4
10
20
30
40
100
200
Sample Output

Sample Output #01

3
Explanation

Explanation #01
Here ; selecting the  integers , unfairness equals

max(1,2,3,4) - min(1,2,3,4) = 4 - 1 = 3"""


def maxMin(k, arr):
    diff = []
    arr = sorted(arr)
    for i in range(0, len(arr) - k + 1):
        diff.append(arr[i + k - 1] - arr[i])
        print(arr[i : i + k - 1], diff)
    return min(diff)


print(
    maxMin(
        3,
        [
            100,
            200,
            300,
            350,
            400,
            401,
            402,
        ],
    )
)

3
[
    100,
    200,
    300,
    350,
    400,
    401,
    402,
]


def iterative_dfs(start_v):
    visited = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for w in graph[v]:
                stack.append(w)
    return visited


def iterative_dfs(start_v, graph):
    visited = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for w in graph[v]:
                stack.append(w)
    return visited


def recursive_dfs(v, visited=[]):
    visited.append(v)  # 시작 정점 방문
    for w in graph[v]:
        if not w in visited:  # 방문 하지 않았으면
            visited = recursive_dfs(w, visited)
    return visited


from collections import deque


def bfs(start_v):
    visited = [start_v]
    deq = deque()
    deq.append(start_v)
    while deq:
        v = deq.popleft()
        for w in graph[v]:
            if w not in visited:
                visited.append(w)
                deq.append(w)
    return visited


def binary_search(target, data):
    data.sort()
    start = 0  # 맨 처음 위치
    end = len(data) - 1  # 맨 마지막 위치
    while start <= end:
        mid = (start + end) // 2  # 중간값
        if data[mid] == target:
            return mid  # target 위치 반환
        elif data[mid] > target:  # target이 작으면 왼쪽을 더 탐색
            end = mid - 1
        else:  # target이 크면 오른쪽을 더 탐색
            start = mid + 1
    return None


def binary_search_recursion(target, start, end, data):
    if left > right:
        return None
    mid = (left + right) // 2
    if data[mid] == target:
        return mid
    elif data[mid] > target:
        right = mid - 1
    else:
        left = mid + 1
    return binary_search_recursion(target, left, right, data)
