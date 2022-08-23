"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 
Constraints:

1 <= prices.length <= 10**5
0 <= prices[i] <= 10**4
"""


class Solution():
#    #每天都計算先前買的利潤,太耗時,time limit Exceeded
#    def maxProfit(self, prices):
#        if len(prices) <= 1:
#            return 0
#        else :
#            profit = []
#            for i in range(len(prices)-1):
#                profit.append(max( [p - prices[i] for p in prices[i+1:]]))
#            if max(profit) <0 :
#                return 0
#            else:
#                return max(profit)
    #只需保存先前最便宜價,最高利潤                     
    def maxProfit(self, prices):
        if not prices or len(prices) < 2:
            return 0
        min_buy = prices[0]
        best_profit = 0
        for i in range(len(prices)):
            if i == 0 :
                continue
            else:
                min_buy = min(min_buy, prices[i])
                best_profit = max(best_profit, prices[i] - min_buy)
        return best_profit


if __name__ == '__main__':
    s = Solution()
    print( s.maxProfit(prices =  [7,1,5,3,6,4]))



