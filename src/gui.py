import tkinter as tk
from tkinter import filedialog, messagebox
from generator import generate_passwords

def export_wordlist(wordlist):
    filepath = filedialog.asksaveasfilename(defaultextension=".lst", filetypes=[("Text files", "*.lst")])
    if filepath:
        with open(filepath, "w", encoding="utf-8") as f:
            for pw in wordlist:
                f.write(pw + "\n")
        messagebox.showinfo("Exported", f"Wordlist saved to:\n{filepath}")

def run_generator():
    size = int(size_slider.get())
    mutate_flag = mutate_var.get()
    wordlist = generate_passwords(size=size, mutate_flag=mutate_flag)
    preview.delete(1.0, tk.END)
    preview.insert(tk.END, "\n".join(wordlist[:20]))
    export_wordlist(wordlist)

root = tk.Tk()
root.title("NepalPassForge - Nepali Password Generator")

tk.Label(root, text="Wordlist Size").grid(row=0, column=0)
size_slider = tk.Scale(root, from_=1000, to=10000000, orient=tk.HORIZONTAL, length=300)
size_slider.set(100000)
size_slider.grid(row=0, column=1)

mutate_var = tk.BooleanVar()
tk.Checkbutton(root, text="Enable Mutation (Leetspeak)", variable=mutate_var).grid(row=1, column=1)

tk.Button(root, text="Generate & Export", command=run_generator).grid(row=2, column=1)

tk.Label(root, text="Preview (first 20 passwords):").grid(row=3, column=0)
preview = tk.Text(root, height=10, width=50)
preview.grid(row=4, column=0, columnspan=2)

root.mainloop()