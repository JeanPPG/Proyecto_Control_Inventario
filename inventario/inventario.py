import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class GestionInventario(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Gestión de Inventario")
        self.geometry("600x400")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.parent = parent

        self.create_widgets()

    def create_widgets(self):
        # Frame para organizar los botones principales
        button_frame = tk.Frame(self)
        button_frame.pack(pady=20)

        # Botón de cerrar sesión en la esquina superior izquierda
        logout_button = ttk.Button(button_frame, text="Cerrar Sesión", command=self.logout)
        logout_button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        # Botones principales para añadir, modificar y listar elementos
        add_button = ttk.Button(button_frame, text="Añadir", command=self.add_item)
        add_button.grid(row=0, column=1, padx=10, pady=10)

        modify_button = ttk.Button(button_frame, text="Modificar", command=self.modify_item)
        modify_button.grid(row=0, column=2, padx=10, pady=10)

        list_button = ttk.Button(button_frame, text="Listar", command=self.list_items)
        list_button.grid(row=0, column=3, padx=10, pady=10)

        # Etiqueta de bienvenida
        label = tk.Label(self, text="Bienvenido a la Gestión de Inventario", font=("Arial", 16))
        label.pack(pady=20)

    def logout(self):
        self.destroy()
        self.parent.deiconify()

    def on_close(self):
        if messagebox.askokcancel("Salir", "¿Estás seguro de que quieres salir?"):
            self.parent.destroy()

    def add_item(self):
        # Funcionalidad para añadir un elemento al inventario
        messagebox.showinfo("Añadir", "Funcionalidad de añadir aún no implementada.")

    def modify_item(self):
        # Funcionalidad para modificar un elemento del inventario
        messagebox.showinfo("Modificar", "Funcionalidad de modificar aún no implementada.")

    def list_items(self):
        # Funcionalidad para listar los elementos del inventario
        messagebox.showinfo("Listar", "Funcionalidad de listar aún no implementada.")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal temporalmente
    gestion_inventario = GestionInventario(root)
    root.mainloop()
