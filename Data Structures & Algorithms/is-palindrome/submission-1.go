
func isAlphabet(val rune) bool{
    return !(val<48 || val> 57 && val < 65 || val > 90 &&  val < 97 || val > 122)
}


func isPalindrome(s string) bool {

    i := 0
    j := len(s) -1

    for i<j {
        sv := rune(s[i])
        ev := rune(s[j])
        if unicode.ToLower(sv) != unicode.ToLower(ev) {
            si := isAlphabet(sv)
            sj := isAlphabet(ev)

            if si && sj {
                return false
            }

            if !si {
                i = i + 1
                
            }
            if !sj {
                j = j -1
                
            }
            continue

        }
            
      
        i += 1
        j -= 1
    }
    return true
}
