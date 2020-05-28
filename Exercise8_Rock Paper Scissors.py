plyinp1 = input("Player1 please input Rock, Paper or Scissor:")
plyinp2 = input("Player1 please input Rock, Paper or Scissor:")

def compare(ply1, ply2):
    if ply1 == ply2:
        return("It's a tie!")

    elif ply1 == "Rock":
        if ply2 =="Scissor":
            return("Rock win!")
        else:
            return("Paper win!")

    elif ply1 == "Paper":
        if ply2 =="Rock":
            return("Paper win!")
        else:
            return("Scissor win!")

    elif ply1 == "Scissor":
        if ply2 == "Paper":
            return("Scissor win!")
        else:
            return("Rock win!")




print(compare(plyinp1, plyinp2))