func lenLongestFibSubseq(arr []int) int {
	longest := 0
	s := make(map[int]bool) 
	for _, num := range arr {
		s[num] = true
	}
	for i := 0; i < len(arr); i++ {
		for j := i + 1; j < len(arr); j++ {
			a, b := arr[i], arr[j]
			count := 2 
			for s[a+b] {
				count++
				a, b = b, a+b
			}
			if count >= 3 { 
				if count > longest {
					longest = count
				}
			}
		}
	}
	return longest
}
