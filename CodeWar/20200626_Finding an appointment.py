# 문제
# Finding an appointment
# The businesspeople among you will know that it's often not easy to find an appointment.
# In this kata we want to find such an appointment automatically.
# You will be given the calendars of our businessperson and a duration for the meeting.
# Your task is to find the earliest time,
# when every businessperson is free for at least that duration.
# Rules:
# All times in the calendars will be given in 24h format "hh:mm",
# the result must also be in that format
# A meeting is represented by its start time (inclusively) and end time (exclusively)
# -> if a meeting takes place from 09:00 - 11:00, the next possible start time would be 11:00
# The businesspeople work from 09:00 (inclusively) - 19:00 (exclusively),
# the appointment must start and end within that range
# If the meeting does not fit into the schedules, return null or None as result
# The duration of the meeting will be provided as an integer in minutes

# 입력 == 출력
# schedules = [
#   [['09:00', '11:30'], ['13:30', '16:00'], ['16:00', '17:30'], ['17:45', '19:00']],
#   [['09:15', '12:00'], ['14:00', '16:30'], ['17:00', '17:30']],
#   [['11:30', '12:15'], ['15:00', '16:30'], ['17:45', '19:00']]
# ]
# test.assert_equals(get_start_time(schedules, 60), '12:15')
# test.assert_equals(get_start_time(schedules, 90), None)

def mins(timeStr):
    h, m = map(int, timeStr.split(':'))
    return h * 60 + m

def get_start_time(schedules, duration):
    # 일정이 있는 값들을 모두 합치고 정렬한다.
    # 19:00 ~ 19:00 을 추가하여 끝을 맞춘다.
    periods = sorted(sum(schedules, [['19:00', '19:00']]))
    # 처음 시작 시간 변수 설정
    time = '09:00'
    for period in periods:
        # 일정의 시작값과 처음 시작 시간 + duration 값을 비교하여 크거나 같을 경우만 값을 반환한다.
        # 시간 계산은 분으로 한다. 이를 위해 mins라는 함수가 필요하다.
        if mins(period[0]) >= mins(time) + duration:
            return time
        # 시작 시간에 끝시간과 시작시간을 비교하여 큰 값을 넣는다.
        time = max(time, period[1])
    return None

if __name__ == '__main__':
    schedules = [
        [['09:00', '11:30'], ['13:30', '16:00'], ['16:00', '17:30'], ['17:45', '19:00']],
        [['09:15', '12:00'], ['14:00', '16:30'], ['17:00', '17:30']],
        [['11:30', '12:15'], ['15:00', '16:30'], ['17:45', '19:00']]
    ]
    # print(get_start_time(schedules, 60), '12:15')
    print(get_start_time(schedules, 90), None)