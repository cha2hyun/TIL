def solution(progresses, speeds):
    temp = []
    for idx, ps in enumerate(progresses):
        temp.append(ps/speeds[idx])
        print(ps, speeds[idx])
    print(temp)
    answer = []
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]	
# return = [2, 1]


solution(progresses, speeds)