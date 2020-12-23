# from .importer import check
import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
import GUI


# check()

# main
print("notepad+ \n" + "version: 3beta \n" + "please report any bugs to Arian")

window = GUI.MainWindow()
window.Loop()

input("press any key to exit...")
