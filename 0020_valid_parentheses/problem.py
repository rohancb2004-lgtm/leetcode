class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        pairs={
            ")":"(",
            "}":"{",
            "]":"["
        }
        for i in s:
            if i in pairs:
                if not a or a.pop()!=pairs[i]:
                    return False
            else:
                a.append(i)
        return len(a)==0
