import sys


N = int(input())
words = {}
wordkeys = []
for i in range(N):
    word = sys.stdin.readline().rstrip()
    wordLength = len(word)
    if wordLength in words:
        if word not in words[wordLength]:
            words[wordLength].append(word)
    else:
        words[wordLength]=[word]
        wordkeys.append(wordLength)    
wordkeys.sort()
for wordkey in wordkeys:
    curWords = sorted(words[wordkey])
    for i in range(len(curWords)):
        print(curWords[i])



