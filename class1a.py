mywords = input("enter your introduction")
charactercount = 0
wordcount = 1
for i in mywords:
    charactercount = charactercount + 1
    if(i==" "):
        wordcount = wordcount + 1
print("wordcount", wordcount)    
print("charactercount", charactercount)    