illegal = False


def checker(string):
    for i in range(len(string)):
        if string[i] == "/":
            global illegal
            illegal = True


# main
print("notepad+ v1.0")
opr = input("1.read/2.write: ")

if opr == "1":
    title = input("file name: ")
    checker(title)

    try:
        if not illegal:
            file = open("files/" + title, 'r')
            print(file.read())
        else:
            print("Error: cant use [/] in file name")
    except FileNotFoundError:
        print("Error: file doesn't exist")

elif opr == "2":
    title = input("title: ")
    text = input("text: ")
    checker(text)

    if not illegal:
        file = open("files/" + title, 'w+')
        file.write(text)
    else:
        print("Error: cant use [/] in file name")
else:
    print("Error:", "[" + opr + "]", "doesn't exist")
