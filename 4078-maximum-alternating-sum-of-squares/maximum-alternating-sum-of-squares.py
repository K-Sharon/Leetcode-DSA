class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=abs)
        k=len(nums)//2
        return sum(i*i for i in nums[k:])-sum(i*i for i in nums[:k])