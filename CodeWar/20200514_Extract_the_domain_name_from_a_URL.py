# 문제
# Extract the domain name from a URL
# Write a function that when given a URL as a string,
# parses out just the domain name and returns it as a string.

# 입력 == 출력
# Test.assert_equals(domain_name("http://google.com"), "google")
# Test.assert_equals(domain_name("http://google.co.jp"), "google")
# Test.assert_equals(domain_name("www.xakep.ru"), "xakep")
# Test.assert_equals(domain_name("https://youtube.com"), "youtube")

# My Code
def domain_name(url):
    tmp = url.replace('http://', '').replace('https://', '').replace('www.', '')
    tmp = tmp.split('.')
    return tmp[0]

def domain_name1(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]

if __name__=='__main__':
    print(domain_name("http://google.com"))
    print(domain_name("http://google.co.jp"))
    print(domain_name("www.xakep.ru"))
    print(domain_name1("https://youtube.com"))