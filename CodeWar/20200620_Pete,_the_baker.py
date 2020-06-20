# 문제
# Pete, the baker
# Pete likes to bake some cakes. He has some recipes and ingredients.
# Unfortunately he is not good in maths.
# Can you help him to find out,
# how many cakes he could bake considering his recipes?
#
# Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object)
# and returns the maximum number of cakes Pete can bake (integer).
# For simplicity there are no units for the amounts
# (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200).
# Ingredients that are not present in the objects, can be considered as 0.

# 입력 == 출력
# test.describe('Testing Pete, the Baker')
# test.it('gives us the right number of cakes')
#
# recipe = {"flour": 500, "sugar": 200, "eggs": 1}
# available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
# test.assert_equals(cakes(recipe, available), 2, 'Wrong result for example #1')
#
# recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
# available = {"sugar": 500, "flour": 2000, "milk": 2000}
# test.assert_equals(cakes(recipe, available), 0, 'Wrong result for example #2')

# My Code
def cakes(recipe, available):
    return min([available[key] // value if key in available.keys() else 0 for key, value in recipe.items()])

# Warriors Code
def cakes(recipe, available):
    return min(available.get(k, 0)/recipe[k] for k in recipe)

if __name__ == '__main__':
    recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    print(cakes(recipe, available), 2)

    recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
    available = {"sugar": 500, "flour": 2000, "milk": 2000}
    print(cakes(recipe, available), 0)