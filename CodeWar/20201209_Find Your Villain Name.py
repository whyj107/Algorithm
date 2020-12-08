# Find Your Villain Name
# https://www.codewars.com/kata/536c00e21da4dc0a0700128b/train/python

# 나의 풀이
def get_villain_name(birthdate):
    first = [ "The Evil", "The Vile", "The Cruel", "The Trashy", "The Despicable", "The Embarrassing",
              "The Disreputable", "The Atrocious", "The Twirling", "The Orange", "The Terrifying", "The Awkward"]
    last = ["Mustache", "Pickle", "Hood Ornament", "Raisin", "Recycling Bin",
            "Potato", "Tomato", "House Cat", "Teaspoon", "Laundry Basket"]
    return f'{first[int(birthdate.month)-1]} {last[int(birthdate.day)%10]}'

import datetime
format_str = '%d/%m/%Y'
print(get_villain_name(datetime.datetime.strptime("1/1/2000", format_str)), "The Evil Pickle")
print(get_villain_name(datetime.datetime.strptime("2/2/2000", format_str)), "The Vile Hood Ornament")
print(get_villain_name(datetime.datetime.strptime("2/12/2000", format_str)), "The Awkward Hood Ornament")