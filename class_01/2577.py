A,B,C = int(input()),int(input()),int(input())
mul = A*B*C
lst = []

def classify(n):
    lst[n] += 1

for i in range(10): lst.append(0)
while(mul>0):
    classify(mul%10)
    mul = mul//10
for i in range(10): print(lst[i])