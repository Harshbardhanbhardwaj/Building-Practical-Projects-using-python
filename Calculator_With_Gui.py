import tkinter as tk
from tkinter import ttk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(True, True)

        self.expression = ""   # stores input expression
        self.display_text = tk.StringVar()

        # ===== Display Frame =====
        display_frame = ttk.Frame(root)
        display_frame.pack(fill=tk.BOTH, expand=True)

        display_label = ttk.Label(
            display_frame, 
            textvariable=self.display_text, 
            font=("Arial", 26), 
            anchor='e',          # text aligned right
            background='white',
            foreground='black',
            padding=6
        )
        display_label.pack(fill=tk.BOTH, expand=True)

        # ===== Button Frame =====
        button_frame = ttk.Frame(self.root)
        button_frame.pack(fill=tk.BOTH, expand=True)
        
        self.create_buttons(button_frame)

    def create_buttons(self, frame):
        # Buttons layout (4x5 grid)
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C'
        ]

        for i, text in enumerate(buttons):
            row, col = divmod(i, 4)  # 4 buttons per row
            button = ttk.Button(frame, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
        
        # Make the grid expandable
        for i in range(4):
            frame.columnconfigure(i, weight=1)
        for i in range(5):  # 5 rows including 'C'
            frame.rowconfigure(i, weight=1)

    def on_button_click(self, text):
        if text == "=":
            try:
                result = str(eval(self.expression))  # evaluate math expression
                self.display_text.set(result)
                self.expression = result
            except Exception:
                self.display_text.set("Error")
                self.expression = ""
        elif text == "C":   # Clear screen
            self.expression = ""
            self.display_text.set("")
        else:
            self.expression += str(text)   # append button text
            self.display_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
