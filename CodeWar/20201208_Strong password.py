# Strong password?
# https://www.codewars.com/kata/57e35f1bc763b8ccce000038/train/python

# 나의 풀이
import re
def check_password(s):
    print(s)
    reg = re.compile(r'^[A-Za-z0-9!@#$%^&*?]{8,20}$')
    spec_reg = re.compile(r'[!@#$%^&*?]+')
    tmp = re.compile(r'[0-9]+')
    pswd_mat = reg.search(s)
    spec_mat = spec_reg.search(s)
    return 'valid' if pswd_mat and spec_mat and tmp else 'not valid'

# 다른 사람의 풀이
def check_password1(s):
    if re.search('^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?\d)(?=.*?[!@#$%^&*?])[a-zA-Z\d!@#$%^&*?]{8,20}$', s) :
        return 'valid'
    else:
        return 'not valid'

PATTERN = re.compile(
'^'                   # begin string
'(?=.*?[A-Z])'        # at least one uppercase letter
'(?=.*?[a-z])'        # at least one lowercase letter
'(?=.*?\d)'           # at least one digit
'(?=.*?[!@#$%^&*?])'  # at least one special character
'[A-Za-z\d!@#$%^&*?]' # only the given characters
'{8,20}'              # between 8 and 20 characters long
'$'                   # end string
)

def check_password2(s):
    return "valid" if PATTERN.match(s) else "not valid"

print(check_password(""), "not valid")
print(check_password("password"), "not valid")
print(check_password("P1@p"), "not valid")
print(check_password("P1@pP1@p"), "valid")
print(check_password("P1@pP1@pP1@pP1@pP1@pP1@p"), "not valid")
print(check_password("Paaaaaa222!!!"), "valid")
