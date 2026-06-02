class Solution:
    def isNumber(self, s: str) -> bool:
        valid_digit = False
        seen_dot = False
        seen_e = False
        valid_dot = False
        for i in range(len(s)):
            char = s[i]

            if char in ('.'):
                    
                if seen_dot or seen_e:
                    return False
                seen_dot = True
                    

            elif char.isdigit():
                seen_digit = True
                valid_digit = True
                if seen_dot and seen_digit:
                    valid_digit = True
            
                
            elif char in ('+','-'):
                if i > 0 and s[i - 1] not in ('e','E'):
            
                    return False
                
                    
            elif char in ('e','E'):
                
                if seen_e or not valid_digit:
                    return False
                seen_e = True
                valid_digit = False# cannot be invalid after e (no dot after e)

            else:
                return False
        return valid_digit

            