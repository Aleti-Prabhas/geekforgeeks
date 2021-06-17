import math
class Solution:
    def lcmAndGcd(self, A , B):
        return (A*B)//math.gcd(A,B),math.gcd(A,B)


import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
