class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        hashmap1 = {}
        hashmap2 = {}
        for word in word1:
            hashmap1[word] = hashmap1.get(word,0) + 1
        for word in word2:
            hashmap2[word] = hashmap2.get(word,0) + 1
        set1 = set(hashmap1.keys())
        set2 = set(hashmap2.keys())
        list1 = sorted(list(hashmap1.values()))
        list2 = sorted(list(hashmap2.values()))
        return True if list1 == list2  and set1 == set2 else False
