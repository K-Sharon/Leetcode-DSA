from functools import cache
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD=10**9+7
        m,n=len(grid),len(grid[0])
        @cache
        def dfs(i,j,dr):
            if i<0 or i>=m or j<0 or j>=n:
                return 0
            if i==m-1 and j==n-1:
                return 1
            if grid[i][j]==1:
                if dr=='r':
                    return dfs(i+1,j,'d')
                else:
                    return dfs(i,j+1,'r')
            right=dfs(i,j+1,'r')
            down=dfs(i+1,j,'d')
            return (right + down)%MOD
        return dfs(0,0,'r')
    


        