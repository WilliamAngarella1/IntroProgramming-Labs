def fibonacci():
    global current, last
    current=1
    last=1

    n= int(input("Enter a number: "))

    for i in range(n-2):
        current, last = current+last, current
    
def main():
    fibonacci()
    print(current)


main()
