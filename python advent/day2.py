#creating a function to find out the possibility of the game

def game(red , green , blue )
 
totalred = 12
totalgreen = 13
totalblue = 14

  if red >= total_red or green >= total_green or blue >= total_blue:
        return False
    else:
        print("Game possible")
        return True

game1 = [blue = 3 , red = 4, red = 1, green = 2, blue = 6, green = 2]
 possibility = game(game1)

game2 = [blue = 1 , green = 2, green = 3, blue = 4, red = 1, green = 1, blue = 1]
 possibility = game(game1)

game3 = [green = 8 , blue = 6, red = 20, blue = 5, red = 4 , green = 13 , green = 5 , red = 1]
 possibility = game(game1)

game4 = [green = 1 , red = 3, blue = 6 , green = 3, red = 6, green = 3, blue = 15]
 possibility = game(game1)

game5 = [red = 6 , blue = 1, green = 3, blue = 2, red = 1, green = 2]
 possibility = game(game1)