class Bonus:
    def getMost(self, board):
        # write code here
        l= [[0 for i in range(7)] for j in range(7)]
        for i in range(1,7):
            for j in range(1,7):
                l[i][j]=board[i-1][j-1] + max(l[i-1][j],l[i][j-1])
        return l[6][6]