import tkinter as tk

def btn_click(value):
    entry.insert(tk.END, value)

def clear_all():
    entry.delete(0, tk.END)

def clear_entry():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Window setup
root = tk.Tk()
root.title("Compact Calculator")
root.geometry("300x400")  # Smaller size
root.resizable(False, False)

# Entry field
entry = tk.Entry(root, font=("Arial", 20), bd=8, relief="sunken", justify="right")
entry.pack(padx=10, pady=10, fill="both", ipady=10)

# Button frame
btn_frame = tk.Frame(root)
btn_frame.pack(padx=5, pady=5)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['C', 'CE']
]

# Create smaller buttons
for r, row in enumerate(buttons):
    for c, text in enumerate(row):
        if text == '=':
            cmd = calculate
        elif text == 'C':
            cmd = clear_all
        elif text == 'CE':
            cmd = clear_entry
        else:
            cmd = lambda x=text: btn_click(x)

        btn = tk.Button(btn_frame, text=text, font=("Arial", 12), width=5, height=2,
                        command=cmd)
        btn.grid(row=r, column=c, padx=2, pady=2)

root.mainloop()
