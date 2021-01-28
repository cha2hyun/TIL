def solution(progresses, speeds):
    from math import ceil
    left_days = [ceil((100-progresses[idx])/speeds[idx]) for idx in range(len(progresses))]
    answer = []
    cursor = left_days[0]
    cnt = 0
    for idx, day in enumerate(left_days):
        print(idx,day,cursor,cnt)
        if day > cursor:
            cursor = day
            answer.append(cnt)
            cnt = 1
        else:
            cnt += 1
        if idx == len(left_days) - 1 :
            answer.append(cnt)
    return answer

# 다른 사람 풀이
def solution1(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0] < -((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]


progresses = [93, 30, 55]
speeds = [1, 30, 5]	
# return = [2, 1]
solution(progresses, speeds)

print("==========")
progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
# return = [1, 3, 2]
solution(progresses, speeds)