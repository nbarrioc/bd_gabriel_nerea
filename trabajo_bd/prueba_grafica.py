# %%
# Te dejo aquí un ejemplo de cómo sería gráfico. Solo está la primera 
# consulta
# No preguntes qué significa nada. Ni idea. Pura IA
import tkinter as tk
from tkinter import ttk, messagebox
from connection import get_connection
import queries

def run_query_1ai():
    try:
        total = queries.query_1ai(conn)
        output_var.set(f"Número total de fármacos: {total}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Conexión una vez
conn = get_connection()

root = tk.Tk()
root.title("Base de datos de fármacos")

main_frame = ttk.Frame(root, padding=10)
main_frame.pack(fill="both", expand=True)

btn_1ai = ttk.Button(main_frame, text="Número total de fármacos", command=run_query_1ai)
btn_1ai.grid(row=0, column=0, padx=5, pady=5, sticky="w")

output_var = tk.StringVar()
output_label = ttk.Label(main_frame, textvariable=output_var, wraplength=400, justify="left")
output_label.grid(row=1, column=0, columnspan=2, sticky="w")

root.mainloop()

conn.close()
# %%
