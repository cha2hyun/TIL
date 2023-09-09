# 첫번째 답안 - 통과
# def solution(answers):
#     # 배열 = [고유번호, 맞춘답의갯수, 찍는방식]
#     student1 = [1, 0, [1, 2, 3, 4, 5]]
#     student2 = [2, 0, [2, 1, 2, 3, 2, 4, 2, 5]]
#     student3 = [3, 0, [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

#     # 아래를 cycle 로 대체할 수 있음 
#     # from itertools import cycle
#     len_student1 = len(student1[2])
#     len_student2 = len(student2[2])
#     len_student3 = len(student3[2])
#     len_answer = len(answers)
#     for i in range(0, len_answer):
#         if len(student1[2]) < len_answer:
#             add = i % len_student1
#             student1[2].append(student1[2][add])
#         if len(student2[2]) < len_answer:
#             add = i % len_student2
#             student2[2].append(student2[2][add])
#         if len(student3[2]) < len_answer:
#             add = i % len_student3
#             student3[2].append(student3[2][add])
    
#     cnt = 0
#     for answer in answers:        
#         if answer == student1[2][cnt]:
#             student1[1] += 1
#         if answer == student2[2][cnt]:
#             student2[1] += 1
#         if answer == student3[2][cnt]:
#             student3[1] += 1
#         cnt += 1
            
#     winner = []
#     highscore = max(student1[1], student2[1], student3[1])    
#     if highscore == student1[1]:
#         winner.append(student1[0])
#     if highscore == student2[1]:
#         winner.append(student2[0])
#     if highscore == student3[1]:
#         winner.append(student3[0])
    
#     return winner


# 더 깔끔한 답
# def solution(answers):
#     pattern1 = [1,2,3,4,5]
#     pattern2 = [2,1,2,3,2,4,2,5]
#     pattern3 = [3,3,1,1,2,2,4,4,5,5]
#     score = [0, 0, 0]
#     result = []

#     for idx, answer in enumerate(answers):        
#         if answer == pattern1[idx%len(pattern1)]:
#             score[0] += 1
#         if answer == pattern2[idx%len(pattern2)]:
#             score[1] += 1
#         if answer == pattern3[idx%len(pattern3)]:
#             score[2] += 1

#     for idx, s in enumerate(score):
#         if s == max(score):
#             result.append(idx+1)

#     return result



from itertools import cycle

def solution(answers):
    giveups = [
        cycle([1,2,3,4,5]),
        cycle([2,1,2,3,2,4,2,5]),
        cycle([3,3,1,1,2,2,4,4,5,5]),
    ]
    scores = [0, 0, 0]
    for num in answers:
        for i in range(3):
            if next(giveups[i]) == num:
                scores[i] += 1
    highest = max(scores)

    return [i + 1 for i, v in enumerate(scores) if v == highest]


answers = [1,3,2,4,2]
a = solution(answers)
print(a)