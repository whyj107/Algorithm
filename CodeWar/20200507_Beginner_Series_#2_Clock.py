# 문제
# Clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.
#
# Your task is to make 'Past' function which returns time converted to milliseconds.

# 입력 == 출력
# test.assert_equals(past(0,1,1),61000)
# test.assert_equals(past(1,1,1),3661000)
# test.assert_equals(past(0,0,0),0)
# test.assert_equals(past(1,0,1),3601000)
# test.assert_equals(past(1,0,0),3600000)

# My Code
def past(h, m, s):
    # 초를 밀리초로 변환
    second_to_milli = s * 1000

    # 분을 초로 변환
    minute_to_second = m * 60
    # 분을 밀리초로 변환
    minute_to_milli = minute_to_second * 1000

    # 시를 분으로 변환
    hour_to_minute = h * 60
    # 분을 초로 변환
    hour_to_second = hour_to_minute * 60
    # 초를 밀리초로 변환
    hour_to_milli = hour_to_second * 1000

    return second_to_milli + minute_to_milli + hour_to_milli

    # 한줄로 줄이면 다음과 같다.
    return s*1000 + m * 60 * 1000 + h * 60 * 60 * 1000
    # 이렇게도 가능합니다.
    return (s + (m + h * 60) * 60) * 1000

if __name__=='__main__':
    print(past(0, 1, 1))
    print(past(1, 1, 1))
    print(past(0, 0, 0))
    print(past(1, 0, 1))
    print(past(1, 0, 0))