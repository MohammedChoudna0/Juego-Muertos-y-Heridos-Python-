
from PIL import Image
from customtkinter import CTk, CTkFrame, CTkEntry, CTkButton, CTkLabel, CTkImage, CTkToplevel
from Entidades.GestorDeJuego import *
from Entidades.GamePage import *
class LoginPage:

    def __init__(self , debug_mode=False):
        #instanciar clase Gestor y crear la ventana prinicipal
        self.master = CTk()
        self.debug_mode = debug_mode 
        self.gestor = Gestor(debug_mode)
        self.master.title("Login Page")
        self.master.config(bg="#2beaff")
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_rowconfigure(1, weight=1)

        # Creación de la imagen 
        # Ruta a cambiar en main.py
        self.bg_img = CTkImage(light_image=Image.open(r"app/Entidades/bg1.png"), size=(600, 600) )
        self.bg_lab = CTkLabel(self.master, image=self.bg_img, text="" , bg_color='#2beaff',fg_color='#2beaff')
        self.bg_lab.grid(row=0, column=1)

        # Creación del marco para el formulario
        self.frame1 = CTkFrame(self.master, fg_color="#c2e9fc", bg_color="#2beaff", height=350, width=700, corner_radius=20, border_width=5,border_color='#0085FF')
        self.frame1.grid(row=0, column=0, padx=10, sticky="e")

        # Etiqueta de título
        self.title = CTkLabel(self.frame1, text="Bienvenidos\nINICIAR SESIÓN", text_color="black", font=("", 35, "bold"), anchor="center")
        self.title.grid(row=0, column=0, sticky="nw", pady=30, padx=50)

        # Campos de entrada de usuario y contraseña
        self.usrname_entry = CTkEntry(self.frame1, text_color="white", placeholder_text="Por favor, ingrese tu usuario", fg_color="#5f9ab8", placeholder_text_color="white",
                             font=("", 16, "bold"), width=300, corner_radius=10, height=45)
        self.usrname_entry.grid(row=1, column=0, sticky="nwe", padx=40)

        self.passwd_entry = CTkEntry(self.frame1, text_color="white", placeholder_text="Por favor, ingrese tu pin", fg_color="#5f9ab8", placeholder_text_color="white",
                             font=("", 16, "bold"), width=300, corner_radius=15, height=45, show="*")
        self.passwd_entry.grid(row=2, column=0, sticky="nwe", padx=40, pady=20)

        #label de error
        self.error_label = CTkLabel(self.frame1, text="", text_color="red", font=("", 12,"bold"), anchor="center")
        self.error_label.grid(row=5, column=0, sticky="n", pady=10, padx=10)


        # Botones de acción
        self.cr_acc = CTkButton(self.frame1, text="Crear cuenta!", text_color="white", cursor="hand2", font=("", 15 ,"bold")
                                , height=40, width=60, fg_color="#0085FF", command=self.abrir_ventana_registro ,corner_radius=15)
        self.cr_acc.grid(row=3, column=0, sticky="w", pady=20, padx=40)

        self.md_v = CTkButton(self.frame1, text="Modo Invitado", text_color="white", cursor="hand2", font=("", 15 ,"bold")
                                , height=40, width=60, command=self.abrir_juego_modo_invitado,corner_radius=15,anchor="center")
        self.md_v.grid(row=4, column=0, sticky="n", pady=5, padx=5)


        self.l_btn = CTkButton(self.frame1, text="Iniciar Sesión", font=("", 15, "bold"), height=40, width=60, fg_color="#0085FF", cursor="hand2",
                      corner_radius=15, command=self.iniciar_sesion)
        self.l_btn.grid(row=3, column=0, sticky="ne", pady=20, padx=35)
        self.master.bind('<Return>', self.inicio_session_con_evento)  


        #Ventana de registro
        self.toplevel_window = None

        @property
        def nombre_jugador(self):
            return self._nombre_jugador

        @nombre_jugador.setter
        def nombre_jugador(self, nuevo_nombre):
            self._nombre_jugador = nuevo_nombre



    def abrir_ventana_registro(self):
        #Verifica si la ventana de registro no esta y la crea ,poniendo el foco en ella 
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = CTkToplevel() 
            self.toplevel_window.focus_force()
            self.toplevel_window.grab_set()
        else:
            self.toplevel_window.focus_force() 
    

        self.toplevel_window.resizable(False, False)

        #Crea los elementos de la ventana de registro 

        frame = CTkFrame(self.toplevel_window, fg_color="#c2e9fc", bg_color="white")
        frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        titulo = CTkLabel(frame, text="Registrarse", text_color="black", font=("", 24, "bold"), anchor="center")
        titulo.grid(row=0, column=0, sticky="n", pady=10)

        self.nuevo_usuario_registro = CTkEntry(frame, text_color="black", placeholder_text="Por favor, ingrese un usuario", fg_color="#a6ffe0", placeholder_text_color="#809ba6",
                             font=("", 16, "bold"), width=300, corner_radius=10, height=45)
        self.nuevo_usuario_registro.grid(row=1, column=0, sticky="n", padx=40, pady=0)

        self.error_label_registro = CTkLabel(frame, text="", text_color="red", font=("", 12, "bold"), anchor="center")
        self.error_label_registro.grid(row=2, column=0, sticky="s", pady=0, padx=10)

        self.nuevo_pin_registro = CTkEntry(frame, text_color="black", placeholder_text="Por favor, ingrese un pin", fg_color="#a6ffe0", placeholder_text_color="#809ba6",
                            font=("", 16, "bold"), width=300, corner_radius=15, height=45)
        self.nuevo_pin_registro.grid(row=3, column=0, sticky="n", padx=40, pady=10)

        btn_confirmar = CTkButton(frame, text="Confirmar", text_color="black", cursor="hand2", font=("", 15 ,"bold"),
                    border_width=0, fg_color="#c2e9fc", bg_color="#c2e9fc",command=self.confirmar_registro)
        btn_confirmar.grid(row=4, column=0, sticky="n", pady=20)


         #Se encarga de cambiar el texto de la etiqueta del error (ventana de registro) de "" al error correspondiente 
    def mostrar_error_registro(self, mensaje):
            self.error_label_registro.configure(text=mensaje)                                        

        #Confirma el nuevo usuario (si existe , si alguno de los campos es vacio)
    def confirmar_registro(self):
        usuario = self.nuevo_usuario_registro.get()
        pin = self.nuevo_pin_registro.get()

        if not usuario or not pin:
            self.mostrar_error_registro('Por favor, complete ambos campos.')
        else:
            resultado = self.gestor.agregar_usuario(usuario, pin)
            if resultado == "":
                self.mostrar_error_registro('El usuario se ha agregado correctamente')
                if self.toplevel_window is not None:
                
                     self.toplevel_window.destroy()
            else:
                self.mostrar_error_registro(resultado)


    def mostrar_error(self, mensaje):
        self.error_label.configure(text=mensaje)

    #Se encarga de authenticar al usuario y mostrar errores si es el caso
    def iniciar_sesion(self):
            usuario = self.usrname_entry.get()
            pin = self.passwd_entry.get()
            if usuario.__contains__('*') or pin.__contains__('*') :
                self.mostrar_error("Se ha introducido un carácter no válido")
                return

            resultado=self.gestor.autenticar_usuario(usuario,pin)
            if resultado == "":
                self.abrir_juego(usuario)
            else:
                if self.debug_mode: 
                    print("\x1b[31m" + resultado + "\x1b[0m")
                self.mostrar_error(resultado)

    #Abre el juego
    def abrir_juego(self,nombre_jugador):
        self.master.destroy()
        app= GamePage(nombre_jugador , True,self.debug_mode)
        app.run()
        
    def abrir_juego_modo_invitado(self):
        self.master.destroy()
        app= GamePage("",False,self.debug_mode )
        app.run()
        
        

    #El bucle de la ventana + pantalla completa
    def run(self):
        self.master.after(0, lambda: self.master.state('zoomed'))
        self.master.mainloop()

    #iniciar sesion con Enter
    def inicio_session_con_evento(self,event):
        self.iniciar_sesion()

