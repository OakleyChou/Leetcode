"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
 
Constraints:

1 <= nums.length <= 3 * 10**4
-3 * 10**4 <= nums[i] <= 3 * 10**4
Each element in the array appears twice except for one element which appears only once.

"""

class Solution():
    """
    ##經典解法,效率高##
    ^ 為XOR
    0 ^ a = a
    a ^ a = 0
    b ^ a ^ a = b
    EX: nums = [2,2,1]
    0 ^ 2 -> 2
    2 ^ 2 -> 0
    0 ^ 1 -> 1
    """
    def singleNumber(nums):
        res = 0
        for i in nums:
            res ^= i
        return res
    
    #依序查找nums,若i出現在list過,則刪除;若沒出現過,則加入
    # def singleNumber(nums):
    #     l = []
    #     for i in nums:
    #         if i in l:
    #             l.remove(i)
    #         else:
    #             l.append(i)
    #     return l[0]

if __name__ == 'main':
    sol = Solution()
    print(sol.singleNumber(nums))

