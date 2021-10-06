import json


chessPiecesWhite = {
    "Type" : {
        'Queen' : 'Images\\White\\Chess_qlt60.png',
        'King' : 'Images\\White\\Chess_klt60.png',
        'Knight' :  'Images\White\\Chess_nlt60.png',
        'Pawn' : 'Images\\White\\Ches_plt60.png',
        'Rook' : 'Images\\White\\Chess_rlt60.png',
        'Bishop' : 'Images\\White\\Chess_blt60.png'
    }
}

chessPiecesBlack = {
    "Type" : {
        'Queen' : 'Images\\Black\\Chess_qlt60.png',
        'King' : 'Images\\Black\\Chess_klt60.png',
        'Knight' :  'Images\Black\\Chess_nlt60.png',
        'Pawn' : 'Images\\Black\\Ches_plt60.png',
        'Rook' : 'Images\\Black\\Chess_rlt60.png',
        'Bishop' : 'Images\\Black\\Chess_blt60.png'
    }
}

with open('WhiteChessPieces.json', 'w') as write_file:
    json.dump(chessPiecesWhite, write_file)

with open('BlackChessPieces.json', 'w') as write_file:
    json.dump(chessPiecesBlack, write_file)    