import random
def getWord():
    with open('wordlist.txt','r') as file:
        data = file.readlines()
    wordList=[]
    for i in data:
        word=str(i)
        if '\n' in word:
            newWord=word.replace('\n','')
            word=newWord
        wordList.append(word)
    RandIndex=random.randint(0,len(wordList)-1)
    return (wordList[RandIndex])