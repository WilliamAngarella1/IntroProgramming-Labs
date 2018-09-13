#Madlib Program
#CMPT120
#9/13/18
#Author: Will Angarella

def promptForWords():
    global name, verb, adj
    print("Welcome to my madlib! Enter the type of word as prompted for a laugh.")
    name = input("Please enter a name (doesn't necessarily need to be yours).")
    verb = input("Please enter a verb ending in 'ing.'")
    adj = input("Please enter an adjective.")



def makeAndPrint():
    print("Well tell me this, " + name + ", are you " + verb + " " + adj + ", punk?")


def main():
    promptForWords()
    makeAndPrint()

main()
