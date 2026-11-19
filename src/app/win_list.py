import tkinter as tk
from tkinter import ttk, messagebox

def open_win_list(parent):
    # 1. Configuración de la ventana
    win = tk.Toplevel(parent)
    win.title("Mis Establecimientos Favoritos")
    win.geometry("450x320")

    # Marco principal para darle márgenes
    frm = ttk.Frame(win, padding=15)
    frm.pack(fill="both", expand=True)

    # 2. Instrucciones para el usuario
    ttk.Label(
        frm, 
        text="Guarda aquí los restaurantes, puestos o cafeterías que te gustaron:", 
        font=("Arial", 10, "bold")
    ).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))

    # 3. La lista donde se verán los favoritos
    lista_favoritos = tk.Listbox(frm, height=10, font=("Arial", 10))
    lista_favoritos.grid(row=1, column=0, rowspan=4, sticky="nsew", padx=(0, 10))
    
    # Esto hace que la lista se expanda 
    frm.columnconfigure(0, weight=1)
    frm.rowconfigure(1, weight=1)

    # Ejemplos
    lista_favoritos.insert("end", "Fonda Doña Mary")
    lista_favoritos.insert("end", "Tacos de canasta del centro")

    # 4. Caja de texto 
    entrada_lugar = ttk.Entry(frm, font=("Arial", 10))
    entrada_lugar.grid(row=1, column=1, sticky="ew")

    
    # FUNCIONES 
    

    def agregar_favorito():
        
        nuevo_lugar = entrada_lugar.get().strip() 
        
        if nuevo_lugar: 
            lista_favoritos.insert("end", nuevo_lugar)
            entrada_lugar.delete(0, "end") 
        else:
            messagebox.showwarning("Aviso", "Escribe el nombre del establecimiento para agregarlo.")

    def eliminar_favorito():
        seleccion = lista_favoritos.curselection()
        if seleccion: 
            lista_favoritos.delete(seleccion[0])
        else:
            messagebox.showinfo("Aviso", "Primero selecciona un lugar de la lista para eliminarlo.")

    def limpiar_lista():
        
        respuesta = messagebox.askyesno("Confirmar", "¿Seguro que quieres vaciar todos tus favoritos?")
        if respuesta:
            lista_favoritos.delete(0, "end")

# BOTONES
    ttk.Button(frm, text="⭐ Agregar", command=agregar_favorito).grid(row=2, column=1, sticky="ew", pady=4)
    ttk.Button(frm, text="❌ Eliminar seleccionado", command=eliminar_favorito).grid(row=3, column=1, sticky="ew", pady=4)
    ttk.Button(frm, text="🗑️ Vaciar lista", command=limpiar_lista).grid(row=4, column=1, sticky="ew", pady=4)

    # Botón de cerrar (Arreglé la línea que se te cortó)
    ttk.Button(frm, text="Cerrar", command=win.destroy).grid(row=5, column=0, columnspan=2, pady=10, sticky="e")