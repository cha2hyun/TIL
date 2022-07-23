records = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

# 아이디어 1 
# 어차피 마지막에 유저가 닉네임을 변경하면 앞에것도 변경되므로 배열을 거꾸로 돌면서 딕셔너리에 유저아이디를 키값으로 마지막 닉네임을 저장한다.
def solution1(record):
    answer = []
    uids = {}
    for rec_ in reversed(record):
        rec = rec_.split()
        if rec[0] != "Leave" and not rec[1] in list(uids):
            uids[rec[1]] = rec[2]
    
    for rec_ in record:
        rec = rec_.split()
        if rec[0] == "Enter":
            msg = f"{uids[rec[1]]}님이 들어왔습니다."
            answer.append(msg)
        elif rec[0] == "Leave":
            msg = f"{uids[rec[1]]}님이 나갔습니다."
            answer.append(msg)
    return answer
# -> 78.1점 시간초과로 실패 

# 아이디어 2
# For문 1번으로 합쳐보기
def solution2(record):
    answer = []
    uids = {}
    for rec in reversed(record):
        rec = rec.split()
        if rec[0] != "Leave" and not rec[1] in list(uids):
            uids[rec[1]] = rec[2]
        if rec[0] == "Enter":
            msg = f"{uids[rec[1]]}님이 들어왔습니다."
            answer.insert(0, msg)
        elif rec[0] == "Leave":
            msg = f"{uids[rec[1]]}님이 나갔습니다."
            answer.insert(0, msg)
    return answer
# -> 6.3점 런타임에러

# 아이디어 3
# 거꾸로 돌지 않음
def solution(record):
    answer = []
    uids = {}    
    for rec in record:
        rec_split = rec.split()
        if len(rec_split) == 3:
            uids[rec_split[1]] = rec_split[2]
            
    for rec in record:
        rec_split = rec.split()
        if rec_split[0] == 'Enter':
            answer.append('%s님이 들어왔습니다.' %uids[rec_split[1]])
        elif rec_split[0] == 'Leave':
            answer.append('%s님이 나갔습니다.' %uids[rec_split[1]])
            
    return answer

print(solution1(records))