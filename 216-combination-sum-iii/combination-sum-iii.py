class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res = []

        def backtrack(i, curr: list, total):
            if len(curr) == k or total > n:
                if total == n:
                    res.append(curr[:])
                return

            for x in range(i, 10):
                if x + total > n:
                    break
                curr.append(x)
                backtrack(x+1, curr, total+x)
                curr.pop()
            return

        backtrack(1, [], 0)
        return res