import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.configure(bg='#1C1C1C')
        master.resizable(False, False)

        # Configure fonts
        self.display_font = ('Helvetica', 24, 'bold')
        self.button_font = ('Helvetica', 14)

        # Create display
        self.display = tk.Entry(master, width=9, font=self.display_font, bg='#1C1C1C', fg='white', bd=0, justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=(40, 20), sticky='nsew')
        self.display.insert(0, "0")

        # Define buttons
        buttons = [
            ('C', '#A5A5A5'), ('±', '#A5A5A5'), ('%', '#A5A5A5'), ('÷', '#FF9F0A'),
            ('7', '#333333'), ('8', '#333333'), ('9', '#333333'), ('×', '#FF9F0A'),
            ('4', '#333333'), ('5', '#333333'), ('6', '#333333'), ('-', '#FF9F0A'),
            ('1', '#333333'), ('2', '#333333'), ('3', '#333333'), ('+', '#FF9F0A'),
            ('0', '#333333'), ('.', '#333333'), ('=', '#FF9F0A')
        ]

        # Add buttons to interface
        row = 1
        col = 0
        for (text, color) in buttons:
            btn = tk.Button(master, text=text, width=11 if text == '0' else 5, height=2, font=self.button_font, bg=color, 
                fg='white' if color != '#A5A5A5' else 'black', bd=0, command=lambda x=text: self.click(x))

            btn.grid(row=row, column=col, columnspan=2 if text == '0' else 1, padx=2, pady=2, sticky='nsew')

            col += 2 if text == '0' else 1
                
            if col > 3:
                col = 0
                row += 1

        # Configure row and column weights
        for i in range(6): master.grid_rowconfigure(i, weight=1)
        for i in range(4): master.grid_columnconfigure(i, weight=1)

    def click(self, key):
        if key == 'C':
            self.display.delete(0, tk.END)
            self.display.insert(0, "0")
        elif key == '±':
            current = self.display.get()
            if current.startswith('-'):
                self.display.delete(0)
            else:
                self.display.insert(0, '-')
        elif key == '%':
            current = float(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, str(current / 100))
        elif key == '=':
            try:
                result = eval(self.display.get().replace('×', '*').replace('÷', '/'))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            if self.display.get() == "0" or self.display.get() == "Error":
                self.display.delete(0, tk.END)
            self.display.insert(tk.END, key)

if __name__ == "__main__":
    root = tk.Tk()
    my_calculator = Calculator(root)
    root.mainloop()