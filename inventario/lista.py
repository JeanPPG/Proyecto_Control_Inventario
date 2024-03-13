import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from fpdf import FPDF
from PIL import Image, ImageTk
from conexionDB import database

class ListaVentana(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Lista de Productos")
        self.geometry("600x400")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.parent = parent

        self.create_widgets()

    def create_widgets(self): 
        # Icono para el botón de generación de PDF
        pdf_icon = Image.open("icons/pdf_icon.png")
        pdf_icon = pdf_icon.resize((20, 20), Image.NEAREST)
        pdf_icon = ImageTk.PhotoImage(pdf_icon)

        # Botón para generar PDF
        pdf_button = ttk.Button(self, text="Generar PDF", command=self.generate_pdf, image=pdf_icon, compound="left")
        pdf_button.image = pdf_icon
        pdf_button.pack(side="top", padx=10, pady=10, anchor="nw")

        # Crear el Treeview para mostrar la lista de productos
        self.treeview = ttk.Treeview(self, columns=("Nombre", "Código", "Cantidad", "Categoría", "Descripción"), show="headings")
        self.treeview.heading("Nombre", text="Nombre")
        self.treeview.heading("Código", text="Código")
        self.treeview.heading("Cantidad", text="Cantidad")
        self.treeview.heading("Categoría", text="Categoría")
        self.treeview.heading("Descripción", text="Descripción")
        self.treeview.pack(fill="both", expand=True)

        # Obtener los datos de la base de datos y cargarlos en el Treeview
        self.load_data()

        # Verificar niveles de stock y generar alertas
        self.check_stock_levels()

    def load_data(self):
        connection = database.connect_to_database()
        if connection:
            try:
                cursor = connection.cursor()

                # Consulta para seleccionar todos los registros de la tabla inventario
                cursor.execute("SELECT nombre, codigo, cantidad, categoria, descripcion FROM inventario")

                # Obtener todos los registros
                rows = cursor.fetchall()

                # Insertar los datos en el Treeview
                for row in rows:
                    self.treeview.insert("", "end", values=row)

            except Exception as e:
                print("Error al cargar datos:", e)
            finally:
                cursor.close()
                connection.close()

    def generate_pdf(self):
        # Crear un nuevo objeto PDF
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()

        # Encabezado
        pdf.set_font("Arial", size=12, style="B")
        pdf.cell(200, 10, txt="Inventario de Productos", ln=True, align="C")
        pdf.cell(200, 10, txt="---", ln=True, align="C")
        pdf.cell(200, 10, txt="Fecha de creación: 10 de marzo de 2024", ln=True, align="C")
        pdf.cell(200, 10, txt="Ubicación: Almacén principal", ln=True, align="C")
        pdf.cell(200, 10, txt="---", ln=True, align="C")
        pdf.ln(10)

        # Información del inventario
        total_products = len(self.treeview.get_children())
        pdf.cell(200, 10, txt=f"Total de productos: {total_products}", ln=True, align="L")
        pdf.ln(10)

        # Tabla del inventario
        pdf.set_font("Arial", size=10)
        pdf.set_fill_color(200, 220, 255)
        pdf.cell(40, 10, "Nombre", 1, 0, "C", 1)
        pdf.cell(40, 10, "Código", 1, 0, "C", 1)
        pdf.cell(40, 10, "Cantidad", 1, 0, "C", 1)
        pdf.cell(40, 10, "Categoría", 1, 0, "C", 1)
        pdf.cell(80, 10, "Descripción", 1, 1, "C", 1)

        for child in self.treeview.get_children():
            values = self.treeview.item(child)["values"]
            for value in values:
                pdf.cell(40, 10, str(value), 1, 0, "C")
            pdf.ln()

        # Guardar el PDF
        pdf_output = "Inventario_Productos.pdf"
        pdf.output(pdf_output)
        messagebox.showinfo("PDF generado", f"El PDF se ha generado correctamente como {pdf_output}")

    def on_close(self):
        self.parent.deiconify()
        self.destroy()

    def check_stock_levels(self):
        low_stock_products = []  # Lista para almacenar los productos con bajo stock

        for child in self.treeview.get_children():
            quantity = int(self.treeview.item(child, "values")[2])  # Obtener la cantidad del producto
            if quantity <= 10:
                name = self.treeview.item(child, "values")[0]  # Obtener el nombre del producto
                low_stock_products.append(name)  # Agregar el nombre del producto a la lista

        if low_stock_products:
            # Crear un mensaje con todos los productos de bajo stock
            message = "Los siguientes productos tienen un nivel de stock bajo:\n\n"
            for product in low_stock_products:
                message += f"- {product}\n"
            
            messagebox.showwarning("Alerta de stock bajo", message)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal temporalmente
    lista_ventana = ListaVentana(root)
    root.mainloop()
