class Solution:
    def isNumber(self, s: str) -> bool:
        if "nan" in s.lower() or "inf" in s.lower():
            return False

        try:
            float(s)
            return True
        except ValueError:
            return False


sol = Solution()

text = input("Enter a value: ")
result = sol.isNumber(text)
print(result)