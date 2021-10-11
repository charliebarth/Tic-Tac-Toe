class TicTacToe:
    win_results = []
    win_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    
    def __init__(self):
        self.board = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def game_start(self):
        turn = 'X'
        
        while not(self.game_over()):
            self.get_board()
            place = int(float(input(f'Enter a position for your {turn}: ')))
            if type(self.board[place]) == int and turn == 'X':
                self.board[place] = 'X'
                turn = 'O'
            elif type(self.board[place]) == int and turn == 'O':
                self.board[place] = 'O'
                turn = 'X'
            else:
                print("The space you tried to select either doesn't exist or is already taken.", "\nPlease Try Again")
        
        self.get_board()
    
    def get_board(self):
        print(
            f'\n{self.board[0]} | {self.board[1]} | {self.board[2]}',
            '\n-- --- --',
            f'\n{self.board[3]} | {self.board[4]} | {self.board[5]}',
            '\n-- --- --',
            f'\n{self.board[6]} | {self.board[7]} | {self.board[8]}'
        )

    def game_over(self): 
        TIE_CONDITION = 9
        result = False
        cnt_tie = 0 
        
        for condition in TicTacToe.win_conditions:
            cnt_x = 0
            cnt_o = 0 
            for i in condition:
                if self.board[i] == 'X':
                    cnt_x += 1
                elif self.board[i] == 'O':
                    cnt_o += 1
            
            if cnt_x == 3:
                print('\nThe winner is X')
                result = True
            elif cnt_o == 3:
                print('\nThe winner is O')
                result = True

        for condition in TicTacToe.win_conditions[:3]:
            for i in condition:
                if self.board[i] == 'X' or self.board[i] == 'O':
                    cnt_tie += 1
           
            if cnt_tie >= TIE_CONDITION:
                print('\nAll the spaces have been used. The game ends in a tie.')
                result = True
        
        return result

game1 = TicTacToe()
game1.game_start()