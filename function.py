def countwords():
    filename = input("Enter the file name: ")
    NumberOfWords = 0
    file = open(filename, "r")
    for line in file:
        words = line.split()
        NumberOfWords = NumberOfWords+len(words)
    print("NumberOfWords: " + str(NumberOfWords))

countwords()