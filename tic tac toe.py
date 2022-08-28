import os
spots = {1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 
         6 : '6', 7 : '7', 8 : '8', 9 : '9'}

def draw_board(spots):
  board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
             f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
             f"|{spots[7]}|{spots[8]}|{spots[9]}|") 
  print(board)


def check_turn(turn):
  if turn % 2 == 0: return 'O'
  else: return 'X'

def check_for_win(spots):
  # Handle Horizontal Cases
  if   (spots[1] == spots[2] == spots[3]) \
    or (spots[4] == spots[5] == spots[6]) \
    or (spots[7] == spots[8] == spots[9]):
    return True
  # Handle Vertical Cases
  elif   (spots[1] == spots[4] == spots[7]) \
    or (spots[2] == spots[5] == spots[8]) \
    or (spots[3] == spots[6] == spots[9]):
    return True
  # Diagonal Cases
  elif (spots[1] == spots[5] == spots[9]) \
    or (spots[3] == spots[5] == spots[7]):
    return True
      
  else: return False



playing, complete = True, False
turn = 0
prev_turn = -1

while playing:
    # Reset the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    # Draw the current Game Board
    draw_board(spots)
    # if an invalid turn occurred, let the player know
    if prev_turn == turn:
      print("invalid spot selected, please pick another.")
    prev_turn = turn
    print("Player " + str((turn % 2) +1) + "'s turn: Pick your spot or press q to quit.")
  
    # Get input and make sure it's valid
    choice = input() 
    if choice == 'q':
       playing = False
    # Check if the player give a number from 1-9
    elif str.isdigit(choice) and int(choice) in spots:
      # check if the spot has already been taken
      if not spots[int(choice)] in {"X","O"}:
      # Valid input, update the board
       turn += 1
       spots[int(choice)] = check_turn(turn)
     
    # Check if the game has ended (and if someone won)
    if check_for_win(spots): playing, complete = False, True
    if turn > 8: playing = False

# draw the board last time.
os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)
# if there was a winner, say who won
if complete:
  if check_turn(turn) == 'X': print("Player 1 Wins!")
  else: print("Player 2 Wins!")
else: 
  # Tie Game
  print("No Winner")
  
print("Thanks for playing!")
