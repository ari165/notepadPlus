import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import termcolor


# structure
class Window:
    def __init__(self, master):
        self.master = master

        self.master.title("notepad+")
        self.p1 = tk.PhotoImage(file='../data/icon.png')
        self.master.iconphoto(False, self.p1)

        self.frame = tk.Frame(self.master)
        self.frame.pack()


class Read(Window):
    def __init__(self, master, text):
        super().__init__(master)

        # widgets
        self.text = text
        self.lbl1 = tk.Label(self.frame, text=self.text)

        self.lbl1.pack()
        self.frame.pack()

    def exit(self):
        self.master.destroy()


class Write(Window):
    def __init__(self, master, title):
        super().__init__(master)
        self.title = title

        # widgets
        self.textFrame = ScrolledText(self.master)
        self.btn = tk.Button(self.master, text="save", command=self.save)

        self.textFrame.pack()
        self.btn.pack()

    def save(self):
        file = open('../output/' + self.title, 'w+')
        text = self.textFrame.get('1.0', tk.END)
        file.write(text)


# functions
def read(text):
    root = tk.Tk()
    Read(root, text)
    root.mainloop()


def write(title):
    root = tk.Tk()
    Write(root, title)
    root.mainloop()


# if the file is opened as standalone
if __name__ == '__main__':
    print(termcolor.colored("please don't run this file as a standalone\n"
                            "the main program will run it automatically", "red"))

    input("press any key to exit...")
