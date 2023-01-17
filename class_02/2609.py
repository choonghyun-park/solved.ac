# 최대공약수 (GCF : Greatest Common Factor)
def GCF(a,b):
    smaller = min([a,b])
    for i in range(smaller):
        gcf = smaller-i
        if a%gcf==0 and b%gcf==0:
            return gcf

# 최소공배수 (LCM : Least Common Multiple)
def LCM(a,b):
    gcf = GCF(a,b)
    lcm = gcf * int(a/gcf) * int(b/gcf)
    return lcm

a,b = map(int,input().split())

print(GCF(a,b))
print(LCM(a,b))

