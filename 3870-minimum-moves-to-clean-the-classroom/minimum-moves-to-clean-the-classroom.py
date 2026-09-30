class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m,n=len(classroom),len(classroom[0])
        litter=[]
        q=deque()
        visited={}
        for i in range(m):
            for j in range(n):
                if classroom[i][j]=='L':
                    litter.append((i,j))
                elif classroom[i][j]=='S':
                    q.append((0,i,j,0,energy))
                    visited[(i,j,0)]=energy
        target=(1<<len(litter))-1
        if target==0:
            return 0
        while q:
            move,i,j,mask,eng=q.popleft()
            if eng==0:
                continue
                
            for r,c in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
                if 0<=r<m and 0<=c<n and classroom[r][c]!='X':
                    next_eng=eng-1
                    next_mask=mask
                    if classroom[r][c]=='R':
                        next_eng=energy
                    if classroom[r][c]=='L':
                        next_mask |= (1<<litter.index((r,c)))
                    if target==next_mask: 
                        return move+1
                    state=(r,c,next_mask)
                    if state not in visited or visited[state]<next_eng:
                        visited[state]=next_eng
                        q.append((move+1,r,c,next_mask,next_eng))
        return -1
        


