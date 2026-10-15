class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n=len(nums)
        res=0
        for i in range(1,n+1):
            for j in range(n):
                if j+i>n:
                    break
                val=len(set(nums[j:j+i]))
                res+=(val*val)
        return res

        