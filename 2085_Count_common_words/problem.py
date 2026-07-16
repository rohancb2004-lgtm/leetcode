class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        a=0
        for i in set(words1):
            c1=0
            c2=0
            for j in words1:
                if i==j:
                    c1+=1
            for j in words2:
                if i==j:
                    c2+=1
            if c1==1 and c2==1:
                a+=1
        return a
                