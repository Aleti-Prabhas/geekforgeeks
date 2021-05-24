class Solution:
	def Nth_term(self, a, r, n):
        w = n-1
        p=r**w
        return  a*p
		# Code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		a, r, n = input().split()
		a = int(a)
		r = int(r)
		n = int(n)
		ob = Solution()
		ans = ob.Nth_term(a, r, n)
		print(ans)
# } Driver Code Ends