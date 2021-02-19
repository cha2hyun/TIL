import sys
import re
from termcolor import colored, cprint
from collections import deque

# 원본데이터 가져오기
def get_original_text():
    file_path = "./test.txt"
    with open(file_path, mode='rt', encoding='utf-8') as f:
        original_text = f.read()
    return original_text 

# 특수문자와 공백을 제거한다.
def getCleanText(original_text):
    pattern = "[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]"
    text = re.sub(pattern, '', original_text)
    text = text.replace(" ","").replace("\n", "")
    return text

# 필터링할 리스트 가져오기
def get_filtering_list():
    # 추후 파일로 관리
    filtering_list = ["로메", "메인", "피자"]
    return filtering_list

# 필터링 걸리는 문자열 위치와 문자 색상을 리스트로 받아온다
def get_filtering_range(filtering_list, original_text):
    filtering_range = []
    print("찾는 단어 :", filtering_list)
    for filter_word in filtering_list:
        for cursor, alphabet in enumerate(original_text):
            if filter_word.startswith(alphabet):
                start = cursor
                end = cursor + len(filter_word) + len(filter_word)            
                cleaned_text = getCleanText(original_text[start:end])
                if filter_word in cleaned_text:
                    end = start + original_text[start:end].find(filter_word[-1])
                    print("   찾음 => ", filter_word, "|", cleaned_text, "| start", start, "| end", end)
                    filtering_range.append([start, end])
    filtering_range.sort()
    return filtering_range

# 출력
def print_with_color(original_text, validated_filtering_range):
    print("색칠할 인덱스 범위", validated_filtering_range)
    cursor = 0
    for idx, text in enumerate(original_text):
        start = validated_filtering_range[cursor][0]
        end = validated_filtering_range[cursor][1]
        if start <= idx and idx <= end + 1:
            cprint(text, "red", end="")
            if idx == end and cursor < len(validated_filtering_range) - 1: 
                cursor += 1
        else:
            cprint(text, "white", end="")
    print("")

def main():
    original_text = get_original_text()
    filtering_range = get_filtering_range(get_filtering_list(), original_text)
    print_with_color(original_text, filtering_range)

if __name__ == "__main__":
    main()
