#User function Template for python3

class Solution:
    def jumpingNums(self, X):
        for i in range(X,0,-1):
            while(i>0):
                p=i%10
                s=s*10+p
                q=i%100
                r=q//10
                if(p-r==1 or r-p==1):
                    continue
                else:
                    break
            stri=str(s)
            str1=stri[::-1]
            if(str(i)==str1):
                return i
        if(X<)
        # code here 

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        X=int(input())
        
        ob = Solution()
        print(ob.jumpingNums(X))
# } Driver Code Ends