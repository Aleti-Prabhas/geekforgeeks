import math
class Solution:
    def gcd(self, n, arr):
        gcd1=math.gcd(arr[0],arr[1])
        for i in range(2,n):
            gcd1=math.gcd(gcd1,arr[i])
            
        return gcd1

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.gcd(n,arr))
