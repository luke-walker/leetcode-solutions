# Time Complexity: O(n*log(n))
# Auxiliary Space: O(n)

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill_sort = sorted(skill)
        target_skill = skill_sort[0] + skill_sort[-1]

        result = 0
        for i in range(n//2):
            if skill_sort[i] + skill_sort[n-i-1] != target_skill:
                return -1
            result += skill_sort[i] * skill_sort[n-i-1]

        return result
