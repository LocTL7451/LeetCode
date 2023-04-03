### 2250. Count Number of Rectangles Containing Each Point
### https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/description/

"""
    Runtime | 3642 ms
    Beats | 20%
    Memory | 37.5 MB
    Beats | 80%
"""

class Solution(object):
    def countRectangles(self, rectangles, points):
        from bisect import bisect

        """
        :type rectangles: List[List[int]]
        :type points: List[List[int]]
        :rtype: List[int]
        
        
        Up to 5*10^4 points to map 
        for (x,y):
            1<=x<=10^9
            1<=y<=100

        """
        #Sorting the list of rectangles by the width 
        #rectangles = sorted(rectangles ,key=lambda)
        #rectangles  = rectangles.sort(key = lambda x: x[0])
        rectangles = sorted(rectangles, key=lambda x: x[0])
        storageDict = defaultdict(list)
        for(xcoord, ycoord) in rectangles:
            storageDict[ycoord].append(xcoord)
        def searchFor(xcoord,ycoord):
            counter = 0
            for h, l in storageDict.items():
                if h >= y:
                    counter = counter + len(l) - bisect(l, xcoord-1)
            return counter

        returnArr = []
        for point in points:
            x,y = point
            print(x)
            print(y)
            print(searchFor(x,y))
            returnArr.append(searchFor(x,y))
        return returnArr
    