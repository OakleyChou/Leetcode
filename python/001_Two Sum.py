"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

#監控記憶體消耗
#from memory_profiler import profile
#def前先@profile
class Solution:
    #最笨的做法->跑兩個for慢慢找
#    def twoSum(self, nums,target):
#        for i in range(len(nums)):
#            right = nums[i+1:]
#            for j in range(len(right)):
#                if nums[i] + right[j] == target :
#                    return [i,i+j+1]
#    
#    #一個for跑第一個,再找target-第一個有沒有在nums裡
#    def twoSum(self, nums, target):
#        for i in range(len(nums)):
#            if target - nums[i] in nums[i+1:]:
#                return [i, (i+1)+nums[i+1:].index(target - nums[i])]
   
    #創建空dict,在裡面找target-nums[i],找不到就把nums:index丟進dict
#    def twoSum(self, nums, target):
#        dic = {}
#        for i in range(len(nums)):
#            if target-nums[i] in dic:
#                return [dic[target-nums[i]], i ]
#            else:
#                dic[nums[i]] = i
    
    #排序後從兩頭開始找
        def twoSum(self, nums, target):
            head,tail = 0, len(nums)-1
            nums_index = [(v,index) for index,v in enumerate(nums)]
            nums_index.sort()
            while head < tail:
                if nums_index[head][0] + nums_index[tail][0] < target: #若sum比target小->代表頭要往後找
                    head += 1
                elif nums_index[head][0] + nums_index[tail][0] > target: #若sum比target大->代表尾要往前找
                    tail -= 1
                else:
                    return [nums_index[head][1], nums_index[tail][1]]
    

if __name__ == '__main__':
    # begin
    s = Solution()
    print( s.twoSum(nums = [2,7,11,15], target = 18))
        
