"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.  

Constraints:

1 <= s.length <= 2 * 10**5
s consists only of printable ASCII characters.
"""

class Solution():
    #只保留數字及字母,並全部換成小寫,再看倒過來相不相等
    # def isPalindrome(self, s: str):
    #     s = "".join(filter(str.isalnum, s)).lower()
    #     return s[::-1] == s

    #把特殊情況獨立出來,再逐一檢查從頭開始跟從尾開始是否相等
    def isPalindrome(self, s: str):
        s= ''.join(c for c in s if c.isalnum())
        s=s.lower()
        
        if len(s)==1:
            return True
        if len(s)==0:
            return True
        if len(s)<0:
            return False
        else:
            l=0
            r=len(s)-1
            
            while l<r:
                if s[l]==s[r]:
                    l+=1
                    r-=1
                else:
                    return False
            return True
      
if __name__ == '__main__':
    s = Solution()
    print( s.isPalindrome(s = "A man, a plan, a canal: Panama"))
