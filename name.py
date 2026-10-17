# sys.argv (argument vector) is the type list of every word in the command prompt before entering
import sys

def main(): 
    arg = sys.argv
    error_line = True
    if len(arg) < 2:
        output = "Too few arguments!"
    elif len(arg) > 2:
        output = "Too many arguments!"
    else:
        name = arg[1]
        output = "Hello! My name is " + name
        error_line = False

    subtext = " Please read README.md"
    
    print(output + (subtext if error_line else ""))

if __name__ == "__main__":
    main()