import Words
def checkChar(InputChar):
    global word
    global encrypt
    if InputChar in word:
        for i in range(len(word)):
            if InputChar==word[i]:
                encryptNew =encrypt[:i]+InputChar+encrypt[i+1:]
                encrypt = encryptNew
    return encrypt

def display(encrypt,attempt):    
    print('Word Status : \t'+encrypt)
    print('Attempts Left : \t'+str(attempt))    
        
def playHangman():
    global encrypt
    global word
    global attempt
    if encrypt!=word:
        display(encrypt,attempt)
        InputChar = input('Guess an Alphabet : \t')
        encrypt = checkChar(InputChar)
        attempt=attempt-1
    else:
        print("\nYou Won")
        attempt=0
    
if __name__ == "__main__":
    print("            Welcome to Hangman!")
    print("-----------------------------------------------")
    word=Words.getWord()
    word=word.lower()
    attempt=int(input("Enter the number of Attempts : "))
    encrypt='*'
    encrypt=encrypt*len(word)
    while attempt!=0:
        playHangman()
    if word!=encrypt:
        print("Sorry! You ran out of attempts")
    else:
        print("\nYou Won")
    print("The Word was '"+word+"'")
    print('Thanks for Playing')
        
