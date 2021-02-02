def solution(priorities, location):
    from collections import deque
    d = deque([ (v,i) for i,v in enumerate(priorities) ])
    answer = 0
    while len(d):
        item = d.popleft()
        if d and max(d)[0] > item[0]:
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer

priorities = [1, 2, 9, 1, 1, 1]
location = 0
a = solution(priorities, location)
print(a)
