#Alejandro Moreno Camas 5To L
import tkinter as tk
from tkinter import filedialog, messagebox

class AnalizadorLexicoSintactico:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador Léxico y Sintáctico")
        self.root.geometry("800x700")
        self.root.configure(bg="#e8daef")  # Color de fondo para que se vea mas cute

       # Estilos y fuentes
# Estilos y fuentes
        self.fuente_titulo = ("Helvetica", 18, "bold")
        self.fuente_subtitulo = ("Helvetica", 14, "italic")
        self.fuente_texto = ("Verdana", 12)
        self.color_fondo_text = "#F5F5F5"  # Fondo color gris claro
        self.color_boton = "#4CAF50"  # Botón color verde
        self.color_boton_texto = "#FFFFFF"  # Texto del botón color blanco
        self.color_borde_boton = "#388E3C"  # Borde del botón color verde oscuro
        self.color_fondo_ventana = "#E0E0E0"  # Fondo de la ventana color gris claro
        self.color_texto = "#333333"  # Color del texto principal



        # Título
        self.titulo = tk.Label(root, text="Analizador Léxico y Sintáctico", font=self.fuente_titulo, bg="#F0F0F0")
        self.titulo.pack(pady=10)

        # Frame de entrada y salida
        self.frame_textos = tk.Frame(root, bg="#F0F0F0")
        self.frame_textos.pack(pady=10)

        # Área de entrada de código
        self.input_area = tk.Text(self.frame_textos, height=15, width=35, font=self.fuente_texto, bg=self.color_fondo_text, borderwidth=2, relief="solid")
        self.input_area.grid(row=0, column=0, padx=10)

        # Área de salida del análisis
        self.output_area = tk.Text(self.frame_textos, height=15, width=35, font=self.fuente_texto, bg=self.color_fondo_text, borderwidth=2, relief="solid", state='disabled')
        self.output_area.grid(row=0, column=1, padx=10)

        # Frame de botones
        self.frame_botones = tk.Frame(root, bg="#F0F0F0")
        self.frame_botones.pack(pady=10)

        # Botón para abrir archivo
        self.abrir_btn = tk.Button(self.frame_botones, text="Abrir archivo", font=("Arial", 12), bg=self.color_boton, fg=self.color_boton_texto, command=self.abrir_archivo)
        self.abrir_btn.grid(row=0, column=0, padx=10, pady=5)

        # Botón para analizar código
        self.analizar_btn = tk.Button(self.frame_botones, text="Analizar", font=("Arial", 12), bg=self.color_boton, fg=self.color_boton_texto, command=self.analizar_codigo)
        self.analizar_btn.grid(row=0, column=1, padx=10, pady=5)

        # Botón para limpiar áreas de texto
        self.limpiar_btn = tk.Button(self.frame_botones, text="Limpiar", font=("Arial", 12), bg=self.color_boton, fg=self.color_boton_texto, command=self.limpiar_areas)
        self.limpiar_btn.grid(row=0, column=2, padx=10, pady=5)

    def abrir_archivo(self):
        """Abre un archivo de texto para cargar el código en el área de entrada."""
        archivo = filedialog.askopenfilename(title="Abrir archivo", filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
        if archivo:
            with open(archivo, 'r') as file:
                codigo = file.read()
                self.input_area.delete('1.0', tk.END)
                self.input_area.insert(tk.END, codigo)
    
    def analizar_codigo(self):
        """Analiza el código de la entrada y muestra el análisis en el área de salida."""
        codigo = self.input_area.get('1.0', tk.END)
        lineas = codigo.splitlines()
        
        self.output_area.config(state='normal')  # Permitir escribir en el área de salida
        self.output_area.delete('1.0', tk.END)  # Limpiar el área de salida

        num_linea = 1
        for linea in lineas:
            self.analizar_linea(linea, num_linea)
            num_linea += 1
        
        self.output_area.config(state='disabled')  # Deshabilitar escritura para proteger el área de salida
    
    def analizar_linea(self, linea, num_linea):
        """Analiza una línea individual y clasifica los tokens."""
        tokens = linea.split()  # Divide la línea por espacios
        self.output_area.insert(tk.END, f"Línea {num_linea}:\n")

        
        #Aqui colocamos nuestros tokens de tal manera que podamos hacer que el pramagra identifique los caracteres especiales
        for token in tokens:
            if token in ["int", "float"]:
                self.output_area.insert(tk.END, f"<Tipo de dato> {token}\n")
            elif token == "main":
                self.output_area.insert(tk.END, f"<Reservada main> {token}\n")
            elif token == "(":
                self.output_area.insert(tk.END, f"<Paréntesis de apertura> {token}\n")
            elif token == ")":
                self.output_area.insert(tk.END, f"<Paréntesis de cierre> {token}\n")
            elif token == "{":
                self.output_area.insert(tk.END, f"<Llave de apertura> {token}\n")
            elif token == "}":
                self.output_area.insert(tk.END, f"<Llave de cierre> {token}\n")
            elif token == "   ":
                self.output_area.insert(tk.END, f"<Espacio en blanco> {token}\n")
            elif token == ";":
                self.output_area.insert(tk.END, f"<Punto y coma> {token}\n")
            else:
                self.output_area.insert(tk.END, f"<Identificador> {token}\n")
        
        self.output_area.insert(tk.END, "\n")
    
    def limpiar_areas(self):
        """Limpia el área de entrada y de salida."""
        self.input_area.delete('1.0', tk.END)
        self.output_area.config(state='normal')
        self.output_area.delete('1.0', tk.END)
        self.output_area.config(state='disabled')

# Crear ventana principal
root = tk.Tk()
app = AnalizadorLexicoSintactico(root)
root.mainloop()
