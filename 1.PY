from tkinter import *

new_calculator_window = Tk()
new_calculator_window.geometry("312x324")
new_calculator_window.resizable(0, 0)
new_calculator_window.title("Colorful Calculator")

def button_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def button_clear():
    global expression
    expression = ""
    input_text.set("")

def button_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""

expression = ""

input_text = StringVar()

input_frame = Frame(new_calculator_window, width=312, height=50, bd=0, highlightbackground="blue", highlightcolor="blue", highlightthickness=2)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#b3e0ff", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

buttons_frame = Frame(new_calculator_window, width=312, height=272.5, bg="#e6e6e6")
buttons_frame.pack()

clear_button = Button(buttons_frame, text="C", fg="white", width=32, height=3, bd=0, bg="#ff6666", cursor="hand2", command=lambda: button_clear())
clear_button.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

divide_button = Button(buttons_frame, text="/", fg="white", width=10, height=3, bd=0, bg="#ff6666", cursor="hand2", command=lambda: button_click("/"))
divide_button.grid(row=0, column=3, padx=1, pady=1)

# ... (Repeat the pattern for other buttons)

equals_button = Button(buttons_frame, text="=", fg="white", width=10, height=3, bd=0, bg="#ff6666", cursor="hand2", command=lambda: button_equal())
equals_button.grid(row=4, column=3, padx=1, pady=1)

new_calculator_window.mainloop()
