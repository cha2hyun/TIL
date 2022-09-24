def solution(phone_book): 
    answer = True 
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1]:
            answer = False
            return answer
    return answer



phone_book = ["123","456","789"]
a = solution(phone_book)
print(a)


# def solution(phoneBook):
#     phoneBook = sorted(phoneBook)

#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         if p2.startswith(p1):
#             return False
#     return True

# def solution(phone_book): 
#     for i in range(len(phone_book)): 
#         pivot = phone_book[i] 
#         for j in range(i+1, len(phone_book)):
#             strlen = min(len(pivot), len(phone_book[j])) 
#             if pivot[:strlen] == phone_book[j][:strlen]: 
#                 return False 
#     return True


