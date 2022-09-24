def solution(v):
    x_arr = [i[0] for i in v]
    y_arr = [i[1] for i in v]
    x = 0
    y = 0
    for dot in v:
        if x_arr.count(dot[0]) != 2:
            x = dot[0]
        if y_arr.count(dot[1]) != 2:
            y = dot[1]

    return [x, y]


v = [[1, 4], [3, 4], [3, 10]]
print(solution(v))
