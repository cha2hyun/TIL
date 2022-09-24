# s = "aabbaccc" #7 
# s = "ababcdcdababcdcd" #9 8개단위 2ababcdcd
# s = "abcabcdede" #8
s = "abcabcabcabcabcabcdededededede" #14 6개단위 2abcabc2dedede
# s = "xababcdcdababcdcd" #17


# 아이디어 1 
# 문자열을 나누는 숫자는 문자열 길이의 약수여야만 한다. 
# 약수로 나누었을때 나누어질지 확인하고 
# 최대한 짧은 단위를 리턴한다
def solution(s):
    answer = len(s)
    for divider in range(1, len(s)//2+1):
        # if len(s) % divider == 0:
        result = ""
        prev = s[0:divider]
        cnt = 1            
        for idx in range(divider, len(s), divider):
            if prev == s[idx : idx + divider]:
                cnt += 1
            else:
                result += str(cnt) + prev if cnt >= 2 else prev
                prev = s[idx : idx + divider]
                cnt = 1
        result += str(cnt) + prev if cnt >= 2 else prev
        answer = min(answer, len(result))
    return answer


# 다른사람 풀이
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",

    'aaaaaa',
]

for x in a:
    print(solution(x))


    # for divider in range(1, len(s)//2+1):
    #     if len(s) % divider == 0:
    #         print(divider, "로 나눕니다.")
    #         arr = list(map(''.join, zip(*[iter(s)]*divider)))
    #         print(arr)
    #         cursor = 0
    #         cnt = 1
    #         for idx in range(0, len(arr)):                
    #             if arr[idx] == arr[idx+1]:
    #                 cnt += 1
    #             else:
    #                 answer += str(cnt) + arr[idx-1]
    #             print(idx, arr[idx], answer)



    # while divider <= len(s) / 2:
    #     answer = ""
    #     if len(s) % divider == 0:
    #         print(f"{divider} 로 나눌때")
    #         array = list(map(''.join, zip(*[iter(s)]*divider)))
    #         print(array, len(array))

    #     divider += 1
    # return answer

print(solution(s))