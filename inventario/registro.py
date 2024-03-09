import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class RegistroVentana(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Registro de Elemento")
        self.geometry("400x500")
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

        self.quantity_entry = ttk.Entry(card_frame, font=("Arial", 10))
        self.quantity_entry.grid(row=5, column=1, padx=10, pady=5, sticky="we")

        label_category = ttk.Label(card_frame, text="Categoria:", font=("Arial", 10))
        label_category.grid(row=6, column=0, sticky="w", padx=10)

        self.category_combobox = ttk.Combobox(card_frame, values=["Quimicos", "Equipos", "Glassware", "Consumibles"],
                                               font=("Arial", 10))
        self.category_combobox.grid(row=6, column=1, padx=10, pady=5, sticky="we")
        self.category_combobox.set("Seleccione la categoria")

        button_frame = ttk.Frame(card_frame)
        button_frame.grid(row=7, column=0, columnspan=2, pady=20)

        submit_button = ttk.Button(button_frame, text="Enviar", command=self.registrar_elemento, style="Submit.TButton")
        submit_button.grid(row=0, column=0, padx=10, sticky="we")

        cancel_button = ttk.Button(button_frame, text="Cancelar", command=self.on_close, style="Cancel.TButton")
        cancel_button.grid(row=0, column=1, padx=10, sticky="we")


    def registrar_elemento(self):
        name = self.name_entry.get()
        code = self.code_entry.get()
        quantity = self.quantity_entry.get()
        category = self.category_combobox.get()

        # Aquí puedes implementar la funcionalidad para registrar un elemento en el inventario
        messagebox.showinfo("Registrar", f"Registrar elemento:\nNombre: {name}\nCódigo: {code}\nCantidad: {quantity}\nCategoría: {category}")

    def on_close(self):
        if messagebox.askokcancel("Cancelar", "¿Estás seguro de que quieres cancelar el registro?"):
            self.parent.deiconify()
            self.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal temporalmente
    registro_ventana = RegistroVentana(root)
    root.mainloop()
