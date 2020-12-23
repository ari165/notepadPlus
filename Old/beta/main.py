print("notepad+ beta")
opr = input("1.read/2.write: ")

if opr == "1":
    title = input("file name: ")
    file = open(title, 'r')
    print(file.read())

else:
    title = input("title: ")
    text = input("text: ")

    file = open(title, 'w+')
    file.write(text)
