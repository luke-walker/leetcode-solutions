// Time Complexity: O(n)
// Auxiliary Space: O(n)

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}

func findDisappearedNumbers(nums []int) []int {
    var res []int

    // mark found values
    for _, v := range nums {
        index := abs(v) - 1

        if nums[index] > 0 {
            nums[index] = -nums[index]
        }
    }

    // determine missing values
    for i, v := range nums {
        if v > 0 {
            res = append(res, i + 1)
        }
    }

    return res
}