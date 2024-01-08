import tkinter as tk
import onetimepad

root = tk.Tk()
root.title("Szyfrowanie")
root.geometry("430x100")


def encryptMessage():
    pt = e1.get()
    ct = onetimepad.encrypt(pt, 'random')
    e2.insert(0, ct)


def decryptMessage():
    ct1 = e3.get()
    pt1 = onetimepad.decrypt(ct1, 'random')
    e4.insert(0, pt1)


label1 = tk.Label(root, text='plane text')
label1.grid(row=10, column=1)

label2 = tk.Label(root, text='szyfrowany text')
label2.grid(row=11, column=1)

label3 = tk.Label(root, text='cipher text')
label3.grid(row=10, column=10)

label4 = tk.Label(root, text='deszyfrowany text')
label4.grid(row=11, column=10)

e1 = tk.Entry(root)
e1.grid(row=10, column=2)

e2 = tk.Entry(root)
e2.grid(row=11, column=2)

e3 = tk.Entry(root)
e3.grid(row=10, column=11)

e4 = tk.Entry(root)
e4.grid(row=11, column=11)

ent = tk.Button(root, text="szyfrowanie", bg="red",
                fg="white", command=encryptMessage)
ent.grid(row=13, column=2)
b2 = tk.Button(root, text="deszyfrowanie", bg="green",
               fg="white", command=decryptMessage)
b2.grid(row=13, column=11)

root.mainloop()
