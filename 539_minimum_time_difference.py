# Time Complexity: O(n*log(n))
# Auxiliary Space: O(n)

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = []
        for point in timePoints:
            hours, minutes = point.split(":")
            times.append(int(hours)*60 + int(minutes))
        times.sort()

        min_time = 1440 - abs(times[0] - times[-1])
        for i in range(len(times) - 1):
            min_time = min(min_time, abs(times[i] - times[i+1]))

        return min_time
