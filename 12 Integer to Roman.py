### 12. Integer to Roman
### https://leetcode.com/problems/integer-to-roman/

"""
    Runtime | 121 ms
    Beats | 5.42%
    Memory | 14 MB
    Beats | 24.38%
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        
        romanNumeral = ""
        numberSet = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        symbolSet = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
        i = len(numberSet)-1

        while num: 
            quotient = num // numberSet[i]
            #finding remainder
            num = num % numberSet[i]
            while quotient:
                romanNumeral = romanNumeral + symbolSet[i]
                quotient = quotient - 1
            i -= 1

        return romanNumeral
            
                    
        
        
        
        """
        1632 => 1632 // 1000 => Quo 1 || REM 632
        632 => 632 // 500 => Quo 1 || REM 132
        132 => 132 // 100 => Quo 1 || REM 32
        32 => 32 // 10 => Quo 3 || REM 2
        2 => 2 // 1 => Quo 2 || REM 0
        """