def solution(name):
    make_name = [min(ord(i) - ord("A"), ord("Z") - ord(i)+1) for i in name]
    print(make_name)
    idx, answer = 0, 0
    while True:
        answer += make_name[idx]
        make_name[idx] = 0
        print(make_name)
        if sum(make_name) == 0:
            break
        left, right = 1, 1
        while make_name[idx - left] == 0:
            left +=1
        while make_name[idx + right] == 0:
            right +=1
        answer += left if left < right else right
        idx += -left if left < right else right
    return answer

# def solution(name):
#     alphabet = [ord(alphabet) for alphabet in name]
#     up = [0] * len(alphabet)
#     down = [0] * len(alphabet)
#     left = [0] * len(alphabet)
#     right = [0] * len(alphabet)
#     print(alphabet)
    
#     # A: 65 / Z:90
#     #abcdefghijkl mn opqrstuvwxyz 26개 
#     for idx, char in enumerate(alphabet):
#         if char < 78:
#             up[idx] = (char - 65)
#         else:   
#             down[idx] = (91 - char) 
        
    
#     print("up", up)
#     print("down", down)
#     print("left", left)
#     print("right", right)
#     answer = 0
#     return answer

print(solution("JAZ"))