class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
            
        L = n.bit_length()
        par = [[0] * n for _ in range(L)]
        dep = [0] * n
        tin, tout, order = [0] * n, [0] * n, []
        stack, t = [(0, -1, 0)], 0

        while stack:
            u, p, state = stack.pop()
            if not state:
                tin[u], t = t, t + 1
                order.append(u)
                par[0][u] = u if p < 0 else p
                stack.append((u, p, 1))
                for v in reversed(g[u]):
                    if v != p:
                        dep[v] = dep[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = t

        for k in range(1, L):
            for u in range(n):
                par[k][u] = par[k-1][par[k-1][u]]

        bit = [0] * (n + 1)

        def add(i, x):
            while i <= n:
                bit[i] ^= x
                i += i & -i

        def pref(i):
            x = 0
            while i:
                x ^= bit[i]
                i -= i & -i
            return x

        def update(u, x):
            add(tin[u] + 1, x)
            if tout[u] < n:
                add(tout[u] + 1, x)

        def lca(u, v):
            if dep[u] < dep[v]:
                u, v = v, u
            d = dep[u] - dep[v]
            for k in range(L):
                if d >> k & 1:
                    u = par[k][u]
            if u == v:
                return u
            for k in range(L-1, -1, -1):
                if par[k][u] != par[k][v]:
                    u, v = par[k][u], par[k][v]
            return par[0][u]

        s = list(s)
        for u in order:
            update(u, 1 << (ord(s[u]) - 97))

        ans = []
        for q in queries:
            p = q.split()
            if p[0] == "update":
                u, c = int(p[1]), p[2]
                update(u, (1 << (ord(s[u])-97)) ^ (1 << (ord(c)-97)))
                s[u] = c
            else:
                u, v = map(int, p[1:])
                w = lca(u, v)
                m = pref(tin[u] + 1) ^ pref(tin[v] + 1)
                m ^= 1 << (ord(s[w]) - 97)
                ans.append(m & (m - 1) == 0)

        return ans