# 문제
# Metric Units - 1
# Scientists working internationally use metric units almost exclusively.
# Unless that is, they wish to crash multimillion dollars worth of equipment on Mars.
# Your task is to write a simple function that takes a number of meters,
# and outputs it using metric prefixes.
# In practice, meters are only measured in "mm" (thousandths of a meter),
# "cm" (hundredths of a meter), "m" (meters) and "km" (kilometers, or clicks for the US military).
#
# For this exercise we just want units bigger than a meter,
# from meters up to yottameters, excluding decameters and hectometers.

# 입력 == 출력
# Test.assert_equals(meters(1), "1m")
# Test.assert_equals(meters(1000), "1km")
# Test.assert_equals(meters(12300000), "12.3Mm")

# My Code
import math
def meters(x):
    unit = ['m', 'km', 'Mm', 'Gm', 'Tm', 'Pm', 'Em', 'Zm', 'Ym']
    return str(int(x/pow(10, int(math.log10(x))//3*3)) if x/pow(10, int(math.log10(x))//3*3) == int(x/pow(10, int(math.log10(x))//3*3)) else x/pow(10, int(math.log10(x))//3*3))+unit[int(math.log10(x))//3]

# Warriors Code
def meters1(x):
    rank = int(math.log10(x)) / 3
    symbol = ['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']
    return "{0:g}{1}m".format(float(x) / 1000 ** rank, symbol[rank])

if __name__ == '__main__':
    print(meters(1), "1m")
    print(meters(1000), "1km")
    print(meters(12300000), "12.3Mm")