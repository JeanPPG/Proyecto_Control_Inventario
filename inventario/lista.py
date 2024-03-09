import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ListaVentana(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Listado de Elementos")
        self.geometry("400x300")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.parent = parent

        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, text="Listado de Elementos", font=("Arial", 16))
        label.pack(pady=20)

        # Implementar la lógica para mostrar la lista de elementos

    def on_close(self):
        if messagebox.askokcancel("Salir", "¿Estás seguro de que quieres salir?"):
            self.parent.deiconify()
            self.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal temporalmente
    lista_ventana = ListaVentana(root)
    root.mainloop()
