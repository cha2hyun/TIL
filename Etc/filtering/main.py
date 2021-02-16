import sys
import re
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

def getCleanText(original_text):
    pattern = "[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]"
    text = re.sub(pattern, '', original_text)
    return text

def getOriginalText():
    file_path = "./test.txt"
    with open(file_path, mode='rt', encoding='utf-8') as f:
        original_text = f.read()
    return original_text 

def getFilteringList():
    # 추후 파일로 관리
    filtering_list = ["로메인이", "피자"]
    return filtering_list

def getFilteredTextIndex(filtering_list, cleaned_text):
    filtered_text_index = []
    for filter_word in filtering_list:
        print("찾는 단어 :", filter_word)
        for idx, alphabet in enumerate(cleaned_text):
            if filter_word.startswith(alphabet):
                start = idx
                end = idx + len(filter_word) + len(filter_word)
                compare_text = cleaned_text[start:end]
                space_removed_text = compare_text.replace(" ","")
                if filter_word in space_removed_text:
                    end = start + compare_text.find(filter_word[-1])
                    print("   찾음 => ", compare_text, "|", space_removed_text, "| start", start, "| end", end)
                    filtered_text_index.append([start, end])
                    
    return filtered_text_index

def validateFilteredTextIndex(filtered_text_index):
    filtered_text_index.sort()
    dq = deque(filtered_text_index)
    for i in range(len(dq)):
        try:
            if dq[i][1] == dq[i + 1][0]:
                new = [dq[i][0], dq[i+1][1]]
                dq.popleft()
                dq[i] = new
        except:
            pass
    return list(dq)

def printWithColor(original_text, validated_text_index):
    print(validated_text_index)
    # cursor = 0
    # for idx, t in enumerate(original_text):
    #     start = validated_text_index[cursor][0]
    #     end = validated_text_index[cursor][1]
    #     if start <= idx and idx <= end:
    #         cprint(t, 'red', end='')
    #     else:
    #         if idx == end:
    #             cursor += 1
    #         cprint(t, 'white', end='')
    #     print(idx, t, cursor, start, end)

def main():
    original_text = getOriginalText()
    cleaned_text = getCleanText(original_text)
    filtering_list = getFilteringList()
    filtered_text_index = getFilteredTextIndex(filtering_list, cleaned_text)
    validated_text_index = validateFilteredTextIndex(filtered_text_index)
    printWithColor(original_text, validated_text_index)

if __name__ == "__main__":
    main()







# text_temp = text.replace(" ","").replace(",","")
# print("======= 원본 =======")
# print(text)
# print("필터 :", filtering_list)

# cursors = []
# for f in filtering_list:
#     if f in text_temp:
#         cursors.append([text_temp.find(f), text_temp.find(f)+len(f)])
# cursors.sort()
# d_cursors = deque(cursors)
# for i in range(len(d_cursors)):
#     try:
#         if d_cursors[i][1] == d_cursors[i + 1][0]:
#             new = [d_cursors[i][0], d_cursors[i+1][1]]
#             d_cursors.popleft()
#             d_cursors[i] = new
#     except:
#         pass

# cursors = d_cursors

# cursor = 0
# for idx, t in enumerate(text_temp):
#     if idx == 0 :
#         print("======= 변경 =======")
        
#     start = cursors[cursor][0]
#     end = cursors[cursor][1]
#     if idx > end and cursor < len(cursors) - 1:
#         cursor += 1
#     if start <= idx and idx < end:
#         cprint(t, 'red', end='')
#     else:
#         cprint(t, end='')



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

# import sys
# import re
# from termcolor import colored, cprint
# from collections import deque

# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'

#     def disable(self):
#         self.HEADER = ''
#         self.OKBLUE = ''
#         self.OKGREEN = ''
#         self.WARNING = ''
#         self.FAIL = ''
#         self.ENDC = ''

# filtered = ["로메인이"]
# file_path = "./test.txt"
# with open(file_path, mode='rt', encoding='utf-8') as f:
#     text = f.read()

# pattern = "[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]"
# def cleanText(readData):
#     text = re.sub(pattern, '', readData)
#     return text
 
# text = cleanText(text)
# print(text)

# filter_patterns = []
# for filter_word in filtered:
#     filter_pattern = r""
#     for word in filter_word:
#         filter_pattern += word + "[ ]"
#     filter_patterns.append(filter_pattern)

# print(filter_patterns)
# matchOB = re.search(filter_patterns[0], text)
# if matchOB:
#     print("성공")
#     print(matchOB.group())
# else:
#     print("실패")

# print(m.start())
# print(re.findall(filter_patterns[0], text))






# text_temp = text.replace(" ","")
# text_temp = text_temp.sub()
# print("원본 :", text)
# print("필터 :", filtered)

# cursors = []
# for f in filtered:
#     if f in text_temp:
#         cursors.append([text_temp.find(f), text_temp.find(f)+len(f)])
# cursors.sort()
# d_cursors = deque(cursors)
# for i in range(len(d_cursors)):
#     try:
#         if d_cursors[i][1] == d_cursors[i + 1][0]:
#             new = [d_cursors[i][0], d_cursors[i+1][1]]
#             d_cursors.popleft()
#             d_cursors[i] = new
#     except:
#         pass

# cursors = d_cursors

# cursor = 0
# for idx, t in enumerate(text_temp):
#     if idx == 0 :
#         cprint("변경 : ",end='')
#     start = cursors[cursor][0]
#     end = cursors[cursor][1]
#     if idx > end and cursor < len(cursors) - 1:
#         cursor += 1
#     if start <= idx and idx < end:
#         cprint(t, 'red', end='')
#     else:
#         cprint(t, end='')



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

