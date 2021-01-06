# Product ID from URL
# https://www.codewars.com/kata/5e2c7639b5d728001489d910/train/python

# 나의 풀이
def get_product_id(url):
    return url[url.index("p-"):].replace("p-", "").split("-")[-2]

# 다른 사람의 풀이
def get_product_id1(url):
    return url.split('-')[-2]

print(get_product_id("http://www.exampleshop.com/fancy-coffee-cup-p-90764-12052019.html"), "90764")
print(get_product_id("http://www.exampleshop.com/dry-water-just-add-water-to-get-water-p-147-24122017.html"), "147")
print(get_product_id("http://www.exampleshop.com/public-toilet-proximity-radar-p-942312798-01012020.html"), "942312798")