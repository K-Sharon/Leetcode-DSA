class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        dic={n:i for i,n in enumerate(nums)}
        def dsum(x):
            tot=0
            while x:
                tot+=(x%10)
                x//=10
            return tot
        nums.sort()
        nums.sort(key= lambda x:dsum(x))
        res=0
        seen=set()
        for i in range(len(nums)):
            if i in seen: continue
            cnt=0
            e=i
            while e not in seen:
                seen.add(e)
                cnt+=1
                e=dic[nums[e]]
            res+=(cnt-1)
        return res


