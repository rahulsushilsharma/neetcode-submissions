
func maxArea(heights []int) int {
    max := -1
    for i := 0; i<len(heights); i++ {
        for j := i +1 ; j<len(heights); j ++ {
            water := (j - i ) * int(math.Min(float64(heights[i]),float64(heights[j])))
            if water > max {
                max = water
            }
        }
    }
    return max
}
