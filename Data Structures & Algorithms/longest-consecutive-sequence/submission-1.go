func longestConsecutive(nums []int) int {

    max := 1
    hash := make(map[int]int)
    if len(nums) == 0 {
        return 0
    }
    for _,val := range nums {
        hash[val] = 1
    }

    for key,_ := range hash {
        _,pre := hash[key-1]
        if pre {
            continue
        }
        cur:= key
        curMax := 1
         _,find := hash[cur]
        for ;find;cur++ {
             _,find = hash[cur]
            curMax += 1
        }
        if curMax > max {
            max = curMax
        }
    }
    return max -2
    
}
