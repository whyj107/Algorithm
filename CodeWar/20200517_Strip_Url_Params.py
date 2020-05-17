# 문제
# Strip Url Params
# Complete the method so that it does the following:
# Removes any duplicate query string parameters from the url
# (the first occurence should be kept)
# Removes any query string parameters specified within the 2nd argument (optional array)

# 입력 == 출력
# Test.assert_equals(strip_url_params(url1), url1, "Didn't return correct value when given a url that had nothing to be stripped")
# Test.assert_equals(strip_url_params(url2), url1, "Didn't strip duplicates from url")
# Test.assert_equals(strip_url_params(url2, ['b']), url3, "Didn't strip param that was specified in paramsToStrip array")
# Test.assert_equals(strip_url_params(url4, ['b']), url4, "Didn't return an un-modifed url when there was nothing to strip")
# Test.assert_equals(strip_url_params(url1, ['a', 'b']), url4, "Didn't strip all parameters")

# My Code
def strip_url_params(url, params_to_strip=None):
    url_list = url.split('?')
    if len(url_list) == 2:
        para = url_list[1].split('&')
        pre_idx = list(set([i[:2] for i in para]))
        pre_idx.sort()
        idx = []
        for i in pre_idx:
            for j in para:
                if i in j:
                    idx.append(j)
                    break
        if params_to_strip != None:
            for i in para:
                for j in params_to_strip:
                    if i.count(j) != 0:
                        if i in idx:
                            idx.remove(i)
        if len(idx) != 0:
            return url_list[0] + '?' + '&'.join(idx)
    return url_list[0]

# Warriors Code
def strip_url_params1(url, params_to_strip=""):
    params_to_strip = set(params_to_strip)
    base, _, query = url.partition("?")
    params = []

    if query:
        for param in query.split("&"):
            name, value = param.split("=")
            if name not in params_to_strip:
                params_to_strip.add(name)
                params.append(param)

    return base + ("?" + "&".join(params) if params else "")

if __name__=='__main__':
    url1 = 'www.codewars.com?a=1&b=2'
    url2 = 'www.codewars.com?a=1&b=2&a=1&b=3'
    url3 = 'www.codewars.com?a=1'
    url4 = 'www.codewars.com'
    print(strip_url_params(url2))
    # print(strip_url_params(url2, ['b']))
    # print(strip_url_params(url4, ['b']))
    print(strip_url_params(url1, ['a', 'b']))