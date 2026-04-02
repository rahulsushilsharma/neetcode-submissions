func longestConsecutive(nums []int) int {

    max := 0
    hash := make(map[int]bool)
    if len(nums) == 0 {
        return 0
    }
    for _,val := range nums {
        hash[val] = true
    }

    for key := range hash {
    
        if  hash[key-1] {
            continue
        }
        cur:= key
        curMax := 0
        for hash[cur] {
            curMax += 1
            cur += 1
        }
        if curMax > max {
            max = curMax
        }
    }
    return max 
    
}
