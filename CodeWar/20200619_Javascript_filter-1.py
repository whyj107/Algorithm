# 문제
# Javascript filter - 1
# While developing a website, you detect that some of the members have troubles logging in.
# Searching through the code you find that all logins ending with a "_" make problems.
# So you want to write a function that takes an array of pairs of login-names and e-mails,
# and outputs an array of all login-name,
# e-mails-pairs from the login-names that end with "_".

# 입력 == 출력
# a = [[ "foo", "foo@foo.com" ], [ "bar_", "bar@bar.com" ] ]
# b = [ [ "bar_", "bar@bar.com" ] ]
# test.assert_equals(search_names(a), b)
# test.assert_equals(filter_used, True, 'Use filter function' )
#
# a = [[ "foobar_", "foo@foo.com" ], [ "bar_", "bar@bar.com" ] ]
# b = [[ "foobar_", "foo@foo.com" ], [ "bar_", "bar@bar.com" ] ]
# test.assert_equals(search_names(a), b)
# test.assert_equals(filter_used, True, 'Use filter function' )
#
# a = [[ "foo", "foo@foo.com" ], [ "bar", "bar@bar.com" ] ]
# b = []
# test.assert_equals(search_names(a), b)
# test.assert_equals(filter_used, True, 'Use filter function' )

# My Code
def search_names(logins):
    return [i for i in logins if i[0][-1] == '_']

# Warriors Code
def search_names1(logins):
    return(list(filter(lambda s: s[0][-1] == "_", logins)))

if __name__ == '__main__':
    a = [["foo", "foo@foo.com"], ["bar_", "bar@bar.com"]]
    b = [["bar_", "bar@bar.com"]]
    print(search_names(a), b)

    a = [["foobar_", "foo@foo.com"], ["bar_", "bar@bar.com"]]
    b = [["foobar_", "foo@foo.com"], ["bar_", "bar@bar.com"]]
    print(search_names(a), b)

    a = [["foo", "foo@foo.com"], ["bar", "bar@bar.com"]]
    b = []
    print(search_names(a), b)
