def createLadder(steps):
    #Initializing my matrix
    ladder = []
    for i in range(steps):
            ladder.append([' ']  * steps)

    for i in range(len(ladder)):
        for j in range(len(ladder)):
            if(i+j+1 >= steps):
                ladder[i][j] = "*" 
    showLadder(ladder)

def showLadder(ladder):
    for i in ladder:
        for j in i:
           print(f"[{j}]", end='')
        print()
    print("=-="*len(ladder))

createLadder(0)
createLadder(1)
createLadder(2)
createLadder(3)
createLadder(4)
createLadder(5)
createLadder(7)
createLadder(10)

