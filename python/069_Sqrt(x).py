"""
Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.


Example 1:
Input: x = 4
Output: 2

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.

Constraints:

0 <= x <= 2**31 - 1

"""

class Solution:
    #二分搜索法
    def mySqrt(self, x) :
        head = 0 
        tail = x + 1
        while head < tail:
            mid = head + (tail - head) // 2
            if mid ** 2 == x:
                return mid
            elif mid**2 > x :
                tail = mid 
            elif mid**2 < x :
                head = mid + 1
        return tail - 1



if __name__ == 'main':
    sol = Solution()
    print(sol.mySqrt(x=5))
    print(sol.mySqrt(x=50))
