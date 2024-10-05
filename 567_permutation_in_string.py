# Time Complexity: O(m+n)
# Auxiliary Space: O(1)

from string import ascii_lowercase

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)

        count1 = {x: 0 for x in ascii_lowercase}
        count2 = count1.copy()
        matches = 0

        for c in s1:
            count1[c] += 1

        for i in range(n-m+1):
            if i == 0:
                for j in range(m):
                    count2[s2[j]] += 1

                for k, v in count1.items():
                    if v == count2[k]:
                        matches += 1
            else:
                c1 = s2[i-1]
                c2 = s2[i+m-1]
                
                if count1[c1] == count2[c1]:
                    matches -= 1
                elif count1[c1] == count2[c1]-1:
                    matches += 1
                count2[c1] -= 1

                count2[c2] += 1
                if count1[c2] == count2[c2]:
                    matches += 1
                elif count1[c2] == count2[c2]-1:
                    matches -= 1

            if matches == 26:
                return True

        return False
