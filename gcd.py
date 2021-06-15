
import math
class Solution:
    def gcd(self, A, B):
        return math.gcd(A,B)
        



if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        A,B = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.gcd(A,B))