from tkinter.tix import Tree


def solution(n):
    cnt = format(n, "b").count("1")
    n += 1
    while True:
        n += 1
        if format(n, "b").count("1") == cnt:
            return n


print(solution(5))
