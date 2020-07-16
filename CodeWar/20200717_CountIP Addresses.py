# 문제
# CountIP Addresses

# 나의 풀이
def ips_between(start, end):
    cnt, s, e = 0, 0, 0
    for idx in range(3, -1, -1):
        s += int(start.split('.')[idx]) * (256 ** cnt)
        e += int(end.split('.')[idx]) * (256 ** cnt)
        cnt += 1
    return e - s

# 다른 사람의 풀이
from ipaddress import ip_address
def ips_between1(start, end):
    return int(ip_address(end) - int(ip_address(start)))

if __name__ == '__main__':
    print(ips_between("10.0.0.0", "10.0.0.50"), 50)
    print(ips_between("20.0.0.10", "20.0.1.0"), 246)