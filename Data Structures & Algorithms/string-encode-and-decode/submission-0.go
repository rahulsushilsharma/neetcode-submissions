
type Solution struct{}

func (s *Solution) Encode(strs []string) string {
    var enc string
    for  _,val := range strs {
        enc = enc + "<><>" + val 
    }
    return enc
}

func (s *Solution) Decode(encoded string) []string {
    sol := strings.Split(encoded, "<><>")
    return sol[1:]
}
