func twoSum(nums []int, skip int, target int, final * [][]int)  {
    i := skip 
    j := len(nums) -1

    for i < j && i>=0 && j <= len(nums) -1 {
        
        sum := nums[i] + nums[j]
        if sum > target {
            j = j -1
        }else if sum < target{
            i = i +1
        }else {
            *final = append(*final,[]int{target * -1, nums[i],nums[j]})
            i = i + 1
            j = j - 1
            for i<j && nums[i-1] == nums[i]{
                i = i + 1
            } 
            for j >i && nums[j+ 1] == nums[j]{
                j = j - 1
            }
        }
    }
    
}

func threeSum(nums []int) [][]int {
    sort.Ints(nums)
    var final [][]int
    for index,val := range nums{
        if index-1 >= 0 && val == nums[index-1]{
            continue
        }
        twoSum(nums,index + 1,0-val,&final)
        
    }
    return final
}


