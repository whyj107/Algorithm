# 문제
# Did you mean ...?
# I'm sure, you know Google's "Did you mean ...?",
# when you entered a search term and mistyped a word.
# In this kata we want to implement something similar.
#
# You'll get an entered term (lowercase string) and an array of known words (also lowercase strings).
# Your task is to find out, which word from the dictionary is most similar to the entered one.
# The similarity is described by the minimum number of letters you have to add,
# remove or replace in order to get from the entered word to one of the dictionary.
# The lower the number of required changes, the higher the similarity between each two words.
#
# Same words are obviously the most similar ones.
# A word that needs one letter to be changed is more similar to another word that needs 2 (or more) letters to be changed.
# E.g. the mistyped term berr is more similar to beer (1 letter to be replaced)
# than to barrel (3 letters to be changed in total).
#
# Extend the dictionary in a way, that it is able to return you the most similar word from the list of known words.

# Warriors Code
class Dictionary:
    def __init__(self, words):
        self.words = words

    def find_most_similar(self, term):
        answer = []
        for i in self.words:
            grid = [[j for j in range(len(term) + 1)]] + [[e] for e, j in enumerate(i, 1)]
            for e1, j in enumerate(i, 1):
                for e2, k in enumerate(term, 1):
                    if j != k:
                        grid[e1].append(min(grid[e1][e2 - 1], grid[e1 - 1][e2 - 1], grid[e1 - 1][e2]) + 1)
                    elif j == k:
                        grid[e1].append(grid[e1 - 1][e2 - 1])

            answer.append(grid[-1][-1])

        return self.words[answer.index(min(answer))]

if __name__ == '__main__':
    words = ['cherry', 'peach', 'pineapple', 'melon', 'strawberry', 'raspberry',
             'apple', 'coconut', 'banana']
    test_dict = Dictionary(words)
    print(test_dict.find_most_similar('strawbery'), 'strawberry')
    print(test_dict.find_most_similar('berry'), 'cherry')
    print(test_dict.find_most_similar('aple'), 'apple')