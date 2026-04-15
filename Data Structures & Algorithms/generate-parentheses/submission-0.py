class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        brackets=[""]*(n*2)
        def solve(index, total,brackets):
            if index >= len(brackets):
                if total == 0:
                    res.append("".join(brackets))
                return
            if total > n:
                return
            elif total < 0 :
                return
            brackets[index]="("
            sum = total+1
            solve(index+1, sum, brackets)
            brackets[index]=")"
            sum = total-1
            solve(index+1, sum, brackets)
        solve(0,0,brackets)
        return res


