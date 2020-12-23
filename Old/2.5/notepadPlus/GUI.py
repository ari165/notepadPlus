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

        self.frame = tk.Frame(master=master, width=150, height=150)
        self.frame.pack()


class Read(Window):
    def __init__(self, master, text):
        super().__init__(master)

        # widgets
        self.lbl_text = tk.Label(self.frame, text=text)

        self.lbl_text.pack()

    def exit(self):
        self.master.destroy()


class Write(Window):
    def __init__(self, master):
        super().__init__(master)

        # widgets
        self.label = tk.Label(self.master, text="title: ")
        self.entry = tk.Entry(self.master, width=90)
        self.textFrame = ScrolledText(self.master)
        self.btn = tk.Button(self.master, text="save", command=self.save)

        # packs
        self.label.place(x=0, y=0)
        self.entry.pack()
        self.textFrame.pack()
        self.btn.pack()

    def save(self):
        title = self.entry.get()
        file = open('../output/' + title, 'w+')
        text = self.textFrame.get('1.0', tk.END)
        file.write(text)


# functions
def read(text):
    root = tk.Tk()
    Read(root, text)
    root.mainloop()


def write():
    root = tk.Tk()
    Write(root)
    root.mainloop()



# if the file is opened as standalone
if __name__ == '__main__':
    print(termcolor.colored("please don't run this file as a standalone\n"
                            "the main program will run it automatically", "red"))

    input("press any key to exit...")
