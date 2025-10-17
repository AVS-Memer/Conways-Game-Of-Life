import time
input('Welcome to Conway\'s Game of Life. We start with a 30*60 grid of cells, either alive or dead. Here are the rules:\n\t1) Any live cell with fewer than 2 live neighbors dies, as if by\n\tunderpopulation.\n\t2) Any live cell with 2 or 3 live neighbors live on to the next\n\tgeneration.\n\t3)Any live cell with more than 3 live neighbors dies, as if by\n\toverpopulation.\n\t4) Any dead cell with exactly 3 live neighbors becomes a live cell, as\n\tif by reproduction.\nPress Enter to contine:')
#create grid
biglist = []
def gridmaker(biglist):
  for i in range(30):
    smallist = []
    for j in range(60):
      smallist.append(False)
    biglist.append(smallist)
gridmaker(biglist)
#print grid
def prin(biglist):
  for i in range(30):
    for j in range(60):
      if biglist[i][j]:
        print('O',end = '')
      else:
        print('-',end = '')
    print()
#read file
f = open('hertz-oscillator.in','r')
fileinfo = f.readlines()
fileinfo = [i.split() for i in fileinfo]
f.close()
def readfile(fileinfo):
  for i in range(len(fileinfo)):
    x = fileinfo[i][0]
    y = fileinfo[i][1]
    biglist[int(x)][int(y)] = True
readfile(fileinfo)
prin(biglist)
#count neighboring cells
def countneighbor():
  newlist = []
  gridmaker(newlist)
  for i in range(30):
    for j in range(60):
      count = 0
      if j>0:
        if i>0 and biglist[i-1][j-1]:
          count += 1
        if biglist[i][j-1]:
          count += 1
        if i<29 and biglist[i+1][j-1]:
          count += 1
      if i>0 and biglist[i-1][j]:
        count += 1
      if i<29 and biglist[i+1][j]:
        count += 1
      if j<59:
        if i>0 and biglist[i-1][j+1]:
          count += 1
        if biglist[i][j+1]:
          count += 1
        if i<29 and biglist[i+1][j+1]:
          count += 1
      if biglist[i][j]:
        if count < 2 or count > 3:
          newlist[i][j] = False
        else:
          newlist[i][j] = True
      elif count == 3:
        newlist[i][j] = True
  for i in range(len(newlist)):
    biglist[i] = newlist[i]
while 1==1:
  time.sleep(0.5)
  countneighbor()
  prin(biglist)
