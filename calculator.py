import tkinter as tk
from tkinter import messagebox
import math

class WindowsCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("320x500")
        self.root.configure(bg="#202020")

        self.expression = ""
        
        # Display Screen
        self.display_var = tk.StringVar(value="0")
        self.create_widgets()

    def create_widgets(self):
        # Result Display Area
        display_frame = tk.Frame(self.root, bg="#202020", pady=20)
        display_frame.pack(expand=True, fill="both")

        self.label = tk.Label(
            display_frame, textvariable=self.display_var, 
            anchor="e", bg="#202020", fg="white", 
            font=("Segoe UI", 40, "bold"), padx=10
        )
        self.label.pack(expand=True, fill="both")

        # Button Container
        button_frame = tk.Frame(self.root, bg="#202020")
        button_frame.pack(expand=True, fill="both")

        # Define buttons (Text, Row, Column, Color Type)
        buttons = [
            ('%', 0, 0, 'special'), ('CE', 0, 1, 'special'), ('C', 0, 2, 'special'), ('⌫', 0, 3, 'special'),
            ('1/x', 1, 0, 'special'), ('x²', 1, 1, 'special'), ('²√x', 1, 2, 'special'), ('÷', 1, 3, 'op'),
            ('7', 2, 0, 'num'), ('8', 2, 1, 'num'), ('9', 2, 2, 'num'), ('×', 2, 3, 'op'),
            ('4', 3, 0, 'num'), ('5', 3, 1, 'num'), ('6', 3, 2, 'num'), ('-', 3, 3, 'op'),
            ('1', 4, 0, 'num'), ('2', 4, 1, 'num'), ('3', 4, 2, 'num'), ('+', 4, 3, 'op'),
            ('+/-', 5, 0, 'num'), ('0', 5, 1, 'num'), ('.', 5, 2, 'num'), ('=', 5, 3, 'eq'),
        ]

        # Colors
        colors = {
            'num': '#3b3b3b',    # Dark gray for numbers
            'op': '#323232',     # Slightly darker for operators
            'special': '#323232', # Special functions
            'eq': '#00eee7',     # Cyan for equals button
            'text': 'white',
            'eq_text': 'black'
        }

        # Create Buttons using a grid
        for (text, row, col, btype) in buttons:
            bg_color = colors[btype]
            fg_color = colors['eq_text'] if btype == 'eq' else colors['text']
            
            btn = tk.Button(
                button_frame, text=text, font=("Segoe UI", 12),
                bg=bg_color, fg=fg_color, borderwidth=0,
                activebackground="#505050", activeforeground="white",
                command=lambda t=text: self.on_button_click(t)
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)

        # Configure grid weights so buttons expand equally
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)
        for i in range(6):
            button_frame.grid_rowconfigure(i, weight=1)

    def on_button_click(self, char):
        current_text = self.display_var.get()

        try:
            if char == "C" or char == "CE":
                self.expression = ""
                self.display_var.set("0")
            
            elif char == "⌫":
                self.expression = self.expression[:-1]
                self.display_var.set(self.expression if self.expression else "0")

            elif char == "=":
                # Replace visual symbols with python operators
                expr = self.expression.replace('×', '*').replace('÷', '/')
                result = eval(expr)
                # Format to remove .0 if it's an integer
                self.display_var.set(f"{result:g}")
                self.expression = str(result)

            elif char == "x²":
                res = float(current_text) ** 2
                self.display_var.set(f"{res:g}")
                self.expression = str(res)

            elif char == "²√x":
                res = math.sqrt(float(current_text))
                self.display_var.set(f"{res:g}")
                self.expression = str(res)

            elif char == "1/x":
                res = 1 / float(current_text)
                self.display_var.set(f"{res:g}")
                self.expression = str(res)

            elif char == "+/-":
                res = float(current_text) * -1
                self.display_var.set(f"{res:g}")
                self.expression = str(res)

            else:
                # Basic input logic
                if current_text == "0" and char not in "+-×÷":
                    self.expression = char
                else:
                    self.expression += char
                self.display_var.set(self.expression)

        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero")
            self.clear_all()
        except Exception:
            messagebox.showerror("Error", "Invalid Input")
            self.clear_all()

    def clear_all(self):
        self.expression = ""
        self.display_var.set("0")

if __name__ == "__main__":
    root = tk.Tk()
    app = WindowsCalculator(root)
    root.mainloop()