func characterReplacement(s string, k int) int {
    
	i,j := 0,0
	max := 0
	hash := make(map [byte]int)
	window := 0
	maxW := 0

	for i < len(s) && j < len(s) {
		curL := s[j]
		curR := s[i]

		hash[curL] = hash[curL] + 1
		if hash[curL] > max {
			max = hash[curL]
		}
		window = j - i  + 1

		if window - max > k {
			hash[curR] = hash[curR] - 1
			i = i + 1
		} 

		window = j - i + 1

		if window > maxW {
			maxW = window
		}
		j = j + 1
	}
	return maxW
}
