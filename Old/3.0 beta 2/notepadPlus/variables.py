import termcolor

output = "../output/"
standalone = "please don't run this file as a standalone\n the main program will run it automatically"


if __name__ == '__main__':
    termcolor.colored(standalone, 'red')
