# Filter out the geese
# https://www.codewars.com/kata/57ee4a67108d3fd9eb0000e7/train/python

# 나의 풀이
def goose_filter(birds):
    return [bird for bird in birds if bird not in ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]]

print(goose_filter(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]),
      ["Mallard", "Hook Bill", "Crested", "Blue Swedish"])
print(goose_filter(["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"]),
      ["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"])
print(goose_filter(["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]),
      [])