import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.display = tk.Entry(master, width=30, justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Create buttons
        button_1 = self.create_button(1)
        button_2 = self.create_button(2)
        button_3 = self.create_button(3)
        button_4 = self.create_button(4)
        button_5 = self.create_button(5)
        button_6 = self.create_button(6)
        button_7 = self.create_button(7)
        button_8 = self.create_button(8)
        button_9 = self.create_button(9)
        button_0 = self.create_button(0)
        button_add = self.create_button("+")
        button_subtract = self.create_button("-")
        button_multiply = self.create_button("*")
        button_divide = self.create_button("/")
        button_clear = tk.Button(master, text="C", width=5, height=2, command=self.clear)
        button_equals = tk.Button(master, text="=", width=5, height=2, command=self.calculate)

        # Position buttons
        button_1.grid(row=1, column=0)
        button_2.grid(row=1, column=1)
        button_3.grid(row=1, column=2)
        button_add.grid(row=1, column=3)
        button_4.grid(row=2, column=0)
        button_5.grid(row=2, column=1)
        button_6.grid(row=2, column=2)
        button_subtract.grid(row=2, column=3)
        button_7.grid(row=3, column=0)
        button_8.grid(row=3, column=1)
        button_9.grid(row=3, column=2)
        button_multiply.grid(row=3, column=3)
        button_clear.grid(row=4, column=0)
        button_0.grid(row=4, column=1)
        button_equals.grid(row=4, column=2)
        button_divide.grid(row=4, column=3)

    def create_button(self, num):
        return tk.Button(self.master, text=str(num), width=5, height=2, command=lambda:self.add_to_display(str(num)))

    def add_to_display(self, value):
        self.display.insert("end", value)

    def clear(self):
        self.display.delete(0, "end")

    def calculate(self):
        try:
            result = eval(self.display.get())
            self.clear()
            self.add_to_display(result)
        except:
            self.clear()
            self.add_to_display("Error")

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
