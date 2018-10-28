# CMPT 120 - Lab #6
# Will Angarella
# 10/25/18
###
def getinput():
    global num1, num2
    try:    
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
    except ValueError:
        print("That isn't a number!")
        
def showIntro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.\n")
def showOutro():
    print("\nThank you for using the Arithmetic Engine…")
    print("\nPlease come back again soon!")
def doLoop():
    while True:
        cmd = input("What computation do you want to perform? ")
        cmd=cmd.lower() #first edit
        if cmd == "add":
            getinput()
            result = num1 + num2
        elif cmd == "sub":
            getinput()
            result = num1 - num2
        elif cmd == "mult":
                getinput()
                result = num1 * num2
        elif cmd == "div":
                getinput()
                result = num1 // num2
        elif cmd == "quit":
                break
        else:
                print (cmd, "is not a valid command. Enter a valid command.")
                continue
        print("The result is " + str(result) + ".\n")
def main():
 showIntro()
 doLoop()
 showOutro()
main()
