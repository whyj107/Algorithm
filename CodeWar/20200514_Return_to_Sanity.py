# 문제
# Return to Sanity
# This function should return an object,
# but it's not doing what's intended. What's wrong?

# 입력 == 출력
# Test.assert_equals(mystery(), {'sanity': 'Hello'}, 'Mystery has not returned to sanity')

# My Code
def mystery():
    results = {'sanity': 'Hello'}
    return results

if __name__=='__main__':
    print(mystery())