#Hangman game
lives=5
word=list("Apple".lower())
guessing=[];

incorrect_letters=[]
#initializing array of guesses
guessing=["_"]*len(word)

#game algorithm
def printscore():
    print ("Lives: "+str(lives))
    print("Incorrect letters: ")
    for x in range(len(incorrect_letters)):
        if x==len(incorrect_letters)-1:
            print(incorrect_letters[x], end="")
        else:
            print(incorrect_letters[x], end=",")
    print("")
    for x in range(len(guessing)):
        if x==len(guessing)-1:
            print(guessing[x], end="")
        else:
            print(guessing[x], end=",")
    print("")

def updateLives():
  global lives
  lives-=1

def updateGuess(letter1):
    global word
    global guessing

    found="False"
    for x in range(len(word)):
        if word[x]==letter1:
            guessing[x]=letter1
            found="True"
    if found=="False":
        updateLives()
        print("Oh no, that letter wasn\'t there")
        incorrect_letters.append(letter1);
        print(incorrect_letters)
    print(guessing)

#main 
while(lives>0):
    charr=input("please guess a letter: ")
    updateGuess(charr)
    if "_" not in guessing:
        break;
if lives<=0:
    print("You lost, the word was:  {}".format(word))
else:
    print("Congrats, You have won!!  with {} lives left".format(lives))
