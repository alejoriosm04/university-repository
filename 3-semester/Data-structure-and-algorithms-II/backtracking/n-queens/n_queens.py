class n_queens():
    
    def __init__(self, N):
        self.N = N
        self.chess_board =  [[0 for i in range(N)] for j in range(N)]
        self.solution = 0

    def setQueen(self, row):
        if row == self.N:
            self.solution+=1
            print("Solution: " + str(self.solution))
            self.print_chess_board()
            return
        
        for col in range(self.N):
            if self.validate(row, col):
                self.chess_board[row][col] = 1
                self.setQueen(row+1)
                self.chess_board[row][col] = 0

    def validate(self, row, col):
        for r in range(row):
            if self.chess_board[r][col] == 1: return False

        r = row - 1
        c = col - 1
        while(r >= 0 and c >= 0):
            if self.chess_board[r][c] == 1: return False
            r -= 1
            c -= 1

        r = row - 1
        c = col + 1
        while(r >= 0  and c < self.N):
            if self.chess_board[r][c] == 1: return False
            r -= 1
            c += 1
        
        return True

    def print_chess_board(self):
        for row in range(self.N):
            for col in range(self.N):
                print(self.chess_board[row][col], end=" ")
            print()
        print()


def main():
    chess_board1 = n_queens(8)
    chess_board1.print_chess_board()
    chess_board1.setQueen(0)


if __name__ == '__main__':
    main()