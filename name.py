# sys.argv (argument vector) is the type list of every word in the command prompt before entering
import sys

def main(): 
    arg = sys.argv
    subtext = " Please read README.md"

    if len(arg) < 2:
        sys.exit("Too few arguments!" + subtext)
    elif len(arg) > 2:
        sys.exit("Too many arguments!" + subtext)
    
    print("Hello! My name is " + arg[1])

if __name__ == "__main__":
    main()