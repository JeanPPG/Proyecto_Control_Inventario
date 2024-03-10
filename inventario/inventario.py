import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
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
        # Icono para el botón de cerrar sesión
        logout_icon = Image.open("icons/logout.png")
        logout_icon = self.resize_image(logout_icon, (20, 20))
        logout_icon = ImageTk.PhotoImage(logout_icon)

        # Botón de cerrar sesión arriba a la izquierda
        logout_button = ttk.Button(self, text="Cerrar Sesión", command=self.logout, image=logout_icon, compound="left")
        logout_button.image = logout_icon
        logout_button.pack(side="top", padx=10, pady=10, anchor="nw")

        # Etiqueta de título
        label = tk.Label(self, text="Bienvenido a la Gestión de Inventario", font=("Arial", 16))
        label.pack(pady=20)

        # Botones de funcionalidad
        button_frame = tk.Frame(self)
        button_frame.pack(pady=20)

        # Establecer un tamaño fijo para los botones
        button_width = 200
        button_height = 50

        # Agregar iconos a los botones y ajustar su tamaño manteniendo la proporción
        icon_size = (button_width - 20, button_height - 20)

        # Botón Registrar
        registrar_icon = Image.open("icons/register.png")
        registrar_icon = self.resize_image(registrar_icon, icon_size)
        registrar_icon = ImageTk.PhotoImage(registrar_icon)
        registrar_button = ttk.Button(button_frame, text="Registrar", command=self.abrir_registro, image=registrar_icon, compound="left")
        registrar_button.image = registrar_icon
        registrar_button.config(width=button_width)
        registrar_button.pack(side="top", padx=10, pady=10, fill="x")

        # Botón Actualizar
        actualizar_icon = Image.open("icons/update.png")
        actualizar_icon = self.resize_image(actualizar_icon, icon_size)
        actualizar_icon = ImageTk.PhotoImage(actualizar_icon)
        actualizar_button = ttk.Button(button_frame, text="Actualizar", command=self.abrir_actualizacion, image=actualizar_icon, compound="left")
        actualizar_button.image = actualizar_icon
        actualizar_button.config(width=button_width)
        actualizar_button.pack(side="top", padx=10, pady=10, fill="x")

        # Botón Listar
        listar_icon = Image.open("icons/list.png")
        listar_icon = self.resize_image(listar_icon, icon_size)
        listar_icon = ImageTk.PhotoImage(listar_icon)
        listar_button = ttk.Button(button_frame, text="Listar", command=self.abrir_lista, image=listar_icon, compound="left")
        listar_button.image = listar_icon
        listar_button.config(width=button_width)
        listar_button.pack(side="top", padx=10, pady=10, fill="x")

        # Botón Seguimiento
        seguimiento_icon = Image.open("icons/track.png")
        seguimiento_icon = self.resize_image(seguimiento_icon, icon_size)
        seguimiento_icon = ImageTk.PhotoImage(seguimiento_icon)
        seguimiento_button = ttk.Button(button_frame, text="Seguimiento", command=self.abrir_seguimiento, image=seguimiento_icon, compound="left")
        seguimiento_button.image = seguimiento_icon
        seguimiento_button.config(width=button_width)
        seguimiento_button.pack(side="top", padx=10, pady=10, fill="x")

    def resize_image(self, image, size):
        """Resize an image while maintaining aspect ratio."""
        original_width, original_height = image.size
        target_width, target_height = size
        aspect_ratio = original_width / original_height

        if target_width / aspect_ratio <= target_height:
            new_width = int(target_width)
            new_height = int(target_width / aspect_ratio)
        else:
            new_width = int(target_height * aspect_ratio)
            new_height = int(target_height)

        resized_image = image.resize((new_width, new_height), Image.NEAREST)
        return resized_image

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
