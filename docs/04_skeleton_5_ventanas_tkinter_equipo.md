# Documentación técnica — Proyecto Sesion3

**Tipo de proyecto:** aplicación de escritorio en Python con Tkinter  
**Origen de la documentación:** análisis del código fuente incluido en `Sesion3.zip`  
**Fecha de análisis:** 10 de noviembre de 2026

## 1. Resumen ejecutivo

`Sesion3` es una aplicación de demostración de interfaces gráficas con Python y la biblioteca estándar `tkinter`. La ventana principal permite abrir cinco módulos independientes: bienvenida, formulario, lista, tabla y dibujo. El proyecto utiliza controles de `tkinter` y `tkinter.ttk`; para la tabla incorpora la biblioteca estándar `csv`.

**Estado identificado mediante análisis estático:** el código Python tiene una organización simple y adecuada para una demostración, pero la ventana de tabla apunta a una ruta distinta de la ubicación real del CSV. No se ejecutó la interfaz gráfica; las observaciones se basan en la revisión del código del ZIP.

## 2. Estructura de archivos

```text
Sesion3/
├── .vscode/
│   └── launch.json
├── docs/                     # Vacío en el ZIP
└── src/
    ├── app/
    │   ├── main.py            # Ventana principal
    │   ├── win_home.py        # Bienvenida
    │   ├── win_form.py        # Formulario y guardado TXT
    │   ├── win_list.py        # Lista de elementos
    │   ├── win_table.py       # Tabla CSV
    │   ├── win_canvas.py      # Dibujos con Canvas
    │   └── __pycache__/       # Bytecode generado por Python
    ├── core/                  # Vacío en el ZIP
    ├── data/
    │   └── sample.csv        # Datos de ejemplo
    └── tests/                 # Vacío en el ZIP
```

No se incluyeron archivos de dependencias (`requirements.txt`, `pyproject.toml`) ni pruebas automatizadas. No se identificaron bibliotecas de terceros en los archivos Python revisados.

## 3. Arquitectura y flujo de ejecución

```text
main.py
   └── Ventana raíz: tk.Tk()
         ├── Botón Bienvenida → open_win_home(root)
         ├── Botón Formulario → open_win_form(root)
         ├── Botón Lista      → open_win_list(root)
         ├── Botón Tabla      → open_win_table(root) → sample.csv
         ├── Botón Canvas     → open_win_canvas(root)
         └── Botón Salir      → root.destroy()
```

Cada módulo exporta una función `open_win_...(parent)` que abre una ventana secundaria con `tk.Toplevel(parent)`. La ventana principal inicia el ciclo de eventos de Tkinter mediante `root.mainloop()`.

### Conceptos de Tkinter usados

- `tk.Tk()`: ventana raíz de la aplicación.
- `tk.Toplevel(parent)`: ventana independiente asociada a la raíz.
- `ttk.Frame`, `ttk.Label`, `ttk.Button`, `ttk.Entry`: controles gráficos.
- `pack()` y `grid()`: administradores de disposición de controles; cada módulo los usa en contenedores apropiados.
- `command=...`: conecta un botón con una función de Python.
- `messagebox`: mensajes informativos, advertencias y errores.

## 4. Análisis detallado del código

### 4.1. `src/app/main.py`

**Propósito:** construir el menú principal y conectar los cinco módulos.

**Importaciones:** `tkinter as tk`, `ttk` y las funciones `open_win_home`, `open_win_form`, `open_win_list`, `open_win_table` y `open_win_canvas`.

**Función:** `main()`.

**Secuencia:**
1. Crea una ventana raíz con `root = tk.Tk()`.
2. Define el título `Proyecto Integrador - MVP` y el tamaño inicial `420x340`.
3. Crea un `ttk.Frame` y una etiqueta introductoria.
4. Crea cinco botones, cada uno con un `command=lambda: open_win_...(root)`.
5. Crea el botón de salida con `command=root.destroy`.
6. Llama a `root.mainloop()`.

La condición `if __name__ == "__main__": main()` evita iniciar la aplicación automáticamente si el módulo se importa desde otro archivo.

### 4.2. `src/app/win_home.py`

**Propósito:** mostrar una pantalla de bienvenida.

**Función:** `open_win_home(parent: tk.Tk)`.

Crea un `tk.Toplevel`, muestra dos etiquetas y dos botones. El botón **Mostrar mensaje** invoca `messagebox.showinfo("Info", "¡Equipo listo!")`; **Cerrar** destruye exclusivamente esa ventana mediante `win.destroy`.

**Características:** no recibe información del usuario, no almacena datos y no depende de archivos.

### 4.3. `src/app/win_form.py`

**Propósito:** capturar un nombre y una edad y guardarlos en un archivo de texto.

**Función pública:** `open_win_form(parent: tk.Tk)`.  
**Función interna:** `validar_y_guardar()`.

**Controles:** dos etiquetas, dos entradas `ttk.Entry`, botón **Guardar** y botón **Cerrar**. La distribución se organiza con `grid()`.

**Flujo al guardar:**
1. Lee `ent_nombre.get().strip()` y `ent_edad.get().strip()`.
2. Si el nombre está vacío, muestra `messagebox.showerror` y detiene la operación.
3. Si `edad_txt.isdigit()` es falso, muestra un error y detiene la operación.
4. Abre `filedialog.asksaveasfilename()` para que el usuario escoja un archivo `.txt`.
5. Si el usuario selecciona una ruta, escribe el siguiente contenido con codificación UTF-8:

```text
Nombre: Ana
Edad: 21
```

6. Muestra la confirmación `Datos guardados.`.

**Limitaciones:** la edad se valida como una cadena de dígitos, pero no existe validación de límites de edad; no se maneja explícitamente un posible `OSError` al escribir el archivo. `isdigit()` acepta algunos caracteres numéricos Unicode que no necesariamente se pueden convertir directamente con `int()`.

### 4.4. `src/app/win_list.py`

**Propósito:** mantener una lista de textos durante la ejecución de la ventana.

**Función pública:** `open_win_list(parent: tk.Tk)`.

**Funciones internas:**
- `agregar()`: lee el texto, elimina espacios exteriores, agrega un elemento al `Listbox` y limpia el campo. Si está vacío, muestra una advertencia.
- `eliminar()`: obtiene la selección con `lb.curselection()` y elimina el primer elemento seleccionado si existe.
- `limpiar()`: elimina todos los elementos de la lista con `lb.delete(0, "end")`.

**Controles:** `tk.Listbox`, un `ttk.Entry` y los botones **Agregar**, **Eliminar seleccionado**, **Limpiar** y **Cerrar**.

**Alcance del “CRUD”:** implementa crear, visualizar y eliminar elementos. No implementa modificar/actualizar un elemento existente. Los registros solamente están en memoria: desaparecen al cerrar la ventana.

### 4.5. `src/app/win_table.py`

**Propósito:** mostrar datos tabulares procedentes de un CSV.

**Función pública:** `open_win_table(parent: tk.Tk)`.

**Bibliotecas:** `tkinter`, `ttk`, `messagebox`, `csv` y `pathlib.Path`.

**Flujo:**
1. Crea un `ttk.Treeview` con tres columnas: `nombre`, `valor1` y `valor2`.
2. Configura los encabezados y el ancho de cada columna.
3. Construye la ruta del archivo CSV y verifica si existe.
4. Si no existe, informa mediante `messagebox.showwarning(...)` y termina la función.
5. Si existe, abre el CSV en UTF-8, utiliza `csv.DictReader` y agrega cada fila al `Treeview` con `tv.insert`.
6. Agrega un botón **Cerrar** después de la carga de datos.

**Problema encontrado:** actualmente el código contiene:

```python
ruta = Path(__file__).resolve().parents[2] / "data" / "sample.csv"
```

Dado que `win_table.py` se encuentra en `Sesion3/src/app/`, `parents[2]` apunta a la carpeta `Sesion3/`, por lo que la ruta resultante sería `Sesion3/data/sample.csv`. Sin embargo, el CSV del ZIP se encuentra en `Sesion3/src/data/sample.csv`.

**Corrección recomendada:**

```python
ruta = Path(__file__).resolve().parents[1] / "data" / "sample.csv"
```

Aquí `parents[1]` corresponde a `Sesion3/src/`, que sí contiene la carpeta `data`.

**Nota adicional:** cuando no encuentra el CSV, el código retorna antes de crear el botón **Cerrar**; la ventana permanece abierta, pero puede cerrarse con el botón estándar del sistema operativo.

### 4.6. `src/app/win_canvas.py`

**Propósito:** demostrar el dibujo de objetos geométricos en una interfaz.

**Función pública:** `open_win_canvas(parent: tk.Tk)`.

Crea un lienzo blanco `tk.Canvas` de `440x240` y dibuja:

| Método | Resultado |
|---|---|
| `create_rectangle(20, 20, 120, 80, ...)` | Rectángulo con borde negro |
| `create_oval(150, 20, 220, 90, ...)` | Óvalo azul claro |
| `create_line(240, 30, 360, 90, ...)` | Línea de grosor 3 |
| `create_text(220, 140, ...)` | Texto “¡Hola Canvas!” |

El código utiliza coordenadas en píxeles relativas a la esquina superior izquierda del lienzo. Los dibujos son estáticos; no se implementan operaciones de arrastre, edición o animación.

### 4.7. `src/data/sample.csv`

**Propósito:** proporcionar registros para la ventana de tabla.

```csv
nombre,valor1,valor2
A,10,20
B,15,25
C,12,30
```

Contiene una fila de encabezados y tres registros. Los valores se leen como texto desde `csv.DictReader`; no se realiza conversión explícita a números.

### 4.8. `.vscode/launch.json`

**Propósito:** ejecutar y depurar la aplicación desde Visual Studio Code.

La configuración denominada `Programa con PYTHONPATH=src` establece:

- `program`: `${workspaceFolder}/src/app/main.py`.
- `cwd`: `${workspaceFolder}` (carpeta de trabajo).
- `env.PYTHONPATH`: `${workspaceFolder}/src`, para poder importar módulos con `from app...`.
- `console`: terminal integrada.
- `justMyCode`: depuración enfocada en el código del usuario.

## 5. Instalación y ejecución

**Requisitos:** Python 3 con `tkinter` disponible, un sistema capaz de mostrar ventanas gráficas y, opcionalmente, Visual Studio Code. Las bibliotecas utilizadas pertenecen a la distribución estándar de Python; según el sistema operativo, Tkinter puede requerir instalación separada.

**Opción A: VS Code**
1. Descomprime `Sesion3.zip`.
2. Abre la carpeta `Sesion3` como carpeta raíz del proyecto.
3. Selecciona el intérprete de Python.
4. En VS Code, abre **Ejecutar y depurar**, selecciona **Programa con PYTHONPATH=src** y ejecuta.

**Opción B: terminal, desde la carpeta `Sesion3`**

En **PowerShell (Windows)**:

```powershell
$env:PYTHONPATH = (Join-Path (Get-Location) "src")
python src/app/main.py
```

En **macOS/Linux**:

```bash
PYTHONPATH=src python3 src/app/main.py
```

**Importante:** ejecutar directamente `python src/app/main.py` sin configurar `PYTHONPATH` puede fallar con `ModuleNotFoundError: No module named 'app'`. La configuración de VS Code incluida en el ZIP ya establece esa variable.

**Comprobación funcional sugerida:** abrir cada una de las cinco ventanas; en el formulario, probar nombre vacío, edad no numérica y guardado correcto; en la lista, agregar y eliminar; en la tabla, comprobar la carga de A, B y C después de corregir la ruta; y en Canvas, confirmar que se vean las cuatro figuras/textos.

## 6. Problemas identificados y prioridades

| Prioridad | Hallazgo | Impacto | Recomendación |
|---|---|---|---|
| Alta | Ruta incorrecta del CSV en `win_table.py` | La tabla no muestra los datos suministrados | Cambiar `parents[2]` por `parents[1]` |
| Media | Lista descrita como CRUD sin función de actualizar | Funcionalidad incompleta respecto al nombre | Añadir edición o renombrar la función |
| Media | Guardado TXT y lectura CSV sin manejo explícito de excepciones | Errores de archivo podrían interrumpir la acción | Usar `try/except OSError`, y manejar errores de formato según el caso |
| Media | Sin pruebas automatizadas | Los cambios pueden introducir regresiones | Crear pruebas en `src/tests/` |
| Baja | `core/` vacío | No hay separación de lógica de negocio | Extraer reglas de validación y manejo de datos conforme crezca el proyecto |
| Baja | Validación de edad limitada | Se admiten valores poco realistas | Definir reglas del proyecto y validar el rango |

## 7. Recomendaciones de evolución

Para convertir el prototipo en una aplicación más completa:

1. **Corregir primero la ruta del CSV**, sin modificar la estructura existente.
2. **Agregar persistencia a la lista**, por ejemplo mediante CSV o SQLite, si se requiere conservar los elementos entre sesiones.
3. **Implementar edición** para completar las operaciones CRUD.
4. **Separar lógica de interfaz y datos:** aprovechar `src/core/` para validaciones, lectura/escritura de archivos y reglas de negocio.
5. **Agregar pruebas** unitarias para validadores y lógica de archivos; las pruebas de interfaz pueden venir después.
6. **Incorporar un `README.md`** y esta documentación en `docs/` para facilitar el mantenimiento.

## 8. Conclusión

`Sesion3` demuestra correctamente los conceptos fundamentales de interfaces gráficas modulares con Tkinter: ventana principal, ventanas secundarias, controles, validación simple, almacenamiento en TXT, manipulación de listas, visualización tabular y dibujo. El error más relevante observado está en la ruta del CSV; corregirlo permitirá aprovechar el archivo de ejemplo existente. Los demás hallazgos son oportunidades de robustez y crecimiento, no afirmaciones de fallos comprobados en una ejecución real.

---

**Alcance de la revisión:** código fuente, archivo CSV y configuración presentes en `Sesion3.zip`. No se modificaron los archivos originales ni se ejecutó la interfaz gráfica.
