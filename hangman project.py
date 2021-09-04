#hangman project
insert_word=input("enter the word:")
print("hai,"+ insert_word)
word="lap"
guesses=' '
turn=5
while turn>0:
    failed = 0
    for char in  word:

        if char in guesses:
            print(1,end=" ")
        else:
            print("_",end=" ")
            failed+=1

    if failed==0:
             #print("\n you win")
             break
    print()
    guess=input("enter the guess word:")
    guesses=guesses+guess
    if guess not in word:
        turn-=1
        print("wrong")
        print("you have",+ turn,"more guesses")
        if turn == 0:
           print("you lose")
        

