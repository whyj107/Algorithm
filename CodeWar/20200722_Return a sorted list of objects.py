# 문제
# Return a sorted list of objects

# 나의 풀이
def sort_list(sort_by, lst):
    return sorted(lst, key=lambda x: x[sort_by], reverse=True)

# 다른 사람의 풀이
import operator

def sort_list(sort_key, l):
  return sorted(l,key=operator.itemgetter(sort_key), reverse=True)

if __name__ == '__main__':
    print(sort_list("a",
         [
             {"a": 1, "b": 3},
             {"a": 3, "b": 2},
             {"a": 2, "b": 40},
             {"a": 4, "b": 12}
         ])==
        [
           {"a": 4, "b": 12},
           {"a": 3, "b": 2},
           {"a": 2, "b": 40},
           {"a": 1, "b": 3}
        ])