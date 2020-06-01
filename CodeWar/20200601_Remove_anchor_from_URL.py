# 문제
# Remove anchor from URL
# Complete the function/method
# so that it returns the url with anything after the anchor (#) removed.

# 입력 == 출력
# Test.assert_equals(remove_url_anchor("www.codewars.com#about"), "www.codewars.com");
# Test.assert_equals(remove_url_anchor("www.codewars.com/katas/?page=1#about"), "www.codewars.com/katas/?page=1")
# Test.assert_equals(remove_url_anchor("www.codewars.com/katas/"), "www.codewars.com/katas/")

# My Code
def remove_url_anchor(url):
    return url.split('#')[0]

if __name__ == '__main__':
    print(remove_url_anchor("www.codewars.com#about"), "www.codewars.com");
    print(remove_url_anchor("www.codewars.com/katas/?page=1#about"), "www.codewars.com/katas/?page=1")
    print(remove_url_anchor("www.codewars.com/katas/"), "www.codewars.com/katas/")