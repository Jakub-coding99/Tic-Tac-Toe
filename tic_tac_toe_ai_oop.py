import random
import os

class TicTacToe:
    def __init__(self):
        self.board =  [x for x in range(1,10)]
        self.winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        self.current_user = "X"
        self.game_is_over = False

    def print_board(self):
        print(
                f"| {self.board[0]} | {self.board[1]} | {self.board[2]} | \n"
                "-------------\n"
                f"| {self.board[3]} | {self.board[4]} | {self.board[5]} | \n"
                "------------\n"
                f"| {self.board[6]} | {self.board[7]} | {self.board[8]} | \n"
                )

    def check_win(self,player):
    
        for combo in self.winning_combinations:
            if all(self.board[pos] == player for pos in combo):
                self.game_is_over = True
                self.print_board()
                print(f"{player} is Winner!")
                
                
                return True
        return False
                
    
    def check_draw(self):
    
        if all(pos in ["X","O"] for pos in self.board):
            self.print_board()
            print("It's a Draw!")
           
            self.game_is_over = True
            return True
        return False
    
    def pc_turn(self):
   
        if self.game_is_over:
            return
    
        def take_random():
            
            free = []
            for moves in self.board:
                if moves != "O" and moves != "X":
                    free.append(moves)
        
            rnd = random.choice(free) -1

            return rnd

        def try_win():
            
            for combo in self.winning_combinations:
                o_count = sum(1 for pos in combo if self.board[pos ] == "O")
                x_count = sum(1 for pos in combo if self.board[pos ] == "X")
                
                if o_count == 2 and x_count == 0:
                    for pos in combo:
                        if self.board[pos] not in ["X", "O"]:
                            self.board[pos] = "O"
                            return True
            return False
        
        def try_block():
            for combo in self.winning_combinations:
                o_count = sum(1 for pos in combo if self.board[pos ] == "O")
                x_count = sum(1 for pos in combo if self.board[pos ] == "X")

                if o_count == 0 and x_count == 2:
                    
                    for pos in combo:
                        if self.board[pos] not in ["X", "O"]:
                            self.board[pos] = "O"
                            return True
            return False

        def take_center():
            if self.board[4] == 5:
                self.board[4] = "O" 
                return True
            return False
            
        def take_corner():
            corner = [0,2,6,8]
            free_corners = [pos for pos in corner if self.board[pos] not in ["X","O"]]
            if free_corners:
                self.board[random.choice(free_corners)] = "O"
                return True
            return False
        
        
        if try_win():
            pass
        
        elif try_block():
            pass
        elif take_center():
            pass
        elif take_corner():
            pass
        
        else:
            free_pos = take_random()
            if free_pos is not None:
                self.board[free_pos] = "O"

        
        if self.check_win("O"):
            
            return
            
        if self.check_draw():
            return
        
        self.current_user = "X"
    
    
    def change_user(self):
        
        if self.game_is_over:
            return
        if self.current_user == "X":
            self.current_user = "O"
            self.pc_turn()
            
        else:
            self.current_user = "X"



    
    
    def restart_game(self):
        while True:
            play = input("Do you want to play a new game? Type 'Y' or 'N': ").lower()
            if play == "y":
                self.game_is_over = False
                os.system('cls' if os.name == 'nt' else 'clear')
                self.board = [x for x in range(1,10)]
                self.current_user = "X"
                self.run_game()
            elif play == "n":
                print("Thank for playing!")
                exit()
            else:
                print("Invalid input. Type 'Y' or 'N': ")

        
    def run_game(self):
        print("Welcome to Tic Tac Toe!")
        self.print_board()
        while self.game_is_over == False:
            
            print(f"{self.current_user} on turn: ")
            try:
                choose = int(input("Type a number of field (1-9) :  ")) 
                if choose < 1 or choose > 9:
                    print("Wrong number. Type correct field number.")
                    continue
                if self.board[choose -1] in ["X","O"]:
                    print("Already taken. Type a number.")
                    continue
                self.board[choose -1] = self.current_user
                
                
                
                if self.check_win("X"):
                    break
                        
                if self.check_draw():
                    break
                self.change_user()
                if self.game_is_over == False:
                    
                    self.print_board()
                
                
                

            except ValueError:
                    print("Wrong number. Type correct field number.")
        self.restart_game()

game = TicTacToe()
game.run_game()