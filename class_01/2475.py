lst = list(map(int,input().split()))
sum = 0
for v in lst:
    sum += v**2
gum = sum%10
print(gum)