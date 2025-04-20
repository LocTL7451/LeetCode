### 729. My Calendar I
### https://leetcode.com/problems/my-calendar-i/description/?envType=daily-question&envId=2024-09-26

"""
Runtime | 50 ms
Beats | 52.82%
Memory | 17.7 MB
Beats | 23.38%
"""

class MyCalendar:

    def __init__(self):
        self.currentValidBookings = []

    def book(self, start: int, end: int) -> bool:
        retFlag = True
        if len(self.currentValidBookings) < 1:
            self.currentValidBookings.append([start,end])
        else:
            for booking in self.currentValidBookings:
                if start in range(booking[0],booking[1]) or end-1 in range(booking[0],booking[1]):
                    retFlag = False
                    break
                else:
                    if booking == self.currentValidBookings[-1]:
                        continue
        if retFlag == True:
            self.currentValidBookings.append([start,end])
        return retFlag
        


# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
solArr = [[25,32],[19,25]]
for sol in solArr:
    print(obj.book(sol[0],sol[1]))


            
            