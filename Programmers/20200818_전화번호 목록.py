# 문제
# 전화번호 목록
# https://programmers.co.kr/learn/courses/30/lessons/42577?language=python3

# 나의 풀이
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)):
        for j in phone_book[i+1:]:
            if j.startswith(phone_book[i]):
                return False
    return True

# 다른 사람의 풀이
def solution1(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

if __name__ == '__main__':
    print(solution(["119", "97674223", "1195524421"]), False)
    print(solution1(["123", "456", "789", "0"]), True)
    print(solution1(["12", "123", "1235", "567", "88"]), False)
    print(solution1(["4321", "432"]), False)