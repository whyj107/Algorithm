# Pandas Series 101: Rename Columns
# https://www.codewars.com/kata/5e60cdcd01712200335bd676/train/python

# 나의 풀이
import pandas as pd

def rename_columns(df, names):
    df_ = df.copy()
    df_.columns=[i for idx, i in enumerate(names)]
    return df_

# 다른 사람의 풀이
def rename_columns1(df, names):
    return pd.DataFrame(data=df.values, columns=names)

df_input = pd.DataFrame(data=[[1,2,3], [4,5,6]], columns=list('123'))
names = ('A', 'B', 'C')
df_output = pd.DataFrame(data=[[1,2,3], [4,5,6]], columns=list('ABC'))
user_solution = rename_columns(df_input, names)
if type(user_solution) != type(df_output):
    print(f"You've returned object of {type(user_solution)}. You must return a DataFrame object")

print(user_solution.equals(df_output), f'Wrong output: Expected:\n{df_output}\n\nActual:\n{user_solution}')