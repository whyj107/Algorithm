# 문제
# Our football team finished the championship.
# The result of each match look like "x:y".
# Results of all matches are recorded in the collection.
#
# For example: ["3:1", "2:2", "0:1", ...]
#
# Write a function that takes such collection and
# counts the points of our team in the championship.
# Rules for counting points for each match:
# if x>y - 3 points
# if x<y - 0 point
# if x=y - 1 point

# 입력 == 출력
# Test.assert_equals(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']), 30)
# Test.assert_equals(points(['1:1','2:2','3:3','4:4','2:2','3:3','4:4','3:3','4:4','4:4']), 10)
# Test.assert_equals(points(['0:1','0:2','0:3','0:4','1:2','1:3','1:4','2:3','2:4','3:4']), 0)
# Test.assert_equals(points(['1:0','2:0','3:0','4:0','2:1','1:3','1:4','2:3','2:4','3:4']), 15)
# Test.assert_equals(points(['1:0','2:0','3:0','4:4','2:2','3:3','1:4','2:3','2:4','3:4']), 12)

def points(games):
    points = 0
    for i in games:
        print(i)
        tmp = i.split(":")
        if tmp[0] > tmp[1]:
            points += 3
        elif tmp[0] == tmp[1]:
            points += 1
    return points

if __name__=='__main__':
    answer = points(['1:0', '2:0', '3:0', '4:0', '2:1', '3:1', '4:1', '3:2', '4:2', '4:3'])
    print(answer)
    answer = points(['1:1', '2:2', '3:3', '4:4', '2:2', '3:3', '4:4', '3:3', '4:4', '4:4'])
    print(answer)
    answer = points(['0:1', '0:2', '0:3', '0:4', '1:2', '1:3', '1:4', '2:3', '2:4', '3:4'])
    print(answer)
    answer = points(['1:0', '2:0', '3:0', '4:0', '2:1', '1:3', '1:4', '2:3', '2:4', '3:4'])
    print(answer)
    answer = points(['1:0', '2:0', '3:0', '4:4', '2:2', '3:3', '1:4', '2:3', '2:4', '3:4'])
    print(answer)