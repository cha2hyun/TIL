def solution(s):
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
        s = format(s, 'b')
    return [delete_zero_cnt, while_cnt]



solution("110010101001")