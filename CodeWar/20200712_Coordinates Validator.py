# 문제
# Coordinates Validator

# My Code
import re
def is_valid_coordinates(coordinates):
    p = re.compile('^(-)?[0-9]+(\.[0-9]+)?')
    coordinates = coordinates.replace(', ', ',')
    l = coordinates.split(',')
    if len(l) != 2:
        return False
    try:
        if abs(float(l[0])) > 90 or p.match(l[0]).group() != l[0]:
            return False

        if abs(float(l[1])) > 180 or p.match(l[1]).group() != l[1]:
            return False
    except:
        return False
    return True

# Warriors Code
def is_valid_coordinates1(coordinates):
    try:
        lat, lng = [abs(float(c)) for c in coordinates.split(',') if 'e' not in c]
    except ValueError:
        return False

    return lat <= 90 and lng <= 180


def is_valid_coordinates2(coordinates):
    return bool(re.match("-?(\d|[1-8]\d|90)\.?\d*, -?(\d|[1-9]\d|1[0-7]\d|180)\.?\d*$", coordinates))

if __name__ == '__main__':
    invalid_coordinates = [
        "-82.0,-30.6"
    ]

    for coordinate in invalid_coordinates:
        print(is_valid_coordinates(coordinate))