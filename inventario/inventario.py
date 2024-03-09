import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from inventario.registro import RegistroVentana
from inventario.actualizacion import ActualizacionVentana
from inventario.lista import ListaVentana
from inventario.seguimiento import SeguimientoVentana

class GestionInventario(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Gestión de Inventario")
        self.geometry("600x400")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.parent = parent

        self.create_widgets()

    def create_widgets(self):
        # Botón de cerrar sesión arriba a la izquierda
        logout_button = ttk.Button(self, text="Cerrar Sesión", command=self.logout)
        logout_button.pack(side="top", padx=10, pady=10, anchor="nw")

        # Etiqueta de título
        label = tk.Label(self, text="Bienvenido a la Gestión de Inventario", font=("Arial", 16))
        label.pack(pady=20)

        # Botones de funcionalidad
        button_frame = tk.Frame(self)
        button_frame.pack(pady=20)

        registrar_button = ttk.Button(button_frame, text="Registrar", command=self.abrir_registro)
        registrar_button.pack(side="top", padx=10, pady=10, fill="x")

        actualizar_button = ttk.Button(button_frame, text="Actualizar", command=self.abrir_actualizacion)
        actualizar_button.pack(side="top", padx=10, pady=10, fill="x")

        listar_button = ttk.Button(button_frame, text="Listar", command=self.abrir_lista)
        listar_button.pack(side="top", padx=10, pady=10, fill="x")

        seguimiento_button = ttk.Button(button_frame, text="Seguimiento", command=self.abrir_seguimiento)
        seguimiento_button.pack(side="top", padx=10, pady=10, fill="x")

    def logout(self):
        self.destroy()
        self.parent.deiconify()

    def on_close(self):
        if messagebox.askokcancel("Salir", "¿Estás seguro de que quieres salir?"):
            self.parent.destroy()

    def abrir_registro(self):
        self.withdraw()  # Oculta la ventana actual
        registro_ventana = RegistroVentana(self)
        registro_ventana.mainloop()

    def abrir_actualizacion(self):
        self.withdraw()  # Oculta la ventana actual
        actualizacion_ventana = ActualizacionVentana(self)
        actualizacion_ventana.mainloop()

    def abrir_lista(self):
        self.withdraw()  # Oculta la ventana actual
        lista_ventana = ListaVentana(self)
        lista_ventana.mainloop()

    def abrir_seguimiento(self):
        self.withdraw()  # Oculta la ventana actual
        seguimiento_ventana = SeguimientoVentana(self)
        seguimiento_ventana.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal temporalmente
    gestion_inventario = GestionInventario(root)
    root.mainloop()
