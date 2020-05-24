# 문제
# Populate hash with array keys and default value
# Complete the function so that it takes an array of keys and a default value
# and returns a hash (Ruby) / dictionary (Python) with all keys set to the default value.

# 입력 == 출력
# Test.assert_equals(populate_dict(["draft", "completed"], 0), {"completed": 0, "draft": 0})
# Test.assert_equals(populate_dict(["a", "b", "c"], None), {"c": None, "b": None, "a": None})
# Test.assert_equals(populate_dict([1, 2, 3, 4], "OK"), {1: "OK", 2: "OK", 3: "OK", 4: "OK"})

# My Code
def populate_dict(keys, default):
    answer = {}
    for i in keys:
        answer[i] = default
    return answer

# Warriors Code
def populate_dict1(keys, default):
    return {key: default for key in keys}

if __name__ == '__main__':
    print(populate_dict(["draft", "completed"], 0), {"completed": 0, "draft": 0})
    print(populate_dict(["a", "b", "c"], None), {"c": None, "b": None, "a": None})
    print(populate_dict([1, 2, 3, 4], "OK"), {1: "OK", 2: "OK", 3: "OK", 4: "OK"})