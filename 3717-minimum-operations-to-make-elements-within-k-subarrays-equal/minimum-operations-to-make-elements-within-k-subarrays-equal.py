
class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        l = SortedList()  
        h = SortedList()  
        ls, hs = 0, 0
        vals = [inf] * n

        for i in range(n):
            if not h or nums[i] >= h[0][0]:
                h.add((nums[i], i))
                hs += nums[i]
            else:
                l.add((nums[i], i))
                ls += nums[i]
            if i >= x:
                val = nums[i - x]
                old_item = (val, i - x)
                if old_item in l:
                    l.remove(old_item)
                    ls -= val
                else:
                    h.remove(old_item)
                    hs -= val
            while len(h) > len(l) + 1:
                val, idx = h.pop(0)  
                hs -= val
                l.add((val, idx))
                ls += val
            while len(h) < len(l):
                val, idx = l.pop()   
                ls -= val
                h.add((val, idx))
                hs += val
            if i >= x - 1:
                median = h[0][0]
                vals[i] = (len(l) * median - ls) + (hs - len(h) * median)
                
        dp = [[inf] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            dp[i][0] = 0
            for j in range(1, k + 1):
                dp[i][j] = dp[i-1][j]
                if i >= x and vals[i-1] != inf:
                    dp[i][j] = min(dp[i][j], vals[i-1] + dp[i-x][j-1])
                    
        return dp[n][k] if dp[n][k] != inf else -1