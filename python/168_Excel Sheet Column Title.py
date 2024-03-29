"""
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

Example 1:
Input: columnNumber = 1
Output: "A"

Example 2:
Input: columnNumber = 28
Output: "AB"

Example 3:
Input: columnNumber = 701
Output: "ZY"

Constraints:
1 <= columnNumber <= 2**31 - 1

"""

class Solution():
    #從最後一位開始找
    def convertToTitle(self,columnNumber: int):
        string = ''
        while columnNumber > 0:    
            columnNumber -= 1
            string = chr(65 + columnNumber % 26) + string
            columnNumber = columnNumber // 26
        return string

if __name__ == '__main__':
    s = Solution()
    print( s.convertToTitle(columnNumber = 701 ))
