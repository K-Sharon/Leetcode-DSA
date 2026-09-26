class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        hmap={}
        for i in knowledge:
            hmap[i[0]]=i[1]
        res=''
        key=''
        i=0
        while i<len(s):
            if s[i]=='(':
                i+=1
                while s[i]!=')':
                    key+=s[i]
                    i+=1
            if key:
                if key in hmap:
                    res+=hmap[key]
                else:
                    res+='?'
                key=''
            else:
                res+=s[i]
            i+=1
        return res
        