class Solution:
    def getTable(self,n):
        return [n*1,n*2,n*3,n*4,n*5,n*6,n*7,n*8,n*9,n*10]
        
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.getTable(N)
        for i in ans:
            print(i,end=" ")
        print()
# } Driver Code Ends