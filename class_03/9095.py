import sys

T = int(sys.stdin.readline())

n_lst = []


def sol(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:
        return sol(n-1)+sol(n-2)+sol(n-3)


for _ in range(T):
    n = int(sys.stdin.readline())
    n_lst.append(n)

for n in n_lst:
    print(sol(n))
    
        
