from random import randint
from BoardClasses import Move
from BoardClasses import Board
#The following part should be completed by students.
#Students can modify anything except the class name and exisiting functions and varibles.


class StudentAI():

    def __init__(self,col,row,p):
        self.col = col
        self.row = row
        self.p = p
        self.board = Board(col,row,p)
        self.board.initialize_game()
        self.color = ''
        self.opponent = {1:2,2:1}
        self.color = 2

    def get_move(self,move):
        if len(move) != 0:
            self.board.make_move(move,self.opponent[self.color])
        else:
            self.color = 1
        moves = self.board.get_all_possible_moves(self.color)
        chosen_move = self.capture_ai(moves)
        self.board.make_move(chosen_move,self.color)
        return chosen_move

    def capture_ai(self,moves):
        checker_index = randint(0,len(moves)-1)
        checker_move_index = randint(0,len(moves[checker_index])-1)
        c = -1
        for i in moves:
            c += 1
            cm = -1
            for j in i:
                cm += 1
                
                #determine if a piece can be captured by making this move
                #score change is negative if a black piece is captured and positive if a white piece is captured
                before = self.board.white_count - self.board.black_count
                self.board.make_move(j,self.color)
                after = self.board.white_count - self.board.black_count
                score_change = before - after
                self.board.undo()           
                
                #note: score change is negative if a black piece is captured, positive if a white piece is captured, or zero for no capture
                #if you are white and can capture, make that move
                if self.color == 2 and score_change==-1:
                    checker_index = c
                    checker_move_index = cm
                #if you are black and can capture, make that move
                elif self.color == 1 and score_change==1:
                    checker_index = c
                    checker_move_index = cm

        return moves[checker_index][checker_move_index]