# 다른사람 풀이 (쓰택이용)

def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)


# 스택 이용
def solution(number, k):
    num = list(number)
    stack = [num[0]]
    count = 0
    
    for i in range(1, len(num)):
        if count == k:
            stack = stack + num[i:]
            break;

        stack.append(num[i])
        if stack[-1] > stack[-2]:
            while(len(stack) != 1 and stack[-1] > stack[-2] and count < k):                
                stack[-2], stack[-1] = stack[-1], stack[-2]
                stack.pop()
                count += 1

    return "".join(stack[:len(num) -k])

print(solution("1234445", 4))


# def solution1(number, k):
#     collected = []
#     for idx, num in enumerate(number):
#         while len(collected) > 0 and collected[-1] < num and k > 0:
#             collected.pop()
#             k -= 1
#             print(k, collected)
#         if k == 0:
#             collected += list(number[idx:])
#             break
#         collected.append(num)
#         print(collected)
#     print("밖", collected)
#     collected = collected[:-k] if k > 0 else collected
#     print(collected)
#     answer = ''.join(collected)
#     return answer
# print(solution1("543712", 2))

# def solution(number, k):
#     collected = []  # 숫자를 모아서 큰 수를 만들 때 쓰일 배열
#     # 문자열에도 모을 수 있지만 문자열은 immutable(값이 변하지 않는)특성을 가지기에 코드 효율은 리스트(mutable)다 더 좋다
#     # call by value , call by reference와 동일한 개념
#     for i, num in enumerate(number):
#         # k개 만큼의 숫자를 빼냈을 때, i의 인덱스를 기억하기 위해서 i를 사용
#         while len(collected) > 0 and collected[-1] < num and k > 0:
#             # 1. 맨 마지막 문자만 비교를 하면 될까? -> 그렇다. 지금까지 원칙을 지켜서 쌓아 왔다면 지금까지 쌓인 숫자들은 내림차순으로 되어있다.
#             # 2. collected의 마지막 원소는 한 문자로 이루어진 문자열이다. num 또한 한 글자 짜리 문자열이다. 이걸 정수로 변환하지 않고,
#             # 두개의 문자열에 대해서 대소관계를 이용해도 괜찮은가? -> 괜찮다. 알파벳 순서에 따르면 0은 1보다 작고, 3은 2보다 크고, 수의 크기 대소관계와 같다.
#             # ※ 길이가 2 이상이라면, 사전에 나타난 숫자가 되겠지만, 지금은 한글자 짜리기 때문에 정수 변환이 필요없다.
#             collected.pop()  # 리스트이 맨 끝에 있는 원소 하나를 없앤다.
#             k -= 1
#         if k == 0:
#             collected += list(number[i:])
#             break
#         collected.append(num)
#     collected = collected[:-k] if k > 0 else collected
#     # k가 0 이면 빈 리스트가 되기 때문에 if를 이용해서 조건을 걸어준다.
#     answer = ''.join(collected)
#     return answer
    



# def solution(number, k):

#     cnt = len(number) - k

#     start = 0 
#     end = cnt - start
    
#     max_num = []
#     print(cnt, "개 찾아야함")

#     while cnt:        
#         if end - start == len(number):
#             break 
#         if end > len(number) or start > len(number):
#             break
        
#         print(end, start, end-start)
#         print(number[start:end])
#         end += 1
#         start += 1
#         cnt -= 1
#         print("")



# def solution(number, k):
#     start = 0
#     k = len(number) - k
#     answer = ''
#     temp = number[:k]
#     print(number)
#     print(temp)
#     # while cnt:
#     #     cnt -= 1
#     #     try:               
#     #         max_num = max(temp)
#     #         start = temp.index(max_num)
#     #         temp = temp[start+1:]
#     #         answer += max_num
#     #     except:
#     #         print("k=",k)
#     #         print("number=", number)
#     #         answer = number[-k:]
#     #         return answer

#     return answer
        

# print(solution("543789", 4))