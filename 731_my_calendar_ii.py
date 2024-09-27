# Time Complexity: O(n)
# Auxiliary Space: O(n)

class MyCalendarTwo:
    def __init__(self):
        self.bookings = []
        self.conflicts = []

    def book(self, start: int, end: int) -> bool:
        for c_start, c_end in self.conflicts:
            if start < c_end and end > c_start:
                return False

        for b_start, b_end in self.bookings:
            if start < b_end and end > b_start:
                self.conflicts.append((max(start, b_start), min(end, b_end)))

        self.bookings.append((start, end))
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
