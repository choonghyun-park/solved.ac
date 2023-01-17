import sys

def checkLines(answerLines,inputLines,N,M):
    scores = []

    for x in range(N-7):
        for y in range(M-7):
            SLines = selectedLines(inputLines,x,y)
            score = checkLines8x8(answerLines,SLines)
            scores.append(score)
    
    return min(scores)

def checkLines8x8(answerLines,inputLines):
    score = 0

    for i in range(8):
        answerLine = answerLines[i]
        inputLine = inputLines[i]
        if answerLine==inputLine:continue
        else:
            for j in range(8):
                if answerLine[j]!=inputLine[j]:
                    # print("WrongLine : [{},{}]".format(i,j))
                    score+=1
    
    return score

def selectedLines(inputLines,x,y):
    lines = []
    for i in range(8):
        line = inputLines[x+i] # str
        line = line[y:y+8]
        lines.append(line)
    
    return lines

def editLine(initBlock):
    line = []
    if initBlock=="B": line.append("B")
    elif initBlock=="W": line.append("W")
    for i in range(1,8):
        if line[i-1]=="B":line.append("W")
        elif line[i-1]=="W":line.append("B")
    line = ''.join(line) # str
    return line

def editLines(initBlock):
    lines = []
    if initBlock=="B": lines.append(editLine("B"))
    elif initBlock=="W": lines.append(editLine("W"))
    for i in range(1,8):
        if lines[i-1][0]=="B":lines.append(editLine("W"))
        elif lines[i-1][0]=="W":lines.append(editLine("B"))
    return lines



N,M = map(int,input().split())
inputLines=[]

for i in range(N):
    line = sys.stdin.readline().rstrip() # str
    inputLines.append(line)


BLines = editLines("B") # 8x8
WLines = editLines("W") # 8x8

BScore = checkLines(BLines,inputLines,N,M)
WScore = checkLines(WLines,inputLines,N,M)

print(min([BScore,WScore]))



