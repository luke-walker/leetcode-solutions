# Time Complexity: O(n!)
# Auxiliary Space: O(n)

class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        # Heap's Algorithm
        def generate(k, arr):
            if k == 1:
                res.append(arr.copy())
                return
            
            generate(k-1, arr)

            for i in range(k-1):
                if k % 2 == 0:
                    arr[i], arr[k-1] = arr[k-1], arr[i]
                else:
                    arr[0], arr[k-1] = arr[k-1], arr[0]
                
                generate(k-1, arr)

        generate(len(nums), nums.copy())

        return res