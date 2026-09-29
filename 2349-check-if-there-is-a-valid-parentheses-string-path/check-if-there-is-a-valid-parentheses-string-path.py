class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m,n=len(grid),len(grid[0])
        if (m + n - 1) % 2 != 0:
            return False
        if grid[0][0]==')':
            return False
        visited=set()
        q=deque()
        q.append((0,0,1))
        visited.add((0,0,1))
        while q:
            for k in range(len(q)):
                r,c,b=q.popleft()
                if r==m-1 and c==n-1:
                    if b==0:
                        return True
                for nr,nc in [(r+1,c),(r,c+1)]:
                    if 0<=nr<m and 0<=nc<n:
                        if grid[nr][nc]=='(':
                            nb=b+1
                        else:
                            nb=b-1
                        state=(nr,nc,nb)
                        if nb>=0 and state not in visited:
                            visited.add(state)
                            q.append(state)
        return False


        
