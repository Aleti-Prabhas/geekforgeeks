#User function Template for python3

class Solution:
    def isDigitSumPalindrome(self,N):
        sum=0
        while(N>0):
            p=N%10
            sum=sum+p
            N=N//10
        dupli=str(sum)
        dupli2=dupli[::-1]
        if(dupli==dupli2):
            return 1
        else:
            return 0
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.isDigitSumPalindrome(N))
# } Driver Code Ends