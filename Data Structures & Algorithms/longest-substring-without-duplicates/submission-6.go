func lengthOfLongestSubstring(s string) int {
    i, j := 0,0
    hash := make(map[byte]int)
    max := 0
    if len(s) == 0{
        return 0
    }
    sum := 0
    for j < len(s) {
        cur := s[j]
        val, pre := hash[cur]


        if pre && val != -1 {
            for i <= val {
                sum = sum -1
                i = i + 1
            } 
            hash[cur] = -1
        }
            sum = sum + 1 
            hash[cur] = j 
            if sum > max {
                max = sum 
            }
        
        
        j = j + 1
        
    } 
    return max 
}
