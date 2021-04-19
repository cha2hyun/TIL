import sys
import re
import os.path
from termcolor import colored, cprint
# from collections import deque
# from konlpy.tag import Kkma        
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
        return original_text, file_name
    else:
        print("  > 종료합니다. 원고 이름을 확인해주세요. ")
        return False

        
# 특수문자와 공백을 제거한다.
def getCleanSentence(original_text):
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
                    filtering_list.append([line, "on_red", "19"])
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
                    filtering_list.append([line, "on_blue", "ad"])
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
                    filtering_list.append([line, "on_green", "bl"])
            print("  > 금칙어 리스트를", len(lines), "개 불러왔습니다.")
        except:
            print("  > 금칙어 리스트는 불러오지 못했습니다.")
    
    return filtering_list

# 필터링 걸리는 문자열 위치와 문자 색상을 리스트로 받아온다
def get_filtering_range(original_text, filtering_list):
    print("\n3. 필터링 결과를 불러옵니다.")
    filtering_range = []
    filtering_result = []
    filtering_count = []
    # print("찾는 단어 :", filtering_list)
    for filter_word, color, category in filtering_list:
        for cursor, alphabet in enumerate(original_text):
            if filter_word.startswith(alphabet):
                start = cursor
                end = cursor + (len(filter_word) * 2)
                cleaned_sentence = getCleanSentence(original_text[start:end])
                if filter_word in cleaned_sentence:                
                    reversed_original_text = original_text[start:end][::-1]
                    end = start + reversed_original_text.find(filter_word[-1]) -1                 
                    # print("   찾음 => ", filter_word, "|", category, "|", cleaned_sentence, "| start", start, "| end", end)
                    filtering_result.append([category, filter_word])
                    filtering_count.append(filter_word)
                    filtering_range.append([start, end, color, filter_word, category])
    
    filtering_range.sort()
    filtering_result.sort()
    filtering_results = []

    for category, result in list(set(map(tuple, filtering_result))):
        # print("  >", result, ":", filtering_count.count(result), "개")
        filtering_results.append([result, filtering_count.count(result), category])
    filtering_results = sorted(filtering_results, key = lambda x : x[2], reverse=True)
    bl = 0
    ad = 0
    _19 = 0
    filtering_result_text = ""
    for word, count, category in filtering_results:
        if category == "bl" and (bl == 0):
            # print("==== 블랙리스트 ====")
            filtering_result_text += "==== 블랙리스트 ====\n"
            bl += 1
        if category == "ad" and (ad == 0):
            # print("==== 광고 ====")
            filtering_result_text += "==== 광고 ====\n"
            ad += 1
        if category == "19" and (_19 == 0):
            # print("==== 19 ====")
            filtering_result_text += "==== 19 ====\n"
            _19 += 1
        # print(" >", word, ":", count)
        filtering_result_text += "  > " + str(word) + " : " + str(count) + "\n"
    print(filtering_result_text)    
    return filtering_range, filtering_result_text

# 출력
def print_with_color(original_text, filtering_range):
    # print("색칠할 인덱스 범위", filtering_range)
    print_or_not = input("\n4. 필터링 결과물을 출력하시겠습니까? (y/n) :")
    if print_or_not == "y":
        print("\n")
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
    else:
        print(" > 출력하지 않습니다.")

# 문장 분석
def analysis(original_text):
    analysis_or_not = input("\n5. 결과물을 분석하시겠습니까? (y/n) :")
    analysis_text = ""
    if analysis_or_not == "y":
        print(" > 분석중...")        
        kkma = Kkma()
        # kkma.morphs         #형태소 분석
        # kkma.nouns          #명사 분석
        # kkma.pos            #형태소 분석 태깅
        # kkma.sentences      #문장 분석
        nouns = kkma.nouns(original_text)    
        analysis_data = []
        for noun in nouns:
            matchedList = re.findall(noun, original_text)
            if len(matchedList) > 2 and len(noun) > 1:
                analysis_data.append([noun, len(matchedList)])
        if len(analysis_data) < 2:
            print(" > 중복 검사에 통과하였습니다.")
        else: 
            analysis_data = sorted(analysis_data, key = lambda x : x[1], reverse=True)
            for data, cnt in analysis_data:
                print(" >", data, cnt)
                analysis_text += "  > " + str(data) + " : " + str(cnt) + "\n"
            return analysis_data, analysis_text
    else:
        print(" > 분석하지 않습니다.")

# 파일 저장
def saveAsFile(original_text, filtering_list, file_name, filtering_result_text, analysis_text):
    save_or_not = input("\n6. 결과물을 저장하시겠습니까? (y/n) :")
    if save_or_not == "y":
        print(filtering_result_text)
        marked_text = original_text
        for word, colored, cate in filtering_list:
            marked_text = marked_text.replace(word, "["+word+"]")
        file_path = "./article/" + file_name + "_edited.txt"    
        with open(file_path, mode='w', encoding='utf-8') as f:
            f.write(filtering_result_text)
            f.write("\n==== 단어 반복 검사 결과 (3번 반복 이상) ====\n")
            f.write(analysis_text)
            f.write("\n==== 원고 검사 결과 ====\n")
            for text in marked_text:
                f.write(text) 
        print(" > 저장에 성공하였습니다. 파일 위치 : ", file_path)
    else:
        print(" > 저장하지 않습니다.")

def main():
    print("==== 원고검사기 ====")
    original_text, file_name = get_original_text()
    if original_text:
        filtering_list = get_filtering_list()
        filtering_range, filtering_result_text = get_filtering_range(original_text, filtering_list)
        # print(filtering_range, "\n", filtering_results)
        print_with_color(original_text, filtering_range)
        # analysis_data, analysis_text = analysis(original_text)
        # saveAsFile(original_text, filtering_list, file_name, filtering_result_text, analysis_text)
        saveAsFile(original_text, filtering_list, file_name, filtering_result_text, "단어반복검사 업데이트 준비중")

if __name__ == "__main__":
    colorama.init()
    main()
    input("\n\n종료하려면 아무 키를 눌러주세요 : ")
    