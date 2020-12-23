import os, sys
import termcolor
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

import variables


def check():
    try:
        import termcolor
    except ImportError:
        print("installing needed libraries")
        os.system("pip install termcolor")


if __name__ == '__main__':
    termcolor.colored(variables.standalone, 'red')
    input()