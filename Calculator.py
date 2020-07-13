from tkinter import *

window = Tk()
window.geometry("500x250")
window.title("Calculator")
window.configure(bg="black")


def button_click(value):
    old = display_field.get()
    display_field.delete(0, END)
    display_field.insert(0, str(old) + str(value))


def button_clear():
    display_field.delete(0, END)


def button_add():
    return


def button_sub():
    return


def button_mul():
    return


def button_div():
    return


def button_equal():
    return


label = Label(window, text="welcome", bg="blue")
# output field declaration
display_field = Entry(window, width=65, borderwidth=3, bg="grey", fg="orange")
# clear button declaration
button_clr = Button(text=" Clear ", width="8", height="1", bg="black", fg="grey", command=button_clear)
# operand declaration
button1 = Button(text=" 1 ", width="10", height="2", padx=5, pady=5, bg="orange", command=lambda: button_click(1))
button2 = Button(text=" 2 ", width="10", height="2", padx=5, pady=5, bg="orange", command=lambda: button_click(2))
button3 = Button(text=" 3 ", width="10", height="2", padx=5, pady=5, bg="orange", command=lambda: button_click(3))
button4 = Button(text=" 4 ", width="10", height="2", padx=5, pady=5, bg="orange", command=lambda: button_click(4))
button5 = Button(text=" 5 ", width="10", height="2", padx=5, pady=5, bg="orange", command=lambda: button_click(5))
button6 = Button(text=" 6 ", width="10", height="2", padx=5, pady=5, bg="orange", command=lambda: button_click(6))
button7 = Button(text=" 7 ", width="10", height="2", padx=5, pady=5, bg="orange", command=lambda: button_click(7))
button8 = Button(text=" 8 ", width="10", height="2", padx=5, pady=5, bg="orange", command=lambda: button_click(8))
button9 = Button(text=" 9 ", width="10", height="2", padx=5, pady=5, bg="orange", command=lambda: button_click(9))
button0 = Button(text=" 0 ", width="10", height="2", padx=5, pady=5, bg="orange", command=lambda: button_click(0))
button_dot = Button(text=" .", width="10", height="2", padx=5, pady=5, bg="orange", command=lambda: button_click())
# operator declaration
btn_plus = Button(text=" + ", width="10", height="2", padx=5, pady=5, bg="brown", command=lambda: button_add())
btn_Sub = Button(text=" - ", width="10", height="2", padx=5, pady=5, bg="brown", command=lambda: button_sub())
btn_mul = Button(text=" X ", width="10", height="2", padx=5, pady=5, bg="brown", command=lambda: button_mul())
btn_div = Button(text=" / ", width="10", height="2", padx=5, pady=5, bg="brown", command=lambda: button_div())
btn_equ = Button(text=" = ", width="10", height="2", padx=5, pady=5, bg="brown", command=lambda: button_equal())

display_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
button_clr.grid(row=0, column=5)

button0.grid(row=6, column=0)
button_dot.grid(row=6, column=1)
btn_equ.grid(row=6, column=2)
btn_plus.grid(row=6, column=3)

button1.grid(row=5, column=0)
button2.grid(row=5, column=1)
button3.grid(row=5, column=2)
btn_Sub.grid(row=5, column=3)

button4.grid(row=4, column=0)
button5.grid(row=4, column=1)
button6.grid(row=4, column=2)
btn_mul.grid(row=4, column=3)

button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
btn_div.grid(row=3, column=3)

window.mainloop()
