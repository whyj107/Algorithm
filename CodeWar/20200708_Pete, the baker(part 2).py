# 문제
# Pete, the baker (part 2)
# Requirements:
#
# Pete only wants to bake whole cakes.
# And ingredients, that were added once to the mixture, can't be removed from that.
# That means:
# if he already added the amount of flour for 2.8 cakes,
# he needs to add at least the amount of flour for 0.2 cakes,
# in order to have enough flour for 3 cakes.
# If Pete already added all ingredients for an integer amount of cakes,
# you don't need to add anything, just return an empty hash then.
# If Pete didn't add any ingredients at all,
# you need to add all ingredients for exactly one cake.
# For simplicity we ignore all units and just concentrate on the numbers.
# E.g. 250g of flour is simply 250 (units) of flour and 1 lb of sugar is also simply 1 (unit) of sugar.
# Ingredients, which don't have to be added to the mixture (missing amount = 0),
# must not be present in the result.

# 입력 == 출력
# Test.assert_equals(get_missing_ingredients(recipe, {"flour": 100}), {"flour": 100, "eggs": 1, "sugar": 100})
# Test.assert_equals(get_missing_ingredients(recipe, {"flour": 200, "sugar": 100}), {"eggs": 1})
# Test.assert_equals(get_missing_ingredients(recipe, {"flour": 200, "eggs": 1, "sugar": 100}), {})
# Test.assert_equals(get_missing_ingredients(recipe, {"flour": 400, "eggs": 2, "sugar": 200}), {})
# Test.assert_equals(get_missing_ingredients(recipe, {"flour": 1000, "eggs": 5, "sugar": 500}), {})
# Test.assert_equals(get_missing_ingredients(recipe, {"flour": 100}), {"flour": 100, "eggs": 1, "sugar": 100})
# Test.assert_equals(get_missing_ingredients(recipe, {"flour": 200, "sugar": 100}), {"eggs": 1})
# Test.assert_equals(get_missing_ingredients(recipe, {"flour": 200, "eggs": 1, "sugar": 100}), {})
# Test.assert_equals(get_missing_ingredients(recipe, {"flour": 400, "eggs": 2, "sugar": 200}), {})
# Test.assert_equals(get_missing_ingredients(recipe, {"flour": 1000, "eggs": 5, "sugar": 500}), {})
# Test.assert_equals(get_missing_ingredients(recipe, {"flour": 199, "eggs": 1, "sugar": 100}), {"flour": 1})
# Test.assert_equals(get_missing_ingredients(recipe, {"flour": 1, "eggs": 2, "sugar": 200}), {"flour": 399})
# Test.assert_equals(get_missing_ingredients(recipe, {"flour": 123, "eggs": 70}), {"flour": 13877, "sugar": 7000})
# Test.assert_equals(get_missing_ingredients(recipe, {"flour": 199, "eggs": 1, "sugar": 100}), {"flour": 1})
# Test.assert_equals(get_missing_ingredients(recipe, {"flour": 1, "eggs": 2, "sugar": 200}), {"flour": 399})
# Test.assert_equals(get_missing_ingredients(recipe, {"flour": 123, "eggs": 70}), {"flour": 13877, "sugar": 7000})

# My Code
import math
def get_missing_ingredients(recipe, added):
    answer = {}
    n = 1
    for k in added.keys():
        try:
            n = max(n, math.ceil(added[k]/recipe[k]))
        except:
            pass

    for k in recipe.keys():
        try:
            if recipe[k]*n != added[k]:
                answer[k] = recipe[k]*n - added[k]
        except:
            answer[k] = recipe[k]*n
    return answer

# Warriors Code
def get_missing_ingredients1(recipe, added):
    piece = max(math.ceil(v/recipe[k]) if k in recipe else 1 for k,v in added.items())
    return {k:v*piece-added.get(k, 0) for k, v in recipe.items() if (v*piece) > added.get(k, 0)}

if __name__ == '__main__':
    recipe = {'pears': 5, 'milk': 20, 'apples': 10}
    print(get_missing_ingredients(recipe, {'flour': 40, 'sugar': 30}), )
    # print(get_missing_ingredients(recipe, {"flour": 200, "sugar": 100}), {"eggs": 1})

    # print(get_missing_ingredients(recipe, {"flour": 200, "eggs": 1, "sugar": 100}), {})
    # print(get_missing_ingredients(recipe, {"flour": 400, "eggs": 2, "sugar": 200}), {})
    # print(get_missing_ingredients(recipe, {"flour": 1000, "eggs": 5, "sugar": 500}), {})

    # print(get_missing_ingredients(recipe, {"flour": 100}), {"flour": 100, "eggs": 1, "sugar": 100})
    # print(get_missing_ingredients(recipe, {"flour": 200, "sugar": 100}), {"eggs": 1})

    # print(get_missing_ingredients(recipe, {"flour": 200, "eggs": 1, "sugar": 100}), {})
    # print(get_missing_ingredients(recipe, {"flour": 400, "eggs": 2, "sugar": 200}), {})
    # print(get_missing_ingredients(recipe, {"flour": 1000, "eggs": 5, "sugar": 500}), {})

    # print(get_missing_ingredients(recipe, {"flour": 199, "eggs": 1, "sugar": 100}), {"flour": 1})
    # print(get_missing_ingredients(recipe, {"flour": 1, "eggs": 2, "sugar": 200}), {"flour": 399})
    print(get_missing_ingredients(recipe, {"flour": 123, "eggs": 70}), {"flour": 13877, "sugar": 7000})
    # print(get_missing_ingredients(recipe, {"flour": 199, "eggs": 1, "sugar": 100}), {"flour": 1})
    # print(get_missing_ingredients(recipe, {"flour": 1, "eggs": 2, "sugar": 200}), {"flour": 399})
    print(get_missing_ingredients(recipe, {"flour": 123, "eggs": 70}), {"flour": 13877, "sugar": 7000})