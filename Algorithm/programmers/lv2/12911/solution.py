from tkinter.tix import Tree


def solution(n):
    cnt = format(n, "b").count("1")
    n += 1
    while True:
        if format(n, "b").count("1") == cnt:
            return n
        n += 1


print(solution(5))
