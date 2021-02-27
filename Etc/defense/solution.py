def solution(string):
    pass
def main():
    x = input()
    print(x.count("(") == x.count(")") )

# def is_correct_parenthesis(string):
#     dict = {'(':0, ')':0}
#     for s in string:
#         if s == '(':
#             dict['('] += 1
#         else:
#             dict[')'] += 1
#     return dict['('] == dict[')']
    
# def main():
#     x = input()
#     if(2 > len(x) or len(x) > 50):
#         print("문자열의 길이가 범위를 넘어갔습니다.")
#         return 0
#     if is_correct_parenthesis(x):
#         print("YES")
#     else:
#         print("NO")

if __name__=="__main__":
    main()