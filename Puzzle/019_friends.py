# 친구의 친구는 친구?

# 문제
# 1 ~ N의 합성수에서 7개의 수를 골랐을 때 최대 6단계를 거치게 되는 최소 N을 구해보세요.
# 합성수 : 1과 그 수 자신 이외의 약수를 가지는 자연수

from itertools import permutations

# a ~ f에 들어맞는 소수 6개
# 소수 6개 정도는 쉽게 예측할 수 있으므로 미리 배열에 넣는다. == 하드 코딩
primes = [2, 3, 5, 7, 11, 13]

# 가장 큰 값의 제곱(도출되는 식과 비교하기 위해서 일부러 가장 큰 값을 집어 넣었다.)
min_value = primes[-1] * primes[-1]
min_friend = []
# 6개 요소의 순열
for prime in permutations(primes):
    # 2개씩 선택하여 곱한다.
    # friends = prime.each_cons(2).map{|x, y| x * y}
    friends = [prime[i] * prime[i + 1] for i in range(len(prime) - 1)]
    # 맨 앞과 맨 끝은 같은 수의 제곱
    friends += [prime[0] ** 2, prime[-1] ** 2]
    if min_value > max(friends):
        min_value, min_friend = max(friends), friends

print(min_value)

min_friend.sort()
print(min_friend)