def solution(sugar):
    cnt = 0
    while sugar > 0:
        
        # 3키로 짜리 추가
        if sugar % 5 != 0:
            sugar = sugar-3
            if sugar < 0:
                return -1
            cnt = cnt + 1

        # 5키로 짜리 추가
        elif sugar % 5 == 0:
            sugar = sugar - 5
            cnt = cnt + 1

        # 나눌수 없음               
        elif sugar % 5 != 0 and sugar %3 != 0:
            return -1
    return cnt

sugar = int(input())
print(solution(sugar))
    