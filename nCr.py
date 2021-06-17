
import math
class Solution:
    def nCr(self, n, r):
        fac1=math.factorial(n)
        fac2=math.factorial(r)*math.factorial(n-r)
        return math.floor(fac1/fac2)
  

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nCr(n, r))
