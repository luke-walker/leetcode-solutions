# Time Complexity: O(n)
# Auxiliary Space: O(n)

class Solution:

    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqs = list(Counter(nums).values())
        freq = max(freqs)
        
        return freqs.count(freq)*freq
