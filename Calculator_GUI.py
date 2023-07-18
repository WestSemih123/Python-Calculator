import sys
from math import *
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Hesap Makinesi")

def inputs():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = entry3.get()
    except ValueError:
        messagebox.showinfo("Hata", "Bu bir sayı değil.")
        sys.exit()

    if op == "+" or op == "-" or op == "*" or op == "/" or op == "pow" or op == "sqrt" or op == "fac":
        if op == "sqrt":
            deger = sqrt(num1)
        elif op == "fac":
            deger = factorial(num1)
        elif op == "pow":
            deger = pow(num1, num2)
        elif op == "-":
            deger = num1 - num2
        elif op == "+":
            deger = num1 + num2
        elif op == "*":
            deger = num1 * num2
        elif op == "/":
            deger = num1 / num2 
        else:
            print("Geçersiz operatör.")
            sys.exit()
    else:
        print("Geçersiz operatör.")
        sys.exit()

    label2.config(text=deger)

label = tk.Label(window, text="If you want to do raise to power of number use pow.\n" + "If you want to do square root use sqrt.\n" + "If you want to do factorial use fac.")
label.grid()

entry1 = tk.Entry(window)
entry1.insert(0, "Sayı 1")
entry1.grid()

entry2 = tk.Entry(window)
entry2.insert(0, "Sayı 2")
entry2.grid()

entry3 = tk.Entry(window)
entry3.insert(0, "Operatör")
entry3.grid()

button3 = tk.Button(window, text="Send", command=inputs)
button3.grid()

label2 = tk.Label(window, text="")
label2.grid(column=0, row=6, columnspan=2)

window.mainloop()
