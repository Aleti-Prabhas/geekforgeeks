#User function Template for python3

class Solution:
	def binary_to_decimal(self, str):

        sum=0
        i=0
        while(str!=0):
            dec=str%10
            no=no+dec.pow(2,i)
            str=str//10
            i=i+1
		# Code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		str = input()
		ob = Solution()
		ans = ob.binary_to_decimal(str)
		print(ans)
# } Driver Code Ends