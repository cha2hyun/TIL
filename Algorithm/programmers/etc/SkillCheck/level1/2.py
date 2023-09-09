def solution(n, lost, reserve):
    student = [1] * n
    for l in lost:
        student[l - 1] -= 1
    for r in reserve:
        student[r - 1] += 1
        
    answer = n
    for idx in range(len(student)):
        if student[idx] == 0:
            if student[idx + 1] == 2:
                student[idx] += 1
                student[idx + 1] -= 1 
            elif student[idx - 1] == 2:
                student[idx] += 1
                student[idx - 1] -= 1
        if student[idx] == 0:
            answer -= 1
            
    return answer

def solution1(n, lost, reserve):
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    for i in set_reserve:
        if i-1 in set_reserve:
            set_reserve.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    return n-len(set_lost)

    print(set_reserve)
    print(set_lost)

n = 5
lost = [2,4]
reserve = [1,3,5]
s = solution1(n, lost, reserve)
print(s)