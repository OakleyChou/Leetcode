"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""

class Solution():
    #從長的開始,若不相同就-1長度
#    def longestCommonPrefix(self, strs):
#        if len(strs) == 0:      #若strs是空的,返回''
#            return ''
#        if len(strs) == 1:      #若strs是單一字串,返回該字串
#            return strs[0]
#        max_len = len(strs[0])  #預設第一個字串長度為搜索長度
#        for i in range(1,len(strs)):    
#            max_len = min(max_len , len(strs[i])) 
#            while max_len > 0 and strs[0][0: max_len] != strs[i][0:max_len]: #若目標跟新搜索字串不同,就將目標長度-1,直到找到最大公約數
#                max_len -= 1
#            if max_len == 0: #若最後目標長度=0,返回''
#                return ''
#        return strs[0][0: max_len]
    
    """用第一個當基準,看後續的開頭是不是等於目標word"""
    #faster
    def longestCommonPrefix(self, strs):
        word = strs[0]
        for i in strs:
            while len(word) != 0 and not i.startswith(word):
                word = word[:-1]
        return word




if __name__ == 'main':
    sol = Solution()
    print(sol.longestCommonPrefix(strs = ["flower","flow","flight"]))
    print(sol.longestCommonPrefix(strs = ["dog","racecar","car"]))
