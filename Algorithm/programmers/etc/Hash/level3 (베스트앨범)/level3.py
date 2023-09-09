# 1차 코드 정확성 33.3 점
# def solution(genres, plays):
#     from collections import Counter
#     answer = []
#     dic = {}
#     for i in range(len(genres)):
#         dic[i] = [genres[i], plays[i]]
    
#     dic = dict(sorted(dic.items(), reverse=True, key = lambda x : x[1]))
#     max_dic = sorted(dict(zip(genres, plays)).items(), reverse=True, key= lambda x : x[1])

#     for genre, play in max_dic:        
#         count = 0
#         for idx, val in dic.items():
#             if count == 2:                
#                 break;
#             elif genre == val[0]:
#                 answer.append(idx)            
#                 count += 1                        
#     return answer

def solution(genres, plays):
    from collections import defaultdict
    answer = []
    genres_total = defaultdict(int);
    genres_songs = defaultdict(lambda: [])                 

    i = 0
    for g, p in zip(genres, plays):
        genres_total[g] += p
        genres_songs[g].append((i,p))
        i += 1

    sorted_genres = sorted(genres_total.items(), key=(lambda x:x[1]), reverse = True)
    print("genres_songs", genres_songs)
    for g in sorted_genres:        
        sorted_g = sorted(genres_songs[g[0]], key=(lambda x: x[1]), reverse=True)        
        answer.append(sorted_g[0][0])
        if len(sorted_g) > 1:
            answer.append(sorted_g[1][0])
    
    return answer

    


    return answer



genres = ["classic", "pop", "classic", "classic", "pop", "dance", "dance", "dance", "kpop"]
plays = [500, 600, 150, 800, 2500, 400, 100, 150, 100]

test = solution(genres, plays)
print(test)