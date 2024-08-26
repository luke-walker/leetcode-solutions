// Time Complexity: O(n)
// Auxiliary Space: O(1)

// Dutch Flag algorithm
func sortColors(nums []int) {
	i := 0
	j := 0
	k := len(nums) - 1

	for j <= k {
		if nums[j] == 0 {
			nums[i], nums[j] = nums[j], nums[i]
			i++
			j++
		} else if nums[j] == 1 {
			j++
		} else { // nums[j] == 2
			nums[j], nums[k] = nums[k], nums[j]
			k--
		}
	}
}