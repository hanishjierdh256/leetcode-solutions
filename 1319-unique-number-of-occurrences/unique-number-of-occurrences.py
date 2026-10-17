class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        hashmap={}
        for num in arr:
            hashmap[num] = hashmap.get(num, 0) + 1
        list1 = list(hashmap.values())
        set1 = set(list1)
        return True if len(list1) == len(set1) else False
