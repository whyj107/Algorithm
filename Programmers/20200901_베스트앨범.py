# 문제
# 베스트앨범
# https://programmers.co.kr/learn/courses/30/lessons/42579?language=python3

# 나의 풀이
def solution(genres, plays):
    music = {}
    music_total_play = {}
    for i in range(len(genres)):
        if not genres[i] in music.keys():
            music[genres[i]] = [(-plays[i], i)]
            music_total_play[genres[i]] = plays[i]
        else:
            music[genres[i]] += [(-plays[i], i)]
            music_total_play[genres[i]] += plays[i]
    sorted_m_t = sorted(music_total_play.items(), key=lambda i: i[1], reverse=True)
    answer = []
    for k in sorted_m_t:
        sorted_m = sorted(music[k[0]], key=lambda x : (x[0], x[1]))
        answer.append(sorted_m[0][1])
        if len(sorted_m) > 1:
            answer.append(sorted_m[1][1])
    return answer

if __name__=='__main__':
    print(solution(["classic", "pop", "classic", "classic", "pop"],
                    [500, 600, 150, 800, 2500]), [4, 1, 3, 0])