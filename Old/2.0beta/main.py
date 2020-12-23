import GUI

illegal = False


def checker(string):
    for i in range(len(string)):
        if string[i] == "/":
            global illegal
            illegal = True
            break

    if string == "" or string == " ":
        illegal = True


# main
print("notepad+ \n"
      "version: 2.0beta")
mode = input("1.CUI/2.GUI: ")
opr = input("1.read/2.write: ")

# read
if opr == "1":
    title = input("file name: ")
    checker(title)

    try:
        if not illegal:
            file = open("files/" + title, 'r')
            if mode == "1":
                print(file.read())
            else:
                GUI.read(file.read())
        else:
            print("Error: can't use '" + title + "' as file name")

    except FileNotFoundError:
        print("Error: file doesn't exist")

# write
elif opr == "2":
    title = input("title: ")

    if not illegal:
        if mode == "1":
            text = input("text: ")
            checker(text)
            file = open("files/" + title, 'w+')
            file.write(text)
            print("saved")
        else:
            GUI.write(title)
    else:
        print("Error: cant use [/] in file name")
else:
    print("Error:", "[" + opr + "]", "doesn't exist")

input("press any key to exit...")
