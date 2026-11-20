import tkinter as tk
from tkinter import messagebox

def open_win_home(parent):
    win = tk.Toplevel(parent)
    win.title("Inicio - Ruta Foránea")
    win.geometry("1280x720")
    
    # Título 
    tk.Label(win, text="Ruta Foránea", font=("Arial", 16, "bold")).pack(pady=15)
    tk.Label(win, text="Encuentra comida económica cerca del Tec.").pack(pady=5)

    # Funciones de los mensajes
    def buscar():
        messagebox.showinfo("Búsqueda", "Buscando comida de $60 a $80 pesos...")

    def promos():
        messagebox.showinfo("Promos", "Hoy: 2x1 en chilaquiles en Doña Mary")

    # Botones con colores 
    tk.Button(win, text="Buscar comida barata", bg="green", fg="white", command=buscar).pack(fill="x", padx=40, pady=10)
    
    tk.Button(win, text="Ver promociones", bg="orange", command=promos).pack(fill="x", padx=40, pady=10)

    # Botón para cerrar
    tk.Button(win, text="Cerrar ventana", command=win.destroy).pack(pady=20)
    #se uso AI claude para comprender como escribir el código, sin embargo la redacción fue elaborada a mano y con ciertas correciones de retroalimentación