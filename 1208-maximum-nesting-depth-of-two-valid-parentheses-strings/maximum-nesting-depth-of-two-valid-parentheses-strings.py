class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans=[]
        dept=0
        for c in seq:
            if c=='(':
                dept+=1
                ans.append(dept%2)
            else:
                ans.append(dept%2)
                dept-=1
        return ans