import sys

def isPelindrom(input):
    rev = list(input)
    rev.reverse()
    rev = ''.join(rev)

    if input==rev:return True
    else: False

inputs = []
while(1):
    input = sys.stdin.readline().rstrip()
    if input=='0':break
    inputs.append(input)

for input in inputs:
    if isPelindrom(input):print("yes")
    else: print("no")

