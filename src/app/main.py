
import tkinter as tk
from tkinter import ttk
from app.win_home import open_win_home
from app.win_form import open_win_form
from app.win_list import open_win_list
from app.win_table import open_win_table
from app.win_canvas import open_win_canvas

def main():
    root = tk.Tk()
    root.title("Proyecto Integrador - MVP")
    root.geometry("1280x720")
    root.configure(bg="#FFF3E0")
    estilo = ttk.Style()
    estilo.theme_use("clam")
    estilo.configure("TFrame", background="#FFF3E0")
    estilo.configure("Menu.TButton", font=("Segoe UI", 11), padding=8, background="#F4A261", foreground="#3B2A1A")
    estilo.map("Menu.TButton", background=[("active", "#E76F51")], foreground=[("active", "#FFFFFF")])

    frame = ttk.Frame(root, padding=16)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="Fonda foráneo/fondáneo", font=("Segoe UI", 12, "bold")).pack(pady=(0, 12))
    ttk.Button(frame, text="1) Inicio", command=lambda: open_win_home(root)).pack(pady=4, fill="x")
    ttk.Button(frame, text="2) Configuración de preferencias", command=lambda: open_win_form(root)).pack(pady=10, fill="x")
    ttk.Button(frame, text="3) Favoritos", command=lambda: open_win_list(root)).pack(pady=10, fill="x")
    ttk.Button(frame, text="4) Catalogo de establecimientos", command=lambda: open_win_table(root)).pack(pady=10, fill="x")
    ttk.Button(frame, text="5) Mapa de establecimientos", command=lambda: open_win_canvas(root)).pack(pady=10, fill="x")
    ttk.Separator(frame).pack(pady=6, fill="x")
    ttk.Button(frame, text="Salir", command=root.destroy).pack(pady=6)

    root.mainloop()

if __name__ == "__main__":
    main()
  
    #se uso AI claude para comprender como escribir el código, sin embargo la redacción fue elaborada a mano y con ciertas correciones de retroalimentación