"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-2**31 <= x <= 2**31 - 1

"""

class Solution():
    #轉成字串後reverse,判斷是否跟原本的相同
    def isPalindrome(self, x):
        if str(x) == str(x)[::-1]:
            return True
        else :
            return False
    #每次/10取出尾數,再*10,轉成顛倒的數字
#    def isPalindrome(self, x):
#        if x < 0 :
#            return False
#        res = 0
#        y = x
#        while y != 0 :
#            res = res*10 + y % 10
#            y = int(y/10)
#        return x == res

if __name__ == '__main__':
    s = Solution()
    print( s.isPalindrome(x=121) )
