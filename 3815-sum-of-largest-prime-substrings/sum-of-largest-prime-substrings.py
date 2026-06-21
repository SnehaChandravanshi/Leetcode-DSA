class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:

        def isPrime(n):
            if n <= 1: return False
            elif n <= 3: return True
            elif n % 2 == 0 or n % 3 == 0: return False

            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True

        nums = []
        n = len(s)

        for i in range(n):
            for j in range(i + 1, n + 1):
                num = int(s[i:j])
                if isPrime(num) and num not in nums:
                    heapq.heappush(nums, num)
                    if len(nums) > 3:
                        heapq.heappop(nums)
        return sum(nums)