n = input()
l = list(map(int, n.split()))
ls = set()

for i in range(0,len(l)):
    if l[i] not in ls:
        ls.add(l[i])
        print(l[i], 'YES')
    else:
        print(l[i], 'NO')
