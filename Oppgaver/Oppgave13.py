filelocationator = input("Write filetype: ")

for i in range(len(filelocationator)):
    if filelocationator[i] == ".":
        print(f"Your filetype is --> {filelocationator[i:len(filelocationator)]}")
