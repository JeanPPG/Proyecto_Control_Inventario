import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from conexionDB import database

class SeguimientoVentana(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Seguimiento de Inventario")
        self.geometry("800x400")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.parent = parent

        self.create_widgets()
        self.load_data()

    def create_widgets(self):
        # Encabezado
        header_frame = ttk.Frame(self)
        header_frame.pack(pady=10)

        header_label = ttk.Label(header_frame, text="Seguimiento de Inventario", font=("Arial", 14, "bold"))
        header_label.pack()

        # Descripción
        description_frame = ttk.Frame(self)
        description_frame.pack(pady=10)

        description_label = ttk.Label(description_frame, text="Permite un seguimiento completo de la actividad en el inventario, proporcionando un registro histórico detallado.")
        description_label.pack()

        # Crear el Treeview para mostrar el historial de transacciones
        self.treeview = ttk.Treeview(self, columns=("ID", "Fecha", "Evento", "Detalle"), show="headings")
        self.treeview.heading("ID", text="ID")
        self.treeview.heading("Fecha", text="Fecha")
        self.treeview.heading("Evento", text="Evento")
        self.treeview.heading("Detalle", text="Detalle")
        self.treeview.pack(fill="both", expand=True)

    def load_data(self):
        connection = database.connect_to_database()
        if connection:
            try:
                cursor = connection.cursor()

                # Consulta para seleccionar todos los registros de la tabla de seguimiento
                cursor.execute("SELECT id, fecha, evento, detalle FROM seguimiento")

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

    def on_close(self):
        self.parent.deiconify()
        self.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal temporalmente
    seguimiento_ventana = SeguimientoVentana(root)
    root.mainloop()
