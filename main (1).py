labyrinth = [['x', 'x', 'x', 'x', 'x', 'x'],
             ['x', ' ', ' ', ' ', 'S', 'x'],
             ['x', ' ', 'x', 'x', ' ', 'x'],
             ['x', ' ', 'x', 'x', ' ', 'x'],
             ['x', ' ', 'x', 'x', ' ', 'x'],
             ['x', ' ', 'x', ' ', ' ', 'x'],
             ['x', ' ', 'x', ' ', 'x', 'x'],
             ['x', ' ', ' ', 'E', ' ', 'x'],
             ['x', 'x', 'x', 'x', 'x', 'x']]
row = 0
while row< len(labyrinth):
    colum = 0
    while colum<len(labyrinth[0]):
        if labyrinth[row][colum] == 'E' :
            entrancex=colum
            entrancey=row
        colum+=1
    row+=1
print(entrancey)
print(entrancex)



if labyrinth[currentpositiony][currentpositionx-1]= ' ' :
    entrancex-1
    print(entrancex-1 )
    
if  labyrinth[currentpositiony][currentpositionx+1]= ' ' :
    entrancex+1
    print(entancex+1)
if labyrinth[currentpositiony-1][currentpositionx]= ' ' :
    entrancey-1
    print(entrancey-1)
if labyrinth[currentpositiony+1][currentpositionx]= ' ' :
    entrancey+1
    print(entrancey)

