import os


def check():
    try:
        import termcolor
    except ImportError:
        print("installing needed libraries")
        os.system("pip install termcolor")
