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
        else:
            print ("Incorrect, try again!")
        
    
    
main()
