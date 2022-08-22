"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2

Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:

1 <= n <= 45
"""


class Solution():
#一次走一or二步:這一步走法=前一步+前兩步走法    
#f(n) = f(n-1)+f(n-2)
#    def climbStairs(self,n: int):
#        pre = cur = 1
#        for i in range(1,n):
#            pre, cur = cur, pre+cur
#        return cur
    #動態紀錄:記憶體耗較小
    def climbStairs(self,n: int):
        if n==0 or n==1 or n==2 :
            return n
        else:
            steps = [1, 1]
            for i in range(2,n+1):
                steps.append(steps[i-1] + steps[i-2])
            return steps[n]
            


if __name__ == 'main':
    sol = Solution()
    print(sol.climbStairs(n=5))
    print(sol.climbStairs(n=50))
