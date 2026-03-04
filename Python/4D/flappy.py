import tkinter as tk

def somma():
    try:
        a = float(campo_a.get())
        b = float(campo_b.get())
        risultato_var.set(f"Risultato: {a + b}")
    except ValueError:
        risultato_var.set("Inserisci numeri validi!")

finestra = tk.Tk()
finestra.title("Sommatore")
finestra.geometry("300x200")

tk.Label(finestra, text="Primo numero:").grid(row=0, column=0, pady=5)
campo_a = tk.Entry(finestra)
campo_a.grid(row=0, column=1)

tk.Label(finestra, text="Secondo numero:").grid(row=1, column=0, pady=5)
campo_b = tk.Entry(finestra)
campo_b.grid(row=1, column=1)

tk.Button(finestra, text="Somma", command=somma, bg="blue", fg="white").grid(row=2, column=0, columnspan=2, pady=10)

risultato_var = tk.StringVar()
tk.Label(finestra, textvariable=risultato_var, font=("Arial", 13)).grid(row=3, column=0, columnspan=2)

finestra.mainloop()