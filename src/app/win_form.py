import tkinter as tk
from tkinter import ttk, messagebox

def open_win_form(parent):
    # 1. Configuración de la ventana
    win = tk.Toplevel(parent)
    win.title("Filtro de Búsqueda de Comida")
    win.geometry("400x500") # La hicimos más alta para que quepa todo
    
    # Marco principal para tener márgenes
    frm = ttk.Frame(win, padding=20)
    frm.pack(fill="both", expand=True)

    
    # CAMPOS DEL FORMULARIO
    

    # 1. Presupuesto (Caja de texto)
    ttk.Label(frm, text="Presupuesto máximo (\$):").grid(row=0, column=0, sticky="w", pady=5)
    ent_presupuesto = ttk.Entry(frm, width=15)
    ent_presupuesto.grid(row=0, column=1, sticky="w", pady=5)

    # 2. Zona de búsqueda (Menú desplegable)
    ttk.Label(frm, text="Zona de búsqueda:").grid(row=1, column=0, sticky="w", pady=5)
    zonas = ["Cerca del Tec", "Plaza Mayor", "Centro", "San Martín"]
    cmb_zona = ttk.Combobox(frm, values=zonas, state="readonly", width=17)
    cmb_zona.grid(row=1, column=1, sticky="w", pady=5)

    # 3. Tipos de comida (Casillas de selección)
    ttk.Label(frm, text="Tipo de comida:").grid(row=2, column=0, sticky="nw", pady=10)
    
    # Creamos un marquito invisible solo para agrupar las casillas
    frm_tipos = ttk.Frame(frm)
    frm_tipos.grid(row=2, column=1, sticky="w", pady=10)

    # Variables para saber si están marcadas (True/False)
    var_mex = tk.BooleanVar()
    var_ita = tk.BooleanVar()
    var_jap = tk.BooleanVar()
    var_rap = tk.BooleanVar()
    var_sal = tk.BooleanVar()

    ttk.Checkbutton(frm_tipos, text="Mexicana", variable=var_mex).pack(anchor="w")
    ttk.Checkbutton(frm_tipos, text="Italiana", variable=var_ita).pack(anchor="w")
    ttk.Checkbutton(frm_tipos, text="Japonesa", variable=var_jap).pack(anchor="w")
    ttk.Checkbutton(frm_tipos, text="Rápida", variable=var_rap).pack(anchor="w")
    ttk.Checkbutton(frm_tipos, text="Saludable", variable=var_sal).pack(anchor="w")

    # 4. Preferencias alimenticias (Casillas de selección)
    ttk.Label(frm, text="Preferencias:").grid(row=3, column=0, sticky="nw", pady=10)
    
    frm_pref = ttk.Frame(frm)
    frm_pref.grid(row=3, column=1, sticky="w", pady=10)

    var_veg = tk.BooleanVar()
    var_vgn = tk.BooleanVar()
    var_glu = tk.BooleanVar()

    ttk.Checkbutton(frm_pref, text="Vegetariana", variable=var_veg).pack(anchor="w")
    ttk.Checkbutton(frm_pref, text="Vegana", variable=var_vgn).pack(anchor="w")
    ttk.Checkbutton(frm_pref, text="Sin gluten", variable=var_glu).pack(anchor="w")