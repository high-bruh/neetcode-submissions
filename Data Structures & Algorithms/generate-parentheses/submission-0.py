class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = ['()']

        def inc(arr):
            ans = set()
            n = len(arr[0])
            for ar in arr:
                for i in range(0, n - 1):
                    ans.add(ar[:(i + 1)] + '()' + ar[(i + 1):])
                ans.add('()' + ar)
                ans.add(ar + '()')
            return list(ans)

        for i in range(n - 1):
            res = inc(res)

        return res
