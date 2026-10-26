class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m,n=len(grid),len(grid[0])
        def bfs(i,j):
            summ=grid[i][j]
            q=deque([(i,j)])
            grid[i][j]=0
            while q:
                for _ in range(len(q)):
                    r,c=q.popleft()
                    for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                        if 0<=nr<m and 0<=nc<n and grid[nr][nc]!=0:
                            summ+=grid[nr][nc]
                            grid[nr][nc]=0
                            q.append((nr,nc))
            return summ
        island=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=0:
                    s=bfs(i,j)
                    if s%k==0:
                        island+=1
        return island
        
                    
                            
                            