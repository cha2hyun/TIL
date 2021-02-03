def solution(people, limit):
    answer = len(people)
    peple = sorted(people,reverse = True)
    start, end = 0, len(peple)-1
    while start < end : 
        if peple[start] + peple[end] <= limit :
            end -= 1
            answer -= 1
        start += 1
    return answer


# def solution(people, limit):
#     answer = 0
#     poo = sorted(people)
#     while poo:
#         if len(poo) == 1:
#             answer += 1
#             break
#         if poo[0] + poo[-1] > limit:
#             poo.pop()
#             answer += 1
#         else:
#             poo.pop(0)
#             poo.pop()
#             answer += 1
#     return answer


# def solution(people, limit):
#     people.sort()
#     boat = []
#     print(people)
#     print()
#     for i in range(0, len(people)):
#         print(i,"번쨰", people[i], "랑 비교")
#         if people[i] + people[i+1] > 100:
#             boat.append([people[i]])                 
#             people[i] = 0
        
#         for j in range(i + 1, len(people)):
#             if people[i] + people[j] > 100 :
#                 boat.append([people[i], people[j-1]])
#                 people[i] = 0
#                 people[j-1] = 0 
#                 print(people)
#                 print(boat)
#                 break
#             # print(people[j])
#         print("")
#     print(boat)
#     answer = 0
#     return answer

print(solution([70, 50, 80, 50], 100))