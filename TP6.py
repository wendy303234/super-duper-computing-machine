from os import system as clear

class Board ():

    def __init__(self):
        self.cells = [" "," "," "," "," "," "," "," "," "," "]

    def display (self):
        print(" %s | %s | %s " %(self.cells[1], self.cells[2], self.cells[3]))
        print("-----------" )
        print(" %s | %s | %s " %(self.cells[4], self.cells[5], self.cells[6]))
        print("-----------" )
        print(" %s | %s | %s " %(self.cells[7], self.cells[8], self.cells[9]))

    def update_cells(self, cell_no, player):
        if self.cells[cell_no] == " ":
            self.cells[cell_no] = player

    global liste 
    liste = []
    
    def play_joueur1(self,player_1):
        x_choice = 0
        while x_choice in liste or x_choice < 1 or x_choice > 9 :
            x_choice = int(input (player_1 + " choisi un nombre entre 1 et 9 : "))
        board.update_cells (x_choice, "X")
        liste.append(x_choice)
        

    def play_joueur2(self,player_2):
        o_choice = 0
        while o_choice < 1 or o_choice > 9 or o_choice in liste :
            o_choice = int(input (player_2 + " Choisi un nombre entre 1 et 9 : "))
        board.update_cells (o_choice, "O")
        liste.append(o_choice)
        

    def player1_win(self):
        if (self.cells[1] == "X" and self.cells[2] == "X" and self.cells[3] == "X"
        or self.cells[4] == "X" and self.cells[5] == "X" and self.cells[6] == "X"
        or self.cells[7] == "X" and self.cells[8] == "X" and self.cells[9] == "X"
        or self.cells[1] == "X" and self.cells[4] == "X" and self.cells[7] == "X"
        or self.cells[2] == "X" and self.cells[5] == "X" and self.cells[8] == "X"
        or self.cells[3] == "X" and self.cells[6] == "X" and self.cells[9] == "X"
        or self.cells[1] == "X" and self.cells[5] == "X" and self.cells[9] == "X"
        or self.cells[3] == "X" and self.cells[5] == "X" and self.cells[7] == "X"):
            return True

    def player2_win(self):
        if (self.cells[1] == "O" and self.cells[2] == "O" and self.cells[3] == "O"
        or self.cells[4] == "O" and self.cells[5] == "O" and self.cells[6] == "O"
        or self.cells[7] == "O" and self.cells[8] == "O" and self.cells[9] == "O"
        or self.cells[1] == "O" and self.cells[4] == "O" and self.cells[7] == "O"
        or self.cells[2] == "O" and self.cells[5] == "O" and self.cells[8] == "O"
        or self.cells[3] == "O" and self.cells[6] == "O" and self.cells[9] == "O"
        or self.cells[1] == "O" and self.cells[5] == "O" and self.cells[9] == "O"
        or self.cells[3] == "O" and self.cells[5] == "O" and self.cells[7] == "O"):
            return True

    def egalite(self):
        case_utilise = 0
        for i in self.cells:
            if i != " ":
                case_utilise += 1
            if case_utilise == 9:
                return True
                print("égalité!")

    def rejouer (self):
        play_again = input("voulez vous rejouer? (O/N) : ").upper()
        if play_again == "O":
            board.nouvelle_partie()
            return True
            
    def nouvelle_partie(self):
        self.cells = [" "," "," "," "," "," "," "," "," "," "]
        global liste
        liste = []
        
board = Board()


def refresh_screen():
    clear("cls")
    print_header()
    board.display()


def print_header():
    print("Bienvenu sur le jeu Tic-Tac-Toe")


print_header()
board.display()
player1 = input("Entrez le nom du joueur 1 : ")
player2 = input("Entrez le nom du joueur 2 : ")

while True:
    refresh_screen()
    board.play_joueur1(player1)
    if board.player1_win():
        refresh_screen()
        print(player1, "a gagné")
        if board.rejouer():
            continue
        else:
            break
    if board.egalite():
        print ("égalité ! ")
        if board.rejouer():
            continue
        else:
            break
    
    else:
        refresh_screen()
        board.play_joueur2(player2)
    if board.player2_win():
        refresh_screen()
        print(player2, "a gagné")
        if board.rejouer():
            continue
        else:
            break





