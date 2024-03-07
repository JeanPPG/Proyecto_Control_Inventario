import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from inventario.inventario import GestionInventario

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Control de Inventario")
        self.set_window_icon()

        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.window_width = min(800, self.screen_width)
        self.window_height = min(600, self.screen_height)
        self.window_x = (self.screen_width - self.window_width) // 2
        self.window_y = (self.screen_height - self.window_height) // 2
        self.geometry(f"{self.window_width}x{self.window_height}+{self.window_x}+{self.window_y}")

        self.current_frame = None
        self.login_attempts = 0

        self.show_main_menu()

    def set_window_icon(self):
        icon_image = Image.open("icons/icon.png")
        icon_photo = ImageTk.PhotoImage(icon_image)
        self.iconphoto(True, icon_photo)

    def show_main_menu(self):
        if self.current_frame:
            self.current_frame.destroy()

        content_frame = tk.Frame(self)
        content_frame.pack(fill=tk.BOTH, expand=True)

        self.current_frame = content_frame

        self.set_title_and_logo(content_frame)

        login_button = self.create_styled_button(content_frame, "Iniciar Sesión", "icons/login_icon.png",
                                                 self.show_login_form)
        login_button.place(relx=0.25, rely=0.7, anchor=tk.CENTER)

        create_account_button = self.create_styled_button(content_frame, "Crear Usuario",
                                                          "icons/create_account_icon.png", self.show_create_user_form)
        create_account_button.place(relx=0.75, rely=0.7, anchor=tk.CENTER)

    def set_title_and_logo(self, parent):
        title_label = tk.Label(parent, text="Sistema de Control de Inventario", font=("Arial", 24, "bold"))
        title_label.pack(pady=(20, 10))

        logo_image = Image.open("icons/logo.png")
        logo_image = logo_image.resize((200, 200))
        logo_photo = ImageTk.PhotoImage(logo_image)

        logo_canvas = tk.Canvas(parent, bg="white", highlightthickness=0, width=200, height=200)
        logo_canvas.create_image(self.window_width // 2, self.window_height // 3, anchor=tk.CENTER, image=logo_photo)
        logo_canvas.pack(pady=20)

    def create_styled_button(self, parent, text, icon_path, command):
        button_style = ttk.Style()
        button_style.configure("Custom.TButton", background="#4CAF50", foreground="black", font=("Arial", 14, "bold"),
                               padding=10)

        button_image = Image.open(icon_path)
        button_image = button_image.resize((30, 30))
        button_photo = ImageTk.PhotoImage(button_image)

        button = ttk.Button(parent, text=text, style="Custom.TButton", image=button_photo, compound=tk.LEFT,
                            command=command)
        button.image = button_photo  # Keep a reference to the image to avoid garbage collection
        return button

    def show_login_form(self):
        if self.current_frame:
            self.current_frame.destroy()

        login_frame = tk.Frame(self)
        login_frame.pack(fill=tk.BOTH, expand=True)

        self.current_frame = login_frame

        title_label = tk.Label(login_frame, text="Inicio de Sesión", font=("Arial", 24, "bold"))
        title_label.pack(pady=(20, 10))

        user_label = tk.Label(login_frame, text="Usuario:", font=("Arial", 14))
        user_label.pack()

        self.user_entry = ttk.Entry(login_frame, font=("Arial", 14))
        self.user_entry.pack()

        password_label = tk.Label(login_frame, text="Contraseña:", font=("Arial", 14))
        password_label.pack()

        self.password_entry = ttk.Entry(login_frame, show="*", font=("Arial", 14))
        self.password_entry.pack()

        login_button = ttk.Button(login_frame, text="Entrar", style="Custom.TButton", command=self.login)
        login_button.pack(pady=10)

        back_button = ttk.Button(login_frame, text="Regresar", style="Custom.TButton", command=self.show_main_menu)
        back_button.pack()

    def login(self):
        # Verificar las credenciales
        username = self.user_entry.get()
        password = self.password_entry.get()

        # Credenciales temporales para pruebas
        correct_username = "admin"
        correct_password = "admin"

        # Verificar si las credenciales ingresadas coinciden con las credenciales temporales
        if username == correct_username and password == correct_password:
            messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso!")
            self.login_attempts = 0
            # Si la autenticación es exitosa, muestra la interfaz de gestión de inventario
            self.show_inventario()
        else:
            self.login_attempts += 1

            # Si se exceden los 3 intentos, mostrar un mensaje y volver al menú principal
            if self.login_attempts >= 3:
                messagebox.showerror("Inicio de Sesión",
                                    "Exceso de intentos de inicio de sesión. Volviendo al menú principal.")
                self.show_main_menu()
            else:
                messagebox.showerror("Inicio de Sesión", "Error en el inicio de sesión. Por favor, inténtelo de nuevo.")

    def show_create_user_form(self):
        if self.current_frame:
            self.current_frame.destroy()

        create_user_frame = tk.Frame(self)
        create_user_frame.pack(fill=tk.BOTH, expand=True)

        self.current_frame = create_user_frame

        title_label = tk.Label(create_user_frame, text="Crear Usuario", font=("Arial", 24, "bold"))
        title_label.pack(pady=(20, 10))

        name_label = tk.Label(create_user_frame, text="Nombre:", font=("Arial", 14))
        name_label.pack()

        self.name_entry = ttk.Entry(create_user_frame, font=("Arial", 14))
        self.name_entry.pack()

        last_name_label = tk.Label(create_user_frame, text="Apellido:", font=("Arial", 14))
        last_name_label.pack()

        self.last_name_entry = ttk.Entry(create_user_frame, font=("Arial", 14))
        self.last_name_entry.pack()

        id_label = tk.Label(create_user_frame, text="ID:", font=("Arial", 14))
        id_label.pack()

        self.id_entry = ttk.Entry(create_user_frame, font=("Arial", 14))
        self.id_entry.pack()

        phone_label = tk.Label(create_user_frame, text="Teléfono:", font=("Arial", 14))
        phone_label.pack()

        self.phone_entry = ttk.Entry(create_user_frame, font=("Arial", 14))
        self.phone_entry.pack()

        user_label = tk.Label(create_user_frame, text="Usuario:", font=("Arial", 14))
        user_label.pack()

        self.user_entry = ttk.Entry(create_user_frame, font=("Arial", 14))
        self.user_entry.pack()

        password_label = tk.Label(create_user_frame, text="Contraseña:", font=("Arial", 14))
        password_label.pack()

        self.password_entry = ttk.Entry(create_user_frame, show="*", font=("Arial", 14))
        self.password_entry.pack()

        create_button = ttk.Button(create_user_frame, text="Crear", style="Custom.TButton", command=self.create_user)
        create_button.pack(pady=10)

        back_button = ttk.Button(create_user_frame, text="Regresar", style="Custom.TButton",
                                 command=self.show_main_menu)
        back_button.pack()

    def create_user(self):
        # Obtener los datos del nuevo usuario
        name = self.name_entry.get()
        last_name = self.last_name_entry.get()
        user_id = self.id_entry.get()
        phone = self.phone_entry.get()
        username = self.user_entry.get()
        password = self.password_entry.get()

        # Aquí podrías guardar los datos del nuevo usuario en una base de datos o hacer lo que necesites con ellos
        # Por ahora, simplemente mostraremos un mensaje con la información del usuario creado
        message = f"Usuario creado con éxito!\n\nNombre: {name}\nApellido: {last_name}\nID: {user_id}\nTeléfono: {phone}\nUsuario: {username}\nContraseña: {password}"
        messagebox.showinfo("Crear Usuario", message)

    def show_inventario(self):
        # Ocultar la ventana principal y mostrar la ventana de gestión de inventario
        self.withdraw()
        inventario_window = GestionInventario(self)
        inventario_window.mainloop()
        # Cuando se cierre la ventana de gestión de inventario, mostrar nuevamente la ventana principal
        self.deiconify()

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
