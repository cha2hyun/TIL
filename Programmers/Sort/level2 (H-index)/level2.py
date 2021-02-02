def solution(citations):
    citations.sort(reverse=True)
    print(citations)
    k = enumerate(citations, start=1)
    print(list(k))
    t = map(min, enumerate(citations, start=1))
    print(list(t))

    answer = max(map(min, enumerate(citations, start=1)))
    return answer


print(solution([3, 0, 6, 1, 5]))