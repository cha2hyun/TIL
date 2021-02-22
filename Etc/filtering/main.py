import sys
import re
import os.path
from termcolor import colored, cprint
from collections import deque
import colorama

# 원본데이터 가져오기
def get_original_text():
    file_name = input("1. 원고 이름을 작성해주세요 : ")
    file_path = "./article/" + file_name + ".txt"
    if os.path.isfile(file_path):
        try:
            with open(file_path, mode='rt', encoding='utf-8') as f:
                original_text = f.read()
            print("  > 성공적으로 원고를 불러왔습니다. ")
        except:
            print("  > 원고를 불러오지 못했습니다. 원고를 다시 확인해주세요. 원고명은 영문이나 숫자를 추천합니다. ")
            return False
        return original_text 
    else:
        print("  > 종료합니다. 원고 이름을 확인해주세요. ")
        return False
        
# 특수문자와 공백을 제거한다.
def getCleanText(original_text):
    pattern = "[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]"
    text = re.sub(pattern, '', original_text)
    text = text.replace(" ","").replace("\n", "")
    return text

# 필터링할 리스트 가져오기
def get_filtering_list():
    # 추후 파일로 관리
    print("\n2. 필터링할 리스트를 불러옵니다")
    filtering_list = []

    file_path = "./filtering/19.txt"
    if os.path.isfile(file_path):
        try:
            with open(file_path, mode='rt', encoding='utf-8') as f:
                lines = f.readlines()                
                for line in lines:
                    line = line.replace("\n","")
                    filtering_list.append([line, "on_red"])
            print("  > 19금 리스트를", len(lines), "개 불러왔습니다.")
        except:
            print("  > 19금 리스트는 불러오지 못했습니다.")
    
    file_path = "./filtering/advertise.txt"
    if os.path.isfile(file_path):
        try:
            with open(file_path, mode='rt', encoding='utf-8') as f:
                lines = f.readlines()                
                for line in lines:
                    line = line.replace("\n","")
                    filtering_list.append([line, "on_blue"])
            print("  > 과장광고 리스트를", len(lines), "개 불러왔습니다.")
        except:
            print("  > 과장광고 리스트는 불러오지 못했습니다.")
    
    file_path = "./filtering/blacklist.txt"
    if os.path.isfile(file_path):
        try:
            with open(file_path, mode='rt', encoding='utf-8') as f:
                lines = f.readlines()                
                for line in lines:
                    line = line.replace("\n","")
                    filtering_list.append([line, "on_green"])
            print("  > 금칙어 리스트를", len(lines), "개 불러왔습니다.")
        except:
            print("  > 금칙어 리스트는 불러오지 못했습니다.")
    
    return filtering_list

# 필터링 걸리는 문자열 위치와 문자 색상을 리스트로 받아온다
def get_filtering_range(filtering_list, original_text):
    print("\n3. 필터링 결과를 불러옵니다.")
    filtering_range = []
    filtering_result = []
    # print("찾는 단어 :", filtering_list)
    for filter_word, color in filtering_list:
        for cursor, alphabet in enumerate(original_text):
            if filter_word.startswith(alphabet):
                start = cursor
                end = cursor + len(filter_word) + len(filter_word)            
                cleaned_text = getCleanText(original_text[start:end])
                if filter_word in cleaned_text:
                    end = start + original_text[start:end].find(filter_word[-1])
                    filtering_result.append(filter_word)
                    # print("   찾음 => ", filter_word, "|", cleaned_text, "| start", start, "| end", end)
                    filtering_range.append([start, end, color])
    
    filtering_range.sort()
    filtering_result.sort()
    for result in filtering_result:
        print("  >", result, ":", filtering_result.count(result), "개")
        filtering_result.remove(result)
    return filtering_range

# 출력
def print_with_color(original_text, filtering_range):
    # print("색칠할 인덱스 범위", filtering_range)
    cursor = 0
    for idx, alphabet in enumerate(original_text):
        start = filtering_range[cursor][0]
        end = filtering_range[cursor][1]
        on_color = filtering_range[cursor][2]
        if start <= idx and idx < end + 1:
            cprint(alphabet, "grey", on_color, end="")
            if idx == end and cursor < len(filtering_range) - 1: 
                cursor += 1
        else:
            cprint(alphabet, "white", end="")
    print("")

def main():
    print("==== 원고검사기 ====")
    original_text = get_original_text()
    if original_text:
        filtering_range = get_filtering_range(get_filtering_list(), original_text)
        print_or_not = input("\n4. 결과물을 출력하시겠습니까? (y/n) :")
        if print_or_not == "y":
            print("\n")
            print_with_color(original_text, filtering_range)
        else:
            pass

if __name__ == "__main__":
    main()
    colorama.init()
    input("종료하려면 아무 키를 눌러주세요 : ")
