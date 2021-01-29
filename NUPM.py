import tkinter as tk
from tkinter import filedialog, ttk
import os
import pickle
from tkinter import messagebox
import pyperclip


def show():
    '''copy password on clipboard'''
    iDir = os.path.abspath(os.path.dirname(__file__))
    file = tk.filedialog.askopenfilename()
    if not file:
        return
    key = txt.get()
    if key == "":
        messagebox.showinfo(message="Please Input Passcode")
        return
    plaintxt = ""
    i = 0
    k = 0
    pw = []
    plain = ""
    with open(file, "rb") as fp:
        pwlist = pickle.load(fp)
        for ch in pwlist:
            pw.append(ch ^ ord(key[i]))
            i += 1
            if i == len(key):
                i = 0
    pwl = list(map(chr, pw))
    plaintxt = ''.join(pwl)
    pyperclip.copy(plaintxt)


def hide():
    '''encrypt password XOR'''
    masterkey = txt.get()
    if key == "":
        messagebox.showinfo(message="KEY is NEED 1 character!")
        return
    if len(masterkey) <= 8:
        messagebox.showinfo(message="NOTICE:password Too short.\n NEVER USED IMPORTANT PASSWORD!")
    iDir = os.path.abspath(os.path.dirname(__file__))
    file = tk.filedialog.asksaveasfilename()
    wrt = file + ".pckl"
    if file == "":
        return
    cryptxt = ""
    i = 0
    k = 0
    s = []
    b = key.get()
    cryptxt = ""
    p = []
    b = list(b)
    for ch in b:
        s.append(ord(ch) ^ ord(masterkey[i]))
        if not b:
            break
        i += 1
        if i == len(masterkey):
            i = 0
    with open(wrt, mode="wb") as wfp:
        pickle.dump(s, wfp)


if __name__ == '__main__':
    root = tk.Tk()
    pwd = tk.Label(text='マスターパスワード')
    pwd.pack()
    txt = tk.Entry(width=128)
    txt.pack()
    masterpass = tk.Label(text='パスワード')
    masterpass.pack()
    key = tk.Entry(width=128)
    key.pack()
    cbutton = tk.Button(text="crypt!", command=hide)
    cbutton.pack()
    button = tk.Button(text="decrypt!", command=show)
    button.pack()
    root.mainloop()
