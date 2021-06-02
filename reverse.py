#User function Template for python3

class Solution:
	def reverse_digit(self, n):
	    s=0
	    while(n>0):
	        p=n%10
	        s=s*10+p
	        n=n//10
	    return s
		# Code here



if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.reverse_digit(n)
		print(ans)
 