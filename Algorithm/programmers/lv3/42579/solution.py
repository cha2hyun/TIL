# def solution(genres, plays):
#     from collections import defaultdict
#     answer = []
#     genres_total = defaultdict(int);
#     genres_songs = defaultdict(lambda: [])                 

#     i = 0
#     for g, p in zip(genres, plays):
#         genres_total[g] += p
#         genres_songs[g].append((i,p))
#         i += 1

#     sorted_genres = sorted(genres_total.items(), key=(lambda x:x[1]), reverse = True)
#     print("genres_songs", genres_songs)
#     for g in sorted_genres:        
#         sorted_g = sorted(genres_songs[g[0]], key=(lambda x: x[1]), reverse=True)        
#         answer.append(sorted_g[0][0])
#         if len(sorted_g) > 1:
#             answer.append(sorted_g[1][0])
    
#     return answer


def solution(genres, plays):
    # 앨범 배열을 play 많은순, 고유번호 낮은순으로 정렬
    album_array = [(genres[i], plays[i], i) for i in range(len(genres))]
    album_array = sorted(album_array, key=lambda x: (x[0], -x[1], x[2]))

    # 앨범 딕셔너리에 저장
    album_dict = {}
    for genre, play, index in album_array:
        if genre not in album_dict.keys():
            album_dict[genre] = [(play, index)]
        else:
            album_dict[genre].append((play, index))

    # 장르별 플레이합을 구하기 위한 배열 선언
    played_total_genre = []        
    for genre in album_dict.keys():
        total = 0
        for play, index in album_dict[genre]:
            total += play
        played_total_genre.append([genre, total])
    # 플레이합 기준으로 정렬
    played_total_genre = sorted(played_total_genre, key=lambda x: x[1], reverse=True)
    
    best_genre = album_dict[played_total_genre[0][0]]
    second_genre = album_dict[played_total_genre[1][0]]
    # 인덱스만 리턴
    return [best_genre[0][1], best_genre[1][1], second_genre[0][1], second_genre[1][1]]
    print(best_genre, second_genre)

    

    # return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))