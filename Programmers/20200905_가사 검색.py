# 문제
# 가사 검색
# https://programmers.co.kr/learn/courses/30/lessons/60060?language=python3

class Node(object):
    def __init__(self, key):
        self.key = key
        self.children_cnt = {}
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        node = self.head

        children_cnt = len(string)

        if children_cnt in node.children_cnt:
            node.children_cnt[children_cnt] += 1
        else:
            node.children_cnt[children_cnt] = 1

        for char in string:
            if char not in node.children:
                node.children[char] = Node(char)

            node = node.children[char]
            children_cnt -= 1

            if children_cnt in node.children_cnt:
                node.children_cnt[children_cnt] += 1
            else:
                node.children_cnt[children_cnt] = 1

    def search_count(self, string, q_cnt):
        node = self.head
        for char in string:
            if char in node.children:
                node = node.children[char]
            else: return 0

        if q_cnt in node.children_cnt:
            return node.children_cnt[q_cnt]
        else: return 0


def solution(words, queries):
    t = Trie()
    r_t = Trie()
    for word in words:
        t.insert(word)
        r_t.insert(word[::-1])

    answer = []
    for i in queries:
        query = i
        chars = query.replace("?", "")
        q_cnt = len(query) - len(chars)
        if query[0] == '?':
            answer.append(r_t.search_count(chars[::-1], q_cnt))
        else:
            answer.append(t.search_count(chars, q_cnt))
    return answer

if __name__ == '__main__':
    print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]),
          [3, 2, 4, 1, 0])
