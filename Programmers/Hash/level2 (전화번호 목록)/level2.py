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

# p = "123"
# q = "124312534123"

# if p in q:
#     print("yes")
# else:
#     print("no")
