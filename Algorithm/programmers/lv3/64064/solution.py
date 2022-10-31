def is_banned_user(string1, string2):
    if len(string1) != len(string2):
        return False
    for i in range(len(string1)):
        if string2[i] == "*":
            continue        
        elif string1[i] != string2[i]:
            return False                
    return True

def solution(user_ids, banned_ids):
    from itertools import permutations
    answer = []
    # banned list 길이만큼 user_ids의 순열을 구한다.
    for user_combs in permutations(user_ids, len(banned_ids)):
        # print(user_combs)
        # 순열을 돌면서 규칙에 맞는 갯수가 banned_ids의 길이면 응답이 된다.
        cnt = 0
        for user, ban in zip(user_combs, banned_ids):
            if is_banned_user(user, ban):
                cnt += 1
            if cnt == len(banned_ids):
                # 중복(순서)) 제거 위해 Set으로 
                if set(user_combs) not in answer:
                    answer.append(set(user_combs))
    return len(answer)
        
    


def lcm(a, b):
    common = 1    
    for i in range(1, min(a, b)):
        if (a % i == 0) and (b % i == 0):
            common = i
    return int(common * (a / common) * (b / common))

def solution(arr):
    answer = arr[0]
    if len(arr) == 1:
        return answer
    for i in arr:
        answer = lcm(answer, i)

    return answer
