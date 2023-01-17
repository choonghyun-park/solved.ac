a,b = input().split()
# 문자열을 리스트로
a = list(a)
b = list(b)

# 리스트 역순으로
a.reverse()
b.reverse()

# 리스트를 문자열로
a = ''.join(a)
b = ''.join(b)

# 문자열을 정수로
a = int(a)
b = int(b)

if a>b:print(a)
elif a<b:print(b)