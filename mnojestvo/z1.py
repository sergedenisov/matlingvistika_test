l = [23,43,31,23,23,56, 31]

ls = set()

for i in range(0, len(l)):
    counter = 0;
    if l[i] not in ls:
        ls.add(l[i])
        for j in range(0, len(l)):
            if l[j] == l[i]:
                counter = counter + 1;
        print(l[i], ' - ', counter)
