import tkinter as tk
from tkinter import ttk, messagebox
import csv
from pathlib import Path

def open_win_table(parent: tk.Tk):
    win = tk.Toplevel(parent)
    win.title("Catalogo de establecimientos")
    win.geometry("1280x720")
    frm = ttk.Frame(win, padding=24)
    frm.pack(fill="both", expand=True)
 #añadir label de título
    ttk.Label(frm, text="Catálogo de establecimientos", font=("Segoe UI", 14, "bold")).pack(pady=(0, 12))
    estilo = ttk.Style()
    estilo.theme_use("clam")
    estilo.configure("Treeview", rowheight=34, font=("Segoe UI", 11), background="#FFFFFF", fieldbackground="#1F4E79", foreground="#1D2B2A")
    estilo.configure("Treeview.Heading", font=("Segoe UI", 11, "bold"), background="#0F6B63", foreground="#FFFFFF")
    estilo.map("Treeview", background=[("selected", "#E8A317")], foreground=[("selected", "#000000")])
    cols = ("Nombre", "Tipo", "Precio_promedio", "Ubicación", "Promoción")
    tv = ttk.Treeview(frm, columns=cols, show="headings", height=10)
    for c in cols:
        tv.heading(c, text=c.capitalize())
        tv.column(c, width=120, anchor="center")
    tv.pack(fill="both", expand=True)

    ruta = Path(__file__).resolve().parents[2] / "data" / "sample.csv"  # <repo>/data/sample.csv
    if not ruta.exists():
        messagebox.showwarning("Aviso", f"No se encontró {ruta}. Crea el archivo de ejemplo.")
        return

    with open(ruta, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tv.insert("", "end", values=(row["Nombre"], row["Tipo"], row["Precio_promedio"], row["Ubicación"], row["Promoción"]))

    ttk.Button(frm, text="Cerrar", command=win.destroy).pack(pady=8, anchor="e")