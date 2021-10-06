import tkinter as tk
from tkinter import *
#from PIL import ImageTk

class Layout(tk.Tk):
    
    def __init__(self, n=8):
        super().__init__() #Base class __init__ func 
        self.n = n #Number of Files and Ranks
        self.scale = 60
        self.board = [[None for row in range(n)] for col in range(n)]
        self.canvas = tk.Canvas(self, width=640, height=480)
        self.canvas.grid(row=0, column=0, columnspan=8, rowspan=8)
           
        self.chessPiecesWhite = {
            'Queen' : 'Images/White/Chess_qlt60.png',
            'King' : 'Images/White/Chess_klt60.png',
            'Knight' : 'Images/White/Chess_nlt60.png',
            'Pawn' : 'Images/White/Ches_plt60.png',
            'Rook' : 'Images/White/Chess_rlt60.png',
            'Bishop' : 'Images/White/Chess_blt60.png'
        }

        self.chessPiecesBlack = {
            'Queen' : 'Images/Black/Chess_qlt60.png',
            'King' : 'Images/Black/Chess_klt60.png',
            'Knight' :  'Images/Black/Chess_nlt60.png',
            'Pawn' : 'Images/Black/Ches_plt60.png',
            'Rook' : 'Images/Black/Chess_rlt60.png',
            'Bishop' : 'Images/Black/Chess_blt60.png'
        }
        self.chess_pieces_on_board = []
            


    """
    Creates the chess board filled with rectangles, starting from the lower left side of the board.
    Input: self
    Output: None
    """
   

    def create_tiles(self):
        colors = ["#000000", "#FFFFFF"] #Blck and white tiles colors
        for col in range(self.n):
            for row in range(self.n):
                tileColor = colors[0 if (row + col)%2 == 0 else 1]
                x1 = col * self.scale
                y1 = (7-row) * self.scale #Y postion starting from the lower left side
                x2 = x1 + self.scale
                y2 = y1 + self.scale
                #Debug:
                #print(f'col: {col} row: {row} x1: {x1} y1: {y1} x2: {x2} y2: {y2}') 
                self.board[row][col] = self.canvas.create_rectangle(x1, y1, x2, y2, fill=tileColor, tag=f'tile{col+1}{row+1}')
                self.canvas.tag_bind(f'tile{col+1}{row+1}','<Button-1>', lambda e, i=col+1, j=row+1: self.get_tile_pos(e,i,j))
                self.put_piece('Queen','white', x1, y1)
        

    def get_tile_pos(self, e, i, j):
        print(f'Current Tile: [{j}][{i}]')
       
    
    def put_piece(self, piece_type, color, x, y):
        if color == 'white':
            self.chess_pieces_on_board.append(PhotoImage(file=self.chessPiecesWhite[piece_type]))
        else:
            self.chess_pieces_on_board.append(PhotoImage(file=self.chessPiecesBlack[piece_type]))
        self.canvas.create_image(x, y, image=self.chess_pieces_on_board[(len(self.chess_pieces_on_board))-1], anchor=NW)
        

board = Layout()
board.create_tiles()
board.mainloop()