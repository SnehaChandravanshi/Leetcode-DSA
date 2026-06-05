class Solution:
    def numSquares(self, n: int) -> int:
        def is_square(x: int) -> bool:
            r = int(x ** 0.5)
            return r * r == x

        # Case 1: already a perfect square
        if is_square(n):
            return 1

        # Case 2: Legendre form => must be 4
        # Remove all factors of 4 first.
        while n % 4 == 0:
            n //= 4

        # If reduced n is 7 mod 8, answer is forced to be 4.
        if n % 8 == 7:
            return 4

        # Case 3: check if n = a^2 + b^2
        # Only need a up to sqrt(n).
        i = 1
        while i * i <= n:
            if is_square(n - i * i):
                return 2
            i += 1

        # Case 4: if not 1,2,4 then it must be 3
        return 3