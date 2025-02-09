navn = input("Enter name here --> ")
symbol = input("What specific symbol do you want? ")
words = navn.split()  # Splitting the input into a list of words
print(words)

for word in words:
    if symbol in word:  # Check if the symbol is in the word
        print(word)
