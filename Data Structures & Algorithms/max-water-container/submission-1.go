
func maxArea(heights []int) int {
    max := -1
    i,j := 0,len(heights)-1
    for i<j {
        sum := (j-i)* int(math.Min(float64(heights[i]), float64( heights[j] )))
        if heights[i]<heights[j] {
            i = i + 1
        }else{
            j = j - 1
        }
        max = int(math.Max(float64(max), float64(sum)))
    }
    return max
}
