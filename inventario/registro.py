import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re
from conexionDB import database
import datetime

class RegistroVentana(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Registro de Elemento")
        self.geometry("400x550")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.parent = parent

        self.create_widgets()

    def create_widgets(self):
        card_frame = ttk.Frame(self)
        card_frame.pack(pady=20)

        card_title = ttk.Label(card_frame, text="Ingrese los detalles del producto", font=("Arial", 16, "bold"))
        card_title.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        card_description = ttk.Label(card_frame, text="Rellene la siguiente información para añadir un nuevo producto",
                                     font=("Arial", 10))
        card_description.grid(row=1, column=0, columnspan=2, pady=(0, 20))

        label_name = ttk.Label(card_frame, text="Nombre del producto:", font=("Arial", 10))
        label_name.grid(row=2, column=0, sticky="w", padx=10)

        self.name_entry = ttk.Entry(card_frame, font=("Arial", 10))
        self.name_entry.grid(row=2, column=1, padx=10, pady=5, sticky="we")

        label_code = ttk.Label(card_frame, text="Codigo del producto:", font=("Arial", 10))
        label_code.grid(row=3, column=0, sticky="w", padx=10)

        self.code_entry = ttk.Entry(card_frame, font=("Arial", 10))
        self.code_entry.grid(row=3, column=1, padx=10, pady=5, sticky="we")

        label_quantity = ttk.Label(card_frame, text="Cantidad:", font=("Arial", 10))
        label_quantity.grid(row=5, column=0, sticky="w", padx=10)

        self.quantity_var = tk.StringVar()
        self.quantity_entry = ttk.Entry(card_frame, textvariable=self.quantity_var, font=("Arial", 10))
        self.quantity_entry.grid(row=5, column=1, padx=10, pady=5, sticky="we")
        self.quantity_entry.configure(validate="key", validatecommand=(self.register(self.validate_quantity), "%P"))

        label_category = ttk.Label(card_frame, text="Categoría:", font=("Arial", 10))
        label_category.grid(row=6, column=0, sticky="w", padx=10)

        self.category_combobox = ttk.Combobox(card_frame, values=["Quimicos", "Equipos", "Glassware", "Consumibles"],
                                               font=("Arial", 10))
        self.category_combobox.grid(row=6, column=1, padx=10, pady=5, sticky="we")
        self.category_combobox.set("Seleccione la categoria")

        label_description = ttk.Label(card_frame, text="Descripción:", font=("Arial", 10))
        label_description.grid(row=7, column=0, sticky="w", padx=10)

        self.description_entry = tk.Text(card_frame, font=("Arial", 10), height=4, width=30)
        self.description_entry.grid(row=7, column=1, padx=10, pady=5, sticky="we")

        button_frame = ttk.Frame(card_frame)
        button_frame.grid(row=8, column=0, columnspan=2, pady=20)

        submit_button = ttk.Button(button_frame, text="Enviar", command=self.registrar_elemento, style="Submit.TButton")
        submit_button.grid(row=0, column=0, padx=10, sticky="we")

        cancel_button = ttk.Button(button_frame, text="Cancelar", command=self.on_close, style="Cancel.TButton")
        cancel_button.grid(row=0, column=1, padx=10, sticky="we")

    def validate_quantity(self, new_value):
        return re.match(r"^\d*$", new_value) is not None

    def registrar_elemento(self):
        name = self.name_entry.get()
        code = self.code_entry.get()
        quantity = self.quantity_entry.get()
        category = self.category_combobox.get()
        description = self.description_entry.get("1.0", "end-1c")  # Obtiene el texto de la descripción

        # Verifica si todos los campos están completos
        if not name or not code or not quantity or not category or not description:
            messagebox.showerror("Error", "Por favor complete todos los campos.")
            return

        connection = database.connect_to_database()
        if connection:
            try:
                cursor = connection.cursor()

                # Aquí ejecutas la inserción en la base de datos
                cursor.execute("INSERT INTO inventario (nombre, codigo, cantidad, categoria, descripcion) VALUES (%s, %s, %s, %s, %s)",
                               (name, code, quantity, category, description))

                # Agregar evento al seguimiento
                fecha_evento = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                evento = "Registro de Producto"
                detalle = f"Producto: {name}, Cantidad: {quantity}, Categoría: {category}"

                cursor.execute("INSERT INTO seguimiento (fecha, evento, detalle) VALUES (%s, %s, %s)", (fecha_evento, evento, detalle))

                connection.commit()

                messagebox.showinfo("Registrar", "Registro exitoso!")

                # Vaciar los campos después del registro exitoso
                self.name_entry.delete(0, tk.END)
                self.code_entry.delete(0, tk.END)
                self.quantity_var.set("")
                self.category_combobox.set("Seleccione la categoria")
                self.description_entry.delete("1.0", tk.END)  # Borra el contenido de la descripción
            except Exception as e:
                print("Error al registrar elemento:", e)
                messagebox.showerror("Error", "Error al registrar elemento.")
            finally:
                cursor.close()
                connection.close()
        else:
            print("Error: No se pudo conectar a la base de datos.")

    def on_close(self):
        if messagebox.askokcancel("Cancelar", "¿Estás seguro de que quieres cancelar el registro?"):
            self.parent.deiconify()
            self.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal temporalmente
    registro_ventana = RegistroVentana(root)
    root.mainloop()

