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


# 원본데이터 가져오기
def getOriginalText():
    file_path = "./test.txt"
    with open(file_path, mode='rt', encoding='utf-8') as f:
        original_text = f.read()
    return original_text 

# 특수문자 제거, 공백 제거
def getCleanText(original_text):
    pattern = "[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]"
    text = re.sub(pattern, '', original_text)
    text = text.replace(" ","").replace("\n", "") # 공백 및 개행문자 제거
    return text

# 필터링할 리스트 가져오기
def getFilteringList():
    # 추후 파일로 관리
    filtering_list = ["로메인이", "피자", "로하스"]
    return filtering_list

def is_filtering_list_in_text(cleaned_text, filtering_list):
    result = []
    for filtered in filtering_list:
        search_text = cleaned_text
        accumulate_idx = 0
        count = 0
        filtered_len = len(filtered)
        while search_text:
            find_idx = search_text.find(filtered)
            if find_idx != -1:
                if count == 0:
                    accumulate_idx += find_idx
                else:
                    accumulate_idx += find_idx + 1
                result += range(accumulate_idx, accumulate_idx+filtered_len)
                search_text = search_text[find_idx+1:] # 계속 앞 부분 잘라주면서
                count += 1
            else:
                break
    result = list(set(result)) # 중복제거
    result.sort(reverse=True) # 순서 재정렬
    return result

# 출력
def printValidatedText(original_text, result):
    print("색칠할 인덱스 범위", result)
    queue = deque(original_text)
    idx = 0
    while queue:
        text = queue.popleft()
        if text.isalpha() or text.isdigit():
            if result:
                result_idx = result.pop()
            if idx == result_idx:
                cprint(text, "red", end="")
            else:
                cprint(text, "white", end="")
                result.append(result_idx)
            idx += 1
        else:
            cprint(text, "white", end="")
        # if not text.isalpha():
        #     cprint(text, "white", end="")

        # else:
        #     result_idx = result.pop()
        #     if idx == result_idx:
        #         cprint(text, "red", end="")
        #         idx += 1
        #     else:
        #         cprint(text, "white", end="")
        #         idx += 1

def main():
    original_text = getOriginalText()
    cleaned_text = getCleanText(original_text)
    filtering_list = getFilteringList()
    result = is_filtering_list_in_text(cleaned_text, filtering_list)
    # filtered_text_index = getFilteredTextIndex(filtering_list, cleaned_text)
    # validated_text_index = validateFilteredTextIndex(filtered_text_index)
    printValidatedText(original_text, result)

if __name__ == "__main__":
    main()

