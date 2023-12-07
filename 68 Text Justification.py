### 68. Text Justification
### https://leetcode.com/problems/text-justification/?envType=study-plan-v2&envId=top-interview-150

"""
Runtime | 50 ms
Beats | 52.82%
Memory | 17.7 MB
Beats | 23.38%
"""

class Solution:
    def fullJustify(self, words, maxWidth):
        if len(words) == 1:
            return [words[0]]
        currLine = []
        finalLines = []
        currLineWidth = 0 
        
        for word in words:
            # We are calculating if the selected word length plus the current line length plus the number of line words currently (the number of spaces we need to add at a minimum for words)
            # exceeds the max width allowed. 
            if currLineWidth + len(word) + len(currLine) <= maxWidth:
                currLineWidth += len(word)
                currLine.append(word)
                # We use continue to ignore the rest of the code, as we want to greedily fit as many words into a line as possible
                continue
            
            # Here we start to write the logic to add spacing if the line is only one word long 
            if len(currLine) == 1:
                currLine = " ".join(currLine)
                currLine += " " * (maxWidth - len(currLine))
                finalLines.append(currLine)
            #
            else:
                spacesBetween = (maxWidth - currLineWidth) // (len(currLine) - 1)
                extraSpace = (maxWidth - currLineWidth) % (len(currLine) - 1)
                i = 0
                while extraSpace > 0:
                    currLine[i] += " "
                    extraSpace -= 1
                    i += 1
                finalLines.append(
                    (" " * spacesBetween).join(currLine)
                )
            currLine = [word]
            currLineWidth = len(word)
        currLine = " ".join(currLine)
        currLine += " " * (maxWidth - len(currLine))
        finalLines.append(currLine)
        return finalLines
sol = Solution()
sol.fullJustify(["This", "is", "an", "example", "of", "text", "justification."],16)