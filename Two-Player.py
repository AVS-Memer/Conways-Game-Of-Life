import time
#input('Welcome to Conway\'s Game of Life. We start with a 30*60 grid of cells, either alive or dead. Here are the rules:\n\t1) Any live cell with fewer than 2 live neighbors dies, as if by\n\tunderpopulation.\n\t2) Any live cell with 2 or 3 live neighbors live on to the next\n\tgeneration.\n\t3)Any live cell with more than 3 live neighbors dies, as if by\n\toverpopulation.\n\t4) Any dead cell with exactly 3 live neighbors becomes a live cell, as\n\tif by reproduction.\nPress Enter to contine:')
#create grid
O = 5
X = 5
biglist = []
def gridmaker(biglist):
  for i in range(10):
    smallist = []
    for j in range(10):
      smallist.append(0)
    biglist.append(smallist)
gridmaker(biglist)

#print grid
def prin(biglist):
  for i in range(10):
    for j in range(10):
      if biglist[i][j] == 1:
        print('O',end = '')
      elif biglist[i][j] == 2:
        print('X',end = '')
      else:
        print('-',end = '')
    print()

#read file
f = open('StartingCoords/player1.in','r')
fileinfo = f.readlines()
fileinfo = [i.split() for i in fileinfo]
f.close()
f = open('StartingCoords/player2.in','r')
fileinfo2 = f.readlines()
fileinfo2 = [i.split() for i in fileinfo2]
f.close()
def readfile(fileinfo,turn):
  for i in range(len(fileinfo)):
    x = fileinfo[i][0]
    y = fileinfo[i][1]
    biglist[int(x)][int(y)] = turn
readfile(fileinfo,1)
readfile(fileinfo2,2)
prin(biglist)

#count neighboring cells
def countneighbor():
  newlist = []
  gridmaker(newlist)
  for i in range(10):
    for j in range(10):
      newlist[i][j] = biglist[i][j]
  for i in range(10):
    for j in range(10):
      count = [0,0]
      if j>0:
        if i>0 and biglist[i-1][j-1]:
          count[biglist[i-1][j-1]-1] += 1
        if biglist[i][j-1]:
         count[biglist[i][j-1]-1] += 1
        if i<9 and biglist[i+1][j-1]:
          count[biglist[i+1][j-1]-1] += 1
      if i>0 and biglist[i-1][j]:
        count[biglist[i-1][j]-1] += 1
      if i<9 and biglist[i+1][j]:
        count[biglist[i+1][j]-1] += 1
      if j<9:
        if i>0 and biglist[i-1][j+1]:
          count[biglist[i-1][j+1]-1] += 1
        if biglist[i][j+1]:
          count[biglist[i][j+1]-1] += 1
        if i<9 and biglist[i+1][j+1]:
          count[biglist[i+1][j+1]-1] += 1
      if biglist[i][j]:
        if sum(count) < 2 or sum(count) > 3:
          newlist[i][j] = 0
      elif sum(count) == 3:
        if count[0]>count[1]:
          newlist[i][j] = 1
        else:
          newlist[i][j] = 2
  for i in range(10):
    for j in range(10):
      biglist[i][j] = newlist[i][j]

def playercell(biglist):
  global O
  global X
  O = 0
  X = 0
  for i in range(10):
    for j in range(10):
      if biglist[i][j] == 1:
        O += 1
      elif biglist[i][j] == 2:
        X += 1
  print('Player O has ' + str(O) + ' cells alive')
  print('Player X has ' + str(X) + ' cells alive')

while X != 0 and O != 0:
  rowadd = input('Player O, please enter the row of the cell you wish to add: ')
  columnadd = input('Player O, please enter the column of the cell you wish to add: ')
  rowadd = int(rowadd)
  columnadd = int(columnadd)
  if biglist[rowadd][columnadd]:
    print('that space is occupied')
    while biglist[rowadd][columnadd]:
      rowadd = input('Player O, please enter the row of the cell you wish to add: ')
      columnadd = input('Player O, please enter the column of the cell you wish to add: ')
      rowadd = int(rowadd)
      columnadd = int(columnadd)
      if biglist[rowadd][columnadd]:
        print('that space is occupied')
  biglist[rowadd][columnadd] = 1
  

  rowdelete = input('Player O, please enter the row of the cell you wish to delete: ')
  columndelete = input('Player O, please enter the column of the cell you wish to delete: ')
  rowdelete = int(rowdelete)
  columndelete = int(columndelete)
  if not biglist[rowdelete][columndelete]:
    print('you cannot delete that space')
    while not biglist[rowdelete][columndelete]:
      rowdelete = input('Player O, please enter the row of the cell you wish to delete: ')
      columndelete = input('Player O, please enter the column of the cell you wish to delete: ')
      if not biglist[rowdelete][columndelete]:
        print('you cannot delete that space')
  biglist[rowdelete][columndelete] = 0
  countneighbor()
  print()
  prin(biglist)
  playercell(biglist)
  if X == 0 or O == 0:
    break
  
  rowadd = input('Player X, please enter the row of the cell you wish to add: ')
  columnadd = input('Player X, please enter the column of the cell you wish to add: ')
  rowadd = int(rowadd)
  columnadd = int(columnadd)
  if biglist[rowadd][columnadd]:
    print('that space is occupied')
    while biglist[rowadd][columnadd]:
      rowadd = input('Player X, please enter the row of the cell you wish to add: ')
      columnadd = input('Player X, please enter the column of the cell you wish to add: ')
      rowadd = int(rowadd)
      columnadd = int(columnadd)
      if biglist[rowadd][columnadd]:
        print('that space is occupied')
  biglist[rowadd][columnadd] = 2
  

  rowdelete = input('Player X, please enter the row of the cell you wish to delete: ')
  columndelete = input('Player X, please enter the column of the cell you wish to delete: ')
  rowdelete = int(rowdelete)
  columndelete = int(columndelete)
  if not biglist[rowdelete][columndelete]:
    print('you cannot delete that space')
    while not biglist[rowdelete][columndelete]:
      rowdelete = input('Player X, please enter the row of the cell you wish to delete: ')
      columndelete = input('Player X, please enter the column of the cell you wish to delete: ')
      rowdelete = int(rowdelete)
      columndelete = int(columndelete)
      if not biglist[rowdelete][columndelete]:
        print('you cannot delete that space')
  biglist[rowdelete][columndelete] = 0
  
  
  countneighbor()
  print()
  prin(biglist)
  playercell(biglist)
  if X == 0 or O == 0:
    break
if X == 0:
  if O == 0:
    print('Player O and Player X tied.')
  else:
    print('Player O wins!')
else:
  print('player X wins!')
  
