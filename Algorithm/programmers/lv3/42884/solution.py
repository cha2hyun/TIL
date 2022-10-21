def solution(routes):
    camera = -30001
    # 나간 기준으로 정렬
    routes.sort(key=lambda x: x[1])
    cameraCount = 0
    for route in routes:
        if route[0] > camera:
            cameraCount += 1
            camera = route[1]

    print(routes)
    return cameraCount



print(solution([[-20,-15], [-14,-1], [-18,-13], [-5,-3]]))