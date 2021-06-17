class Solution:
    def isPerfectNumber(self, n):
        list1=[6,28,496,8128,33550336,8589869056,137438691328,2305843008139952128]
        if(n in list1):
            return 1
        else:
            return 0

   

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.isPerfectNumber(N))
