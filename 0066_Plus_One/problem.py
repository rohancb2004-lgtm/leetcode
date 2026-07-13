class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        car=1
        for i in range(len(digits)-1,-1,-1):
            if car==1:
                digits[i]+=1
            car=digits[i]//10 
            digits[i]%=10 
            if car==0:
                return digits  
        if car==1:
            digits.insert(0,car)
        return digits