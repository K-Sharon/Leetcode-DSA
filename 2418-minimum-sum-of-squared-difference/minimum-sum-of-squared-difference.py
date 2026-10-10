class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        freq=[0]*100001
        mx=0
        tot=0
        k=k1+k2
        for a,b in zip(nums1,nums2):
            diff=abs(a-b)
            freq[diff]+=1
            tot+=diff
            mx=max(mx,diff)
        if tot<=k:
            return 0
        for i in range(mx,0,-1):
            if k<=0:
                break
            move=min(k,freq[i])
            freq[i]-=move
            freq[i-1]+=move
            k-=move
        ans=0
        for i in range(mx+1):
            ans+=i*i*freq[i]
        return ans

        