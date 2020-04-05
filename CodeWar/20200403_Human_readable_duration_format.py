# 문제
# Your task in order to complete this Kata is to write a function which formats a duration,
# given as a number of seconds, in a human-friendly way.
# The function must accept a non-negative integer. If it is zero, it just returns "now".
# Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

# 입력 == 출력
# test.assert_equals(format_duration(1), "1 second")
# test.assert_equals(format_duration(62), "1 minute and 2 seconds")
# test.assert_equals(format_duration(120), "2 minutes")
# test.assert_equals(format_duration(3600), "1 hour")
# test.assert_equals(format_duration(3662), "1 hour, 1 minute and 2 seconds")

# My Code
def format_duration(seconds):
    y, d, h, m, s, answer = ' year', ' day', ' hour', ' minute', ' second', ''
    # 0일 경우 now 리턴
    if seconds == 0: return 'now'

    # 시간 계산
    minute = seconds // 60
    seconds = seconds % 60

    hour = minute // 60
    minute -= hour * 60

    day = hour // 24
    hour -= day * 24

    year = day // 365
    day -= year * 365

    tmp = [year, y, day, d, hour, h, minute, m, seconds, s]
    answer_list = []

    for i in range(len(tmp)):
        if i % 2 == 0 and tmp[i] != 0:
            # 복수일 경우는 's'를 붙여줘야 한다.
            if tmp[i] > 1:
                tmp[i+1] += 's'
            answer_list.append(str(tmp[i]) + tmp[i+1])

    return (', '.join(answer_list[:-1]) + ' and ' + answer_list[-1] if len(answer_list)>1 else answer_list[0])

# Warriors Code
times = [("year", 365 * 24 * 60 * 60),
         ("day", 24 * 60 * 60),
         ("hour", 60 * 60),
         ("minute", 60),
         ("second", 1)]
def format_duration_(seconds):
    if not seconds:
        return "now"

    chunks = []
    for name, secs in times:
        qty = seconds // secs
        if qty:
            if qty > 1:
                name += "s"
            chunks.append(str(qty) + " " + name)
        seconds = seconds % secs
    return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]

if __name__=='__main__':
    answer = format_duration(1)
    print(answer)
    answer = format_duration(62)
    print(answer)
    answer = format_duration(120)
    print(answer)
    answer = format_duration(3600)
    print(answer)
    answer = format_duration(3662)
    print(answer)