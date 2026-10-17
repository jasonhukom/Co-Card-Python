# sys.argv (argument vector) is the type list of every word in the command prompt before entering
import sys

def main():
    print("Hello! My name is", sys.argv[1])

if __name__ == "__main__":
    main()