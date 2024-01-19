def solution1(s):
    delete_zero_cnt = 0
    while_cnt = 0
    while True:
        if s == "1":
            break
        while_cnt += 1
        zero_cnt = 0
        for char in s:
            if char == "0":
                zero_cnt += 1
        delete_zero_cnt += zero_cnt
        s = len(s) - zero_cnt
        s = format(s, "b")
    return [while_cnt, delete_zero_cnt]


# 1월 19일 복기로 다시풀어봄
def solution(s):
    count = 0
    zero_count = 0
    while s != "1":
        count += 1
        zero_count += s.count("0")
        next_length = s.count("1")
        s = bin(next_length)[2:]
    return count, zero_count


solution("1111111")
