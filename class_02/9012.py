import sys

def isVPS(input):
    copyInput = input
    while(len(copyInput)>0):
        # print("input state :",copyInput)
        savedInput = copyInput
        copyInput = copyInput.replace("()","")
        if len(savedInput)==len(copyInput):
            return False
    return True

T = int(input())
inputs = []
for i in range(T):
    input = sys.stdin.readline().rstrip()
    inputs.append(input)

for input in inputs:
    if isVPS(input):print("YES")
    else:print("NO")
