class Solution:
    def integerReplacement(self, n: int) -> int:
        if(n == 1):
            return 0
        elif(n == 2):
            return 1
        elif(n == 3):
            return 2

        count = 0
        while(True):

            if(n % 2 == 0):
                n //= 2

            else:

                if(((n - 1)//2) % 2 == 0):
                    n -= 1
                
                else:
                    n += 1

            count += 1

            if(n == 1):
                return count
            elif(n == 3):
                return count + 2