# https://leetcode.com/problems/my-calendar-i/


class MyCalendar:
    def __init__(self):
        self.dates = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.dates:
            if start < e and end > s:
                return False
        self.dates.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
