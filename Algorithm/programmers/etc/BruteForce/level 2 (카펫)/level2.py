def solution(brown, yellow):
    x = (brown + 4 + ((brown + 4) ** 2 - 16 * (brown + yellow)) ** 0.5) / 4
    y = (brown + yellow) // x
    return [max(x,y), min(x,y)]
    
brown = 10
yellow = 2
   
