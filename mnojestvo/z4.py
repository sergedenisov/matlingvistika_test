intext = open("input.txt", "r")

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
intext.close
print(wordcount)
