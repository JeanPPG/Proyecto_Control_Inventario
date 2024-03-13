import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from conexionDB import database
import datetime

class ActualizacionVentana(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Actualizar Producto")
        self.geometry("600x400")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.parent = parent

        self.create_widgets()
        self.load_data()

    def create_widgets(self):
        # Encabezado de la tarjeta
        card_frame = ttk.Frame(self)
        card_frame.pack(pady=20)

        card_title = ttk.Label(card_frame, text="Actualizar Producto", font=("Arial", 16, "bold"))
        card_title.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        card_description = ttk.Label(card_frame, text="Realice cambios en el producto", font=("Arial", 10))
        card_description.grid(row=1, column=0, columnspan=2, pady=(0, 20))

        # Campos de entrada
        label_id = ttk.Label(card_frame, text="ID:", font=("Arial", 10))
        label_id.grid(row=2, column=0, sticky="w", padx=10)
        self.id_entry = ttk.Entry(card_frame, font=("Arial", 10), state="readonly")
        self.id_entry.grid(row=2, column=1, padx=10, pady=5, sticky="we")

        label_name = ttk.Label(card_frame, text="Nombre:", font=("Arial", 10))
        label_name.grid(row=3, column=0, sticky="w", padx=10)
        self.name_entry = ttk.Entry(card_frame, font=("Arial", 10))
        self.name_entry.grid(row=3, column=1, padx=10, pady=5, sticky="we")

        label_code = ttk.Label(card_frame, text="Código:", font=("Arial", 10))
        label_code.grid(row=4, column=0, sticky="w", padx=10)
        self.code_entry = ttk.Entry(card_frame, font=("Arial", 10))
        self.code_entry.grid(row=4, column=1, padx=10, pady=5, sticky="we")

        label_quantity = ttk.Label(card_frame, text="Cantidad:", font=("Arial", 10))
        label_quantity.grid(row=5, column=0, sticky="w", padx=10)
        self.quantity_entry = ttk.Entry(card_frame, font=("Arial", 10))
        self.quantity_entry.grid(row=5, column=1, padx=10, pady=5, sticky="we")

        label_category = ttk.Label(card_frame, text="Categoría:", font=("Arial", 10))
        label_category.grid(row=6, column=0, sticky="w", padx=10)
        self.category_combobox = ttk.Combobox(card_frame, values=["Químicos", "Equipos", "Glassware", "Consumibles"], font=("Arial", 10))
        self.category_combobox.grid(row=6, column=1, padx=10, pady=5, sticky="we")

        # Descripción del producto
        label_description = ttk.Label(card_frame, text="Descripción:", font=("Arial", 10))
        label_description.grid(row=7, column=0, sticky="w", padx=10)
        self.description_entry = tk.Text(card_frame, font=("Arial", 10), height=4, width=30)
        self.description_entry.grid(row=7, column=1, padx=10, pady=5, sticky="we")

        # Botones de actualización y eliminación
        button_frame = ttk.Frame(card_frame)
        button_frame.grid(row=8, column=0, columnspan=2, pady=20)

        update_button = ttk.Button(button_frame, text="Actualizar", command=self.actualizar_producto)
        update_button.grid(row=0, column=0, padx=10, sticky="we")

        delete_button = ttk.Button(button_frame, text="Eliminar", command=self.eliminar_producto)
        delete_button.grid(row=0, column=1, padx=10, sticky="we")

        # Tabla de productos
        self.treeview = ttk.Treeview(self, columns=("ID", "Nombre", "Código", "Cantidad", "Categoría", "Descripción"), show="headings")
        self.treeview.heading("ID", text="ID")
        self.treeview.heading("Nombre", text="Nombre")
        self.treeview.heading("Código", text="Código")
        self.treeview.heading("Cantidad", text="Cantidad")
        self.treeview.heading("Categoría", text="Categoría")
        self.treeview.heading("Descripción", text="Descripción")
        self.treeview.bind("<ButtonRelease-1>", self.seleccionar_elemento)
        self.treeview.pack(fill="both", expand=True)

    def load_data(self):
        self.treeview.delete(*self.treeview.get_children())
        connection = database.connect_to_database()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT id, nombre, codigo, cantidad, categoria, descripcion FROM inventario ORDER BY id")
                rows = cursor.fetchall()
                for row in rows:
                    self.treeview.insert("", "end", values=row)
            except Exception as e:
                print("Error al cargar datos:", e)
            finally:
                cursor.close()
                connection.close()

    def seleccionar_elemento(self, event):
        selected_item = self.treeview.focus()
        if selected_item:
            item_values = self.treeview.item(selected_item, "values")
            self.id_entry.config(state="normal")
            self.name_entry.config(state="normal")
            self.code_entry.config(state="normal")
            self.quantity_entry.config(state="normal")
            self.category_combobox.config(state="normal")
            self.description_entry.config(state="normal")
            self.id_entry.delete(0, tk.END)
            self.name_entry.delete(0, tk.END)
            self.code_entry.delete(0, tk.END)
            self.quantity_entry.delete(0, tk.END)
            self.description_entry.delete("1.0", tk.END)
            self.id_entry.insert(0, item_values[0])
            self.name_entry.insert(0, item_values[1])
            self.code_entry.insert(0, item_values[2])
            self.quantity_entry.insert(0, item_values[3])
            self.category_combobox.set(item_values[4])
            self.description_entry.insert("1.0", item_values[5])

    def actualizar_producto(self):
        id = self.id_entry.get()
        name = self.name_entry.get()
        code = self.code_entry.get()
        quantity = self.quantity_entry.get()
        category = self.category_combobox.get()
        description = self.description_entry.get("1.0", "end-1c")

        if not id or not name or not code or not quantity or not category or not description:
            messagebox.showerror("Error", "Por favor complete todos los campos.")
            return

        connection = database.connect_to_database()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("UPDATE inventario SET nombre=%s, codigo=%s, cantidad=%s, categoria=%s, descripcion=%s WHERE id=%s", (name, code, quantity, category, description, id))
                connection.commit()
                messagebox.showinfo("Actualización", "Producto actualizado correctamente.")

                # Registrar la actualización en el seguimiento
                self.registrar_seguimiento(f"Producto actualizado: {name}")

                self.load_data()
                self.limpiar_campos()
            except Exception as e:
                print("Error al actualizar producto:", e)
                messagebox.showerror("Error", "Error al actualizar producto.")
            finally:
                cursor.close()
                connection.close()

    def eliminar_producto(self):
        id = self.id_entry.get()

        if not id:
            messagebox.showerror("Error", "Por favor ingrese el ID del producto a eliminar.")
            return

        if messagebox.askyesno("Eliminar", "¿Estás seguro de que quieres eliminar este producto?"):
            connection = database.connect_to_database()
            if connection:
                try:
                    cursor = connection.cursor()
                    cursor.execute("SELECT nombre FROM inventario WHERE id=%s", (id,))
                    nombre_producto = cursor.fetchone()[0]
                    cursor.execute("DELETE FROM inventario WHERE id=%s", (id,))
                    connection.commit()
                    messagebox.showinfo("Eliminación", "Producto eliminado correctamente.")

                    # Registrar la eliminación en el seguimiento
                    self.registrar_seguimiento(f"Producto eliminado: {nombre_producto}")

                    self.load_data()
                    self.limpiar_campos()
                except Exception as e:
                    print("Error al eliminar producto:", e)
                    messagebox.showerror("Error", "Error al eliminar producto.")
                finally:
                    cursor.close()
                    connection.close()

    def limpiar_campos(self):
        self.id_entry.config(state="readonly")
        self.name_entry.delete(0, tk.END)
        self.code_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.category_combobox.set("")
        self.description_entry.delete("1.0", tk.END)

    def on_close(self):
        self.parent.deiconify()
        self.destroy()

    def registrar_seguimiento(self, detalle):
        connection = database.connect_to_database()
        if connection:
            try:
                cursor = connection.cursor()
                fecha_hora_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                cursor.execute("INSERT INTO seguimiento (fecha, evento, detalle) VALUES (%s, %s, %s)", (fecha_hora_actual, "Actualización/Eliminación", detalle))
                connection.commit()
            except Exception as e:
                print("Error al registrar seguimiento:", e)
            finally:
                cursor.close()
                connection.close()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal temporalmente
    actualizacion_ventana = ActualizacionVentana(root)
    root.mainloop()
