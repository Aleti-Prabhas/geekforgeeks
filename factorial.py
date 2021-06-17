import math
class Solution:
    def factorial (self, N):
        return math.factorial(N)
 

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.factorial(N))
