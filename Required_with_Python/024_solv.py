# 점수 분포 출력하기
# 조건 01 : 입력된 점수의 끝은 -1로 확인한다.
# 조건 02 : 점수를 10으로 나누어 저장할 점수대의 인덱스를 구한다.

a = [75, 25, 6, 73, 43, 46, 31, 13, 60, 90,
     5, 43, 35, 65, 100, 28, 83, 95, 35, 45, -1]

history = [0]*11

i = 0

while a[i] != -1:
     rank = a[i] // 10
     if rank >= 0 and rank <= 10:
          history[rank] = history[rank] + 1
     i = i + 1

for i in range(len(history)):
     print(f"{i*10} 점대 - : {history[i]} 명")

