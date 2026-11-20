import tkinter as tk

def open_win_canvas(parent):
    win = tk.Toplevel(parent)
    win.title("Croquis de la zona")
    win.geometry("1280x720")

    tk.Label(win, text="Mapa de 1km a la redonda (Aprox. 10 cuadras)", font=("Arial", 12)).pack(pady=10)

    # Lienzo blanco más grande
    lienzo = tk.Canvas(win, width=450, height=350, bg="white")
    lienzo.pack()

    # 1. DIBUJAMOS LAS CALLES 
    # Usamos un 'for' para no escribir la misma línea 10 veces
    for x in range(50, 450, 80):
        lienzo.create_line(x, 0, x, 350, fill="lightgray", width=20) # Calles verticales
        
    for y in range(50, 350, 80):
        lienzo.create_line(0, y, 450, y, fill="lightgray", width=20) # Calles horizontales

    # 2. DIBUJAMOS EL TEC (En la esquina inferior izquierda)
    lienzo.create_rectangle(65, 265, 125, 325, fill="blue")
    lienzo.create_text(95, 295, text="Tec", fill="white", font=("Arial", 10, "bold"))

    # 3. DIBUJAMOS LA FONDA (En la esquina superior derecha)
    lienzo.create_rectangle(305, 25, 385, 65, fill="orange")
    lienzo.create_text(345, 45, text="Doña Mary", fill="black", font=("Arial", 10))

    # 4. EL RECORRIDO COMPLEto
    # create_line permite poner varios puntos: (x1, y1, x2, y2, x3, y3...)
    lienzo.create_line(
        130, 290,  # Sale del Tec
        210, 290,  # Camina a la derecha 2 cuadras
        210, 130,  # Sube 2 cuadras
        370, 130,  # Da vuelta a la derecha 2 cuadras
        370, 70,   # Sube media cuadra para llegar a la fonda
        fill="red", width=3, dash=(5, 5)
    )

    # Letreritos en el camino
    lienzo.create_text(250, 115, text="Atajo por el parque", fill="red")
    lienzo.create_text(160, 275, text="Inicio", fill="red")

    # Botón para cerrar
    tk.Button(win, text="Cerrar mapa", command=win.destroy).pack(pady=10)