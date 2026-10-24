class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        calendar = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        def convert(s):
            mon=int(s[:2])
            day=int(s[3:])
            return [mon,day]
        sa=convert(arriveAlice)
        la=convert(leaveAlice)
        sb=convert(arriveBob)
        lb=convert(leaveBob)
        arrive=max(sa,sb)
        depart=min(la,lb)
        if arrive>depart:
            return 0
        if arrive[0]==depart[0]:
            return depart[1]-arrive[1]+1
        res=calendar[arrive[0]]-arrive[1]+1
        for i in range(arrive[0]+1,depart[0]):
            res+=calendar[i]
        res+=depart[1]
        return res