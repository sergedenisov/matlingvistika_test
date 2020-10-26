infile = open("input.txt", "r")

def z1(intext):
    n = intext.readline()
    l = list(map(int, n.split()))
    ls = set()

    for i in range(0, len(l)):
        counter = 0;
        if l[i] not in ls:
            ls.add(l[i])
            for j in range(0, len(l)):
                if l[j] == l[i]:
                    counter = counter + 1;
            print(l[i], ' - ', counter)

def z2(intext):
    n = intext.readline()
    l = list(map(int, n.split()))
    ls = set()

    for i in range(0, len(l)):
        if l[i] not in ls:
            ls.add(l[i])
            print(l[i], 'YES')
        else:
            print(l[i], 'NO')

def z3(intext):
    n = int(intext.readline())

    wordcount = 0;
    wordbank = set()
    for i in range(0, n):
        s = intext.readline()
        sent  = s.split()
        for word in sent:
            if word not in wordbank:
                wordbank.add(word)
                wordcount = wordcount + 1;
    return wordcount


print(z2(infile))
infile.close
