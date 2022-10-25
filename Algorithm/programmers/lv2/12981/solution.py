
def solution(n, words):
    stack = [words[0]]
    cnt = 0
    for i in range(1, len(words)):
        cnt += 1
        if (words[i] not in stack) and (words[i-1][-1] == words[i][0]):
            stack.append(words[i])
        else:
            return [cnt%n +1, cnt//n + 1]

    return [0, 0]

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(2,["hello", "one", "even", "never", "now", "world", "draw"]))
