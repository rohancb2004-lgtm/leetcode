class Solution:
    def fib(self, n: int) -> int:
        mem={}
        def f(x):
            if x in mem:
                return mem[x]
            if x <=1:
                return x
            mem[x]=f(x-1)+f(x-2)
            return mem[x]
        return f(n)