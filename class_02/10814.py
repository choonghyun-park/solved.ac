import sys

N = int(input())

keys = []
members = {}
for i in range(N):
    age,name = sys.stdin.readline().rstrip().split()
    age = int(age)
    if age in members:
        members[age].append(name)
    else:
        members[age]=[name]
        keys.append(age)
keys.sort()
for key in keys:
    membersInAge = members[key]
    for member in membersInAge:
        print(key,member)

