with open("sample.txt",'r+') as f:
    for line in f:
        for letter in line:
            print(letter)
