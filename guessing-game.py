def main():
    print("*****PYTHON GUESSING GAME*****")
    answer= "rabbit"
    guess =""

    while not answer == guess.lower():
        print ("I'm thinking of an animal...")
        guess = input("What is the name of the animal? ")
        print("")

        if guess.lower()== answer:
            print ("Wow! You are correct! Great job!")
            print("")
            
            userLike=input("Do you like that animal? y/n?")
            if userLike.lower()=="y":
                print("Good to know! Thanks for playing!")
                break
            elif userLike.lower()=="n":
                print("That's too bad!")
                break
            else:
                print("Thanks for playing!")
            
        elif guess.lower()[0]=="q":
            print ("Now exiting, thanks for playing!")
            break
        else:
            print ("Incorrect, try again!")
        
    
    
main()
