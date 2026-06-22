class Solution:
    def minArraySum(self, nums: list[int]) -> int:
        MAXV = 100000

        exists = [False] * (MAXV + 1)

        for x in nums:
            exists[x] = True

        ans = 0

        for x in nums:

            best = x

            # find smallest array element dividing x
            d = 1

            while d * d <= x:

                if x % d == 0:

                    # divisor d
                    if exists[d]:
                        best = d
                        break

                    # paired divisor
                    other = x // d

                    if exists[other]:
                        best = min(best, other)

                d += 1

            ans += best

        return ans