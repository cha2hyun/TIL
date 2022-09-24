def solution(routes):
    print(routes)
    routes.sort()
    print(routes)
    answer = 0
    return answer


routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes))
# return -> 2 // (-5, -15)