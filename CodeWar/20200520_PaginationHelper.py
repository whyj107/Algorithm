# 문제
# PaginationHelper
# For this exercise you will be strengthening your page-fu mastery.
# You will complete the PaginationHelper class,
# which is a utility class helpful for querying paging information related to an array.
#
# The class is designed to take in an array of values and an integer indicating how many items will be allowed per each page.
# The types of values contained within the collection/array are not relevant.

# 입력 == 출력
# collection = range(1,25)
# helper = PaginationHelper(collection, 10)
#
# Test.assert_equals(helper.page_count(), 3, 'page_count is returning incorrect value.')
# Test.assert_equals(helper.page_index(23), 2, 'page_index returned incorrect value')
# Test.assert_equals(helper.item_count(), 24, 'item_count returned incorrect value')

# My Code
class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        return len(self.collection)

    def page_count(self):
        return self.item_count() // self.items_per_page + 1

    def page_item_count(self, page_index):
        if - 1 < page_index < self.page_count() - 1:
            return self.items_per_page
        elif page_index == self.page_count() - 1:
            return self.item_count() % self.items_per_page
        else:
            return -1

    def page_index(self, item_index):
        if self.item_count() == 0:
            return -1
        if - 1 < item_index < self.items_per_page:
            return 0
        elif self.items_per_page < item_index < self.item_count():
            return item_index // self.items_per_page
        else:
            return - 1

# Warriors Code
class PaginationHelper1:
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        return len(self.collection)

    def page_count(self):
        if len(self.collection) % self.items_per_page == 0:
            return len(self.collection) / self.items_per_page
        else:
            return len(self.collection) / self.items_per_page + 1

    def page_item_count(self, page_index):
        if page_index >= self.page_count():
            return -1
        elif page_index == self.page_count() - 1:
            return len(self.collection) % self.items_per_page or self.items_per_page
        else:
            return self.items_per_page

    def page_index(self, item_index):
        if item_index >= len(self.collection) or item_index < 0:
            return -1
        else:
            return item_index / self.items_per_page

if __name__ == '__main__':
    collection = range(1, 25)
    helper = PaginationHelper(collection, 10)
    # helper = PaginationHelper([], 10)

    # print(helper.page_count(), 3)
    # print(helper.page_index(23), 2)
    # print(helper.item_count(), 24)
    print(helper.page_index(0))