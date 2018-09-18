import string

dict = {}
data = ""
ascii = string.ascii_letters
file = open("files.txt", "w")

for i in range(len(ascii)):
    dict[ascii[i]] = ascii[i-1]
print(dict)

with open("files.txt") as f:
    while True:
        c = f.read(1)
        if not c:
            print("End of file")
            break
        if c in dict:
            data = dict[c]
        else:
            data = c
        file.write(data)
        print(data)
file.close()
