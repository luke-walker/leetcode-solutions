// Time Complexity: O(n)
// Auxiliary Space: O(1)

func findLengthOfLCIS(nums []int) int {
    res := 1
    count := 1
    last := nums[0]
    
    for _, v := range nums[1:] {
        if v > last {
            count++
        } else {
            res = max(count, res)
            count = 1
        }

        last = v
    }

    return max(count, res)
}
