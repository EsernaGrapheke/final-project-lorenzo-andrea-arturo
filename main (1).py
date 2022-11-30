#Laberynth Proyect
#Find "E"
Maze=  [['x', 'x', 'x', 'x', 'x', 'x'],
        ['x', ' ', ' ', ' ', 'S', 'x'],
        ['x', ' ', 'x', 'x', ' ', 'x'],
        ['x', ' ', 'x', 'x', ' ', 'x'],
        ['x', ' ', 'x', 'x', ' ', 'x'],
        ['x', ' ', 'x', ' ', ' ', 'x'],
        ['x', ' ', 'x', ' ', 'x', 'x'],
        ['x', ' ', ' ', 'E', ' ', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x']]

row=0
while row < len(Maze):
    column=0
    while column<len(Maze[0]):
        if Maze[row][column] == "E":
            entrancex=column
            entrancey=row
        column+=1
    row+=1 
print (entrancey)
print (entrancex)

#Move through the blanks
Repeat
if entrancex-1==" ":
   numberofpaths>=1
if entrancey+1==" ":
    numberofpaths>=1
if entrancex+1==" ":
   numberofpaths>=1
if entrancey-1==" ":
   numberofpaths>=1
print numberofpaths

if numberofpaths>1:
    Checkpoint
    currentposition= entrancex, entrancey
    
if numberofpaths<2:
    entrancex+1
    entrancey+1
    movecount+1

if entrancex-1=="S":
    print movecount
if entrancey+1=="S":
    print movecount
if entrancex+1=="S":
    print movecount
if entrancey-1=="S":
    print movecount



