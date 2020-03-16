# 문제
# A child is playing with a ball on the nth floor of a tall building.
# The height of this floor, h, is known.
# He drops the ball out of the window.
# The ball bounces (for example), to two-thirds of its height (a bounce of 0.66).
# His mother looks out of a window 1.5 meters from the ground.
# How many times will the mother see the ball pass in front of her window
# (including when it's falling and bouncing?

# Three conditions must be met for a valid experiment:
# Float parameter "h" in meters must be greater than 0
# Float parameter "bounce" must be greater than 0 and less than 1
# Float parameter "window" must be less than h.
# If all three conditions above are fulfilled, return a positive integer, otherwise return -1.
#
# Note:
# The ball can only be seen if the height of the rebounding ball is strictly greater than the window parameter.

# 입력 == 출력
# test.assert_equals(bouncingBall(3, 0.66, 1.5), 3)
# test.assert_equals(bouncingBall(30, 0.66, 1.5), 15)

# --------------------------
# 한 아이가 h 높이에서 공을 창문으로 던질 때 공은 0.66 만큼 튀어오른다.
# 아이의 엄마가 1.5m에서 볼 때 엄마는 공이 지나가는 것을 몇번이나 보는가?
# 이것이 맞는지 모르겠다.
# --------------------------

# My Code
def bouncingBall(h, bounce, window):
    cnt = 0
    if 0 < h and 0 < bounce < 1 and window < h:
        while h > window:
            # 내려갈 때
            cnt += 1
            h *= bounce
            if h > window:
                # 올라갈 때
                cnt += 1
        return cnt
    else:
        return -1

# Warriors Code
def bouncingBall_(h, bounce, window):
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1
    return 2 + bouncingBall(h * bounce, bounce, window)

if __name__=='__main__':
    answer = bouncingBall(3, 0.66, 1.5)
    print(answer)
    answer = bouncingBall(30, 0.66, 1.5)
    print(answer)