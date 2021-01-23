def solution(progresses, speeds):
    from math import ceil
    left_days = [ceil((100-progresses[idx])/speeds[idx]) for idx in range(len(progresses))]
    left_days.sort()
    print(left_days)
    for i, days in enumerate(left_days):
        for j in range(i+1, len(left_days)+1):
            print(i, left_days[j], days)



    answer = []
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]	
# return = [2, 1]


solution(progresses, speeds)