
class Solution:
    def isPerfectNumber(self, n):
        sum = 1
        i = 2
        while i * i <= n:
            if n % i == 0:
               sum = sum + i + n/i
            i += 1

        return (1 if sum == n and n!=1 else 0)   
  

if __name__ == '__main__': 
    t = int (input ())