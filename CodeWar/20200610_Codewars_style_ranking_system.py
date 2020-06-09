# 문제
# Codewars style ranking system
# Write a class called User that is used to calculate the amount
# that a user will progress through a ranking system similar to the one Codewars uses.

# 자세한 문제는 페이지 참조
# https://www.codewars.com/kata/51fda2d95d6efda45e00004e/train/python

# My Code
class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, n):
        if n > 8 or n < -8 or n == 0:
            raise

        if n == self.rank:
            self.progress += 3
        elif n == self.rank - 1:
            self.progress += 1
        elif n == -1 and n == self.rank - 2:
            self.progress += 1
        elif n > self.rank:
            if n > 0 and self.rank < 0:
                d = n - (self.rank) - 1
            else:
                d = n - self.rank
            self.progress += (10 * d * d)

        if self.rank >= 8:
            self.rank = 8
            self.progress = 0

        while self.progress >= 100:
            self.progress -= 100
            self.rank += 1
            if self.rank == 0:
                self.rank += 1
            elif self.rank >= 8:
                self.rank = 8
                self.progress = 0

# Warriors Code
class User1():
    def __init__(self):
        self.RANKS = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
        self.rank = -8
        self.rank_index = 0
        self.progress = 0

    def inc_progress(self, rank):
        rank_index = self.RANKS.index(rank)

        if rank_index == self.rank_index:
            self.progress += 3
        elif rank_index == self.rank_index - 1:
            self.progress += 1
        elif rank_index > self.rank_index:
            difference = rank_index - self.rank_index
            self.progress += 10 * difference * difference

        while self.progress >= 100:
            self.rank_index += 1
            self.rank = self.RANKS[self.rank_index]
            self.progress -= 100

        if self.rank == 8:
            self.progress = 0
            return

if __name__ == '__main__':
    """
    user = User()
    # print(user.rank, -8)
    # print(user.progress, 0)
    user.inc_progress(-7)
    # rint(user.progress, 10)
    user.inc_progress(-5)
    # print(user.progress, 0)
    # print(user.rank, -7)
    """

    test = User()
    test.inc_progress(-8)
    print(test.rank, test.progress)
    test.inc_progress(-7)
    print(test.rank, test.progress)
    test.inc_progress(-6)
    print(test.rank, test.progress)
    test.inc_progress(-5)
    print(test.rank, test.progress)
    test.inc_progress(-4)
    print(test.rank, test.progress)
    test.inc_progress(-8)
    print(test.rank, test.progress)
    test.inc_progress(1)
    print(test.rank, test.progress)
    test.inc_progress(1)
    print(test.rank, test.progress)
    test.inc_progress(1)
    print(test.rank, test.progress)
    test.inc_progress(1)
    print(test.rank, test.progress)
    test.inc_progress(1)
    print(test.rank, test.progress)
    test.inc_progress(2)
    print(test.rank, test.progress)
    test.inc_progress(2)
    print(test.rank, test.progress)
    test.inc_progress(-1)
    print(test.rank, test.progress)
