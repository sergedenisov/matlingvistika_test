n = int(input())

wordcount = 0;
wordbank = set()
for i in range(0, n):
    s = input()
    sent  = s.split()
    for word in sent:
        if word not in wordbank:
            wordbank.add(word)
            wordcount = wordcount + 1;
print(wordcount)
