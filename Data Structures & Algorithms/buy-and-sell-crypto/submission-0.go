func maxProfit(prices []int) int {
    minimum := prices[0]
    maxProfit := 0
    for _,val := range prices {
        profit := val - minimum
        minimum = int(math.Min(float64(minimum),float64(val)))
        maxProfit = int(math.Max(float64(maxProfit),float64(profit)))
    }
    return maxProfit
}
