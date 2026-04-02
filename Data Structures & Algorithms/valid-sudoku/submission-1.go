func isValidSudoku(board [][]byte) bool {
        var row [9][9]int
    var col [9][9]int
    var square [3][3][9] int
    si:= 0
    sj:= 0

    for i := 0 ; i<len(board) ; i ++ {
        
        for j := 0; j < len(board); j ++ {
            num:= board[i][j]-48
           
            if num == 254 {
                
               continue
            }
            si = i/3
            sj = j/3
            
           
           
            if row[i][num-1] != 0 || col[j][num-1] != 0 || square[si][sj][num-1] != 0 {
               
                return false
            }
            row[i][num-1] =  1
            col[j][num-1] = 1
            square[si][sj][num-1] = 1
            
        }
    }

    return true
}


