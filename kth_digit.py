#User function Template for python3

class Solution:
    def kthDigit(self, A, B, K):
        s=A**B
        dupli=str(s)
        p=len(dupli)
        return dupli[p-K]
    
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B,K = input().split()
        ob = Solution()
        print(ob.kthDigit(int(A),int(B),int(K)))
# } Driver Code Ends