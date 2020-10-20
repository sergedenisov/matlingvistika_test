txt = open("input.txt", "r")
sent = 'hellow worldh'
letters = []
for i in range(0, len(sent)):
    count = 0
    if sent[i] not in letters:
        letters.append(sent[i])
        for j in range(0, len(sent)):
            if sent[j] == sent[i]:
                count = count +1
        print(sent[i], ' - ', count)
