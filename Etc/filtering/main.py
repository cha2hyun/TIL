import sys
from termcolor import colored, cprint
from collections import deque

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

filtered = ["피자", "반정", "어간"]
file_path = "./test.txt"
with open(file_path, mode='rt', encoding='utf-8') as f:
    text = f.read()

text_temp = text.replace(" ","").replace(",","")
print("원본 :", text)
print("필터 :", filtered)

cursors = []
for f in filtered:
    if f in text_temp:
        cursors.append([text_temp.find(f), text_temp.find(f)+len(f)])
cursors.sort()
d_cursors = deque(cursors)
for i in range(len(d_cursors)):
    try:
        if d_cursors[i][1] == d_cursors[i + 1][0]:
            new = [d_cursors[i][0], d_cursors[i+1][1]]
            d_cursors.popleft()
            d_cursors[i] = new
    except:
        pass

cursors = d_cursors

cursor = 0
for idx, t in enumerate(text_temp):
    if idx == 0 :
        cprint("변경 : ",end='')
    start = cursors[cursor][0]
    end = cursors[cursor][1]
    if idx > end and cursor < len(cursors) - 1:
        cursor += 1
    if start <= idx and idx < end:
        cprint(t, 'red', end='')
    else:
        cprint(t, end='')



# cprint(text_temp, end='')

# for idx, t in enumerate(text_temp):
#     start = cursors[cursor][0]
#     end = cursors[cursor][1]
#     if idx == 0:
#         cprint("교체 : ", "white", end='')
#     if idx >= start and idx < end:
#         cprint(t, 'red', end='')
#     else:
#         if idx == end and cursor < len(cursors) - 1:
#             cursor += 1
#         cprint(t, 'white', end='')

# print(bcolors.WARNING + text + bcolors.ENDC)

