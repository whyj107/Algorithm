# 문제
# 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3

# 나의 풀이
def solution(s):
    answer = len(s)
    for i in range(1, len(s)+1):
        tmp = [s[j:j+i] for j in range(0, len(s), i)]
        n = ''
        cnt = 1
        for j in range(len(tmp)-1):
            if tmp[j] == tmp[j+1]:
                cnt += 1
            else:
                if cnt == 1:
                    cnt = ''
                n += (str(cnt)+str(tmp[j]))
                cnt = 1
        if cnt == 1:
            cnt = ''
        n += (str(cnt) + str(tmp[-1]))
        answer = min(answer, len(n))
    return answer

# 다른 사람의 풀이
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution1(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

if __name__ == '__main__':
    print(solution("aabbaccc"), 7)
    print(solution("ababcdcdababcdcd"), 9)
    print(solution("abcabcdede"), 8)
    print(solution("abcabcabcabcdededededede"), 14)
    print(solution("xababcdcdababcdcd"), 17)