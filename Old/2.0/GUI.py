import tkinter as tk
from tkinter.scrolledtext import ScrolledText


class Read:
    def __init__(self, master, text):
        self.text = text
        self.master = master
        self.frame = tk.Frame(self.master)
        self.lbl1 = tk.Label(self.frame, text=self.text)
        self.lbl1.pack()
        self.frame.pack()

    def exit(self):
        self.master.destroy()


class Write:
    def __init__(self, master, title):
        self.master = master
        self.title = title
        self.file = open('files/' + self.title, 'w+')

        self.frame = tk.Frame(self.master)
        self.textFrame = ScrolledText(self.master)
        self.btn = tk.Button(self.master, text="save", command=self.save)

        self.textFrame.pack()
        self.btn.pack()
        self.frame.pack()

    def save(self):
        text = self.textFrame.get('1.0', tk.END)
        self.file.write(text)


# functions
def read(text):
    root = tk.Tk()
    Read(root, text)
    root.mainloop()


def write(title):
    root = tk.Tk()
    Write(root, title)
    root.mainloop()


if __name__ == '__main__':
    print("please don't run this file as standalone\n"
                       "the main program will run it automatically")

    input("press any key to exit...")
