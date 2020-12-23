import os, sys
import tkinter as tk
import tkinter.filedialog
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

import variables


# structure
class MainWindow:
    def __init__(self):
        self.master = tk.Tk()

        self.master.title("notepad+")
        self.p1 = tk.PhotoImage(file='../data/icon.png')
        self.master.iconphoto(False, self.p1)
        self.master.geometry("600x500")

        # menubar
        self.menubar = tk.Menu(self.master)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Open", command=self.Open_file)
        self.filemenu.add_command(label="Save", command=self.Save_file)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.master.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.frame = tk.Frame(master=self.master, width=150, height=150)
        self.textArea = tk.Text(self.frame)

        self.master.config(menu=self.menubar)
        self.frame.pack()
        self.textArea.pack()

    def Loop(self):
        self.master.mainloop()

    def Open_file(self):
        self.textArea.delete(1.0, tk.END)
        file = tkinter.filedialog.askopenfile(title="Please select a file to open", defaultextension='.txt',
                                              filetypes=[('text', '.txt')])
        self.textArea.insert(tk.END, file.read())

    def Save_file(self):
        text = self.textArea.get(1.0, tk.END)
        file = tkinter.filedialog.asksaveasfile(title="please choose file name and location", defaultextension='.txt',
                                                filetypes=[('text', '.txt')])
        file.write(text)


if __name__ == '__main__':
    print(variables.standalone)
    input()
