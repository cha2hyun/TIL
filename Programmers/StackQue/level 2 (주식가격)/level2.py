# 2중 포문
# def solution(prices):
#     answer = []
#     for i in range(len(prices)-1): # 마지막 전까지 ,, 마지막에는 비교할 수 없이 그냥 0이기에
#         count = 0
#         for j in range(i+1, len(prices)): # 마지막까지.
#             if(j == len(prices) - 1 or prices[i] > prices[j]): # 끝날 때 답에 count + 1 해준 값을 넣고 끝낸다.
#                 answer.append(count+1)
#                 break
#             else : 
#                 count +=1
#     answer += [0] # 마지막 요소는 비교할 것도 없이 그냥 내려가고 그런게 없으니 0을 더해줌.
#     return answer

def solution1(prices):
    answer = [0 for _ in range(len(prices))]
    stack = []
    for i in range(len(prices)):
        while len(stack) != 0 and prices[i] < prices[stack[len(stack) -1]]:
            temp = stack.pop()
            answer[temp] = i - temp
        stack.append(i)
    while len(stack):
        temp = stack.pop()
        answer[temp] = len(prices) - temp - 1

    return answer