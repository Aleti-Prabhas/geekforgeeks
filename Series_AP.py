
class Solution:
    def nthTermOfAP(self,A1,A2,N):
        d=A2-A1
        return A1+(N-1)*d
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        A1,A2,N=map(int,input().strip().split(' '))
        ob=Solution()
        print(ob.nthTermOfAP(A1,A2,N))  
# } Driver Code Ends