"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

""" 
class Solution():
    #(stack) 使用append,pop的組合，用 list 拼湊出 Queue(先進先出) 與 Stack(先進後出)
    def isValid(self,s):   
        checkdict = {'(':')',
                     '[':']',
                     '{':'}'}  
        stack = [] # append <-> pop(-1) #FILO Last out!!!
        for ele in s:
            if ele in checkdict.keys():
                stack.append(checkdict[ele])
            elif not len(stack)==0 and stack.pop(-1) == ele:
                pass
            else:
                return False
        return len(stack)==0


if __name__ == 'main':
    sol = Solution()
    print(sol.isValid(s = "(){}"))
    print(sol.isValid(s = "({}){]"))
