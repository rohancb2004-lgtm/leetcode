class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #from collections import Counter
        #return Counter(s)==Counter(t)
        def Counter(a):
            freq={}
            for i in a:
                freq[i]=freq.get(i,0)+1
            return freq
        return Counter(s)==Counter(t)
    