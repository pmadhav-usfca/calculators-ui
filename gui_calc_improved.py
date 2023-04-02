import tkinter as tk
import math

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        
        # Create the input field
        self.input_field = tk.Entry(self.master, width=40)
        self.input_field.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        # Create the buttons
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "C", "+",
            "=", "sqrt", "sin", "cos", "tan"
        ]
        for i, button_text in enumerate(buttons):
            row = i // 4 + 1
            col = i % 4
            button = tk.Button(self.master, text=button_text, width=8, height=3)
            button.grid(row=row, column=col, padx=5, pady=5)
            button.bind("<Button-1>", self.button_clicked)
        
        # Initialize the calculator state
        self.expression = ""
        self.result = None
    
    def button_clicked(self, event):
        button = event.widget
        text = button["text"]
        
        if text == "C":
            self.expression = ""
            self.result = None
        elif text == "=":
            try:
                self.result = eval(self.expression)
                self.expression = str(self.result)
            except:
                self.result = "Error"
                self.expression = ""
        elif text == "sqrt":
            try:
                self.result = math.sqrt(float(self.expression))
                self.expression = str(self.result)
            except:
                self.result = "Error"
                self.expression = ""
        elif text in ["sin", "cos", "tan"]:
            try:
                value = float(self.expression)
                if text == "sin":
                    self.result = math.sin(value)
                elif text == "cos":
                    self.result = math.cos(value)
                elif text == "tan":
                    self.result = math.tan(value)
                self.expression = str(self.result)
            except:
                self.result = "Error"
                self.expression = ""
        else:
            self.expression += text
        
        self.input_field.delete(0, tk.END)
        self.input_field.insert(0, self.expression)
    
    def run(self):
        self.master.mainloop()

root = tk.Tk()
app = CalculatorApp(root)
app.run()
