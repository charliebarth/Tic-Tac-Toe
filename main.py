class TicTacToe:
    win_results = []
    win_conditions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    
    def __init__(self):
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def game_start(self):
        turn = 'X'
        while not(self.game_over()):
            self.get_board()
            place = int(float(input(f'Enter a position for your {turn}: ')))
            if type(self.board[place - 1]) == int and turn == 'X':
                self.board[place - 1] = 'X'
                turn = 'O'
            elif type(self.board[place - 1]) == int and turn == 'O':
                self.board[place - 1] = 'O'
                turn = 'X'
            else:
                print("The space you tried to select either doesn't exist or is already taken.", "\nPlease Try Again")
    
    def get_board(self):
        print(
            f'{self.board[0]} | {self.board[1]} | {self.board[2]}',
            '\n-- --- --',
            f'\n{self.board[3]} | {self.board[4]} | {self.board[5]}',
            '\n-- --- --',
            f'\n{self.board[6]} | {self.board[7]} | {self.board[8]}'
        )

    def game_over(self): 
        TIE_CONDITION = 9
        cnt_x = 0
        cnt_o = 0 
        cnt_tie = 0 
        winner = 'no one'
        for condition in TicTacToe.win_conditions:
            for i in condition:
                if self.board[i] == 'X':
                    cnt_x += 1
                    cnt_tie += 1
                elif self.board[i] == 'O':
                    cnt_o += 1
                    cnt_tie += 1
            if cnt_x == 3:
                winner = 'The winner is X'
                result = True
            elif cnt_o == 3:
                winner = 'The winner is O'
                result = True
            elif cnt_tie >= TIE_CONDITION:
                winner = 'All the spaces have been used. The game ends in a tie.'
                result = True

game1 = TicTacToe()