def solution(begin, target, words):
    from collections import deque
    if target not in words:
        return 0

    q = deque()
    # 현재 단어와 이동횟수를 큐에 담는다
    q.append([begin, 0])

    # q를 돌면서
    while(q):
        # pop
        prev, cnt = q.popleft()
        # pop한 값이 타겟과 같으면 리턴
        if prev == target:
            return cnt
        # words를 돌면서
        for i in range(len(words)):
            # 다음에 들어갈 수 있는 단어가 있으면
            if(isOneAlphabetDiff(prev, words[i])):
                # 큐에 넣고 카운트 1증가
                q.append([words[i], cnt+1])        
    
    return 0
    

def isOneAlphabetDiff(prev, next):
    cnt = 0
    for i in range(len(next)):
        if prev[i] != next[i]:
            cnt += 1
        if cnt > 1:
            return False
    return True
        
            

print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))
# print(canBeNextWords('hit','sot'))