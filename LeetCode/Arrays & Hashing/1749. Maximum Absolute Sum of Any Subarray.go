func maxAbsoluteSum(nums []int) int {
	res, mn, mx := 0, 0, 0
	for _, num := range nums {
		mx = int(math.Max(float64(mx+num), 0))
		mn = int(math.Min(float64(mn+num), 0))
		res = int(math.Max(float64(res), math.Max(float64(-mn), float64(mx))))
	}
	return res
}
