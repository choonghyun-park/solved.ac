import itertools

def calScore(n1,n2,n3,M):
    sum = n1+n2+n3
    if sum<=M:
        return sum
    else: return -1

N,M = map(int,input().split())
cards = list(map(int,input().split()))
scores = []

arr = list(range(N))
_5C3 = itertools.combinations(arr,3)
lst_5C3 = list(_5C3)

for idxs in lst_5C3:
    n1 = cards[idxs[0]]
    n2 = cards[idxs[1]]
    n3 = cards[idxs[2]]

    score = calScore(n1,n2,n3,M)
    if score>0:scores.append(score)

print(max(scores))

