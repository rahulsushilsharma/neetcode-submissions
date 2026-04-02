func normalizeZero(val int) int {
    if val <= 0 {
        return 0
    }
    return val
}

func trap(height []int) int {
    i, j := 0,len(height)-1
    maxl, maxr := 0,0
    sum := 0
    for i<j {
        if height[i] <= height[j] {
            sum = sum + normalizeZero(maxl - height[i])
            if maxl < height[i]{
                maxl = height[i]
            }
            i = i + 1
        }else{
            sum = sum + normalizeZero(maxr - height[j])
            if maxr < height[j] {
                maxr = height[j]
            }
            j = j - 1
        }
    }
    return sum
}

