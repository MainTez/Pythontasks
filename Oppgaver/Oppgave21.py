Height = int(input("Write in the height of the pyramid --> "))

for i in range (1, Height + 1):

    print(" " * (Height - i), "*" * (2* i -1))