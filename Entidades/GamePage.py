from customtkinter import CTk, CTkFrame, CTkEntry, CTkButton, CTkLabel, CTkImage,CTkScrollableFrame
from Entidades.GestorDeJuego import *




class GamePage:
    def __init__(self , nombre_jugador, auth , debug_mode ):


        self.gestor = Gestor(debug_mode)
        self.master = CTk()
        self.debug_mode = debug_mode 

        self.nombre_jugador = nombre_jugador
        self.master.title("Página de Juego")
        self.master.config(bg="#b3fbff")
        self.master.resizable(True, True)

        # Creación de la ventana principal
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_rowconfigure(1, weight=1)

        self.auth = auth
    

        # Creación del marco para el formulario
        self.frame = CTkScrollableFrame(self.master, fg_color="#c2e9fc", bg_color="#b3fbff", height=600, width=570, corner_radius=20,border_width=5)
        self.frame.grid(row=0, column=0, pady=20, padx=10, sticky="ne")


        # Crear el label de intentos 
        if (self.auth):

            self.jugador_label = CTkLabel(self.frame, text_color="black", fg_color="#c2e9fc",
                                font=("", 16, "bold"), text='Nombre de jugador :'+ nombre_jugador,anchor="center" )
            self.jugador_label.grid(row=0, column=0, sticky="ne", padx=10 )
        else:
            self.jugador_label = CTkLabel(self.frame, text_color="black", fg_color="#c2e9fc",
                                font=("", 16, "bold"), text='Los resultados de este juego no se almacenarán',anchor="center" )
            self.jugador_label.grid(row=0, column=0, sticky="ne", padx=10 )


        # Crear el frame de la tabla
        
        self.frame1 = CTkFrame(self.frame, fg_color="#fa7a70", height=350, width=100, corner_radius=20)
        self.frame1.grid(row=0, column=0, pady=40, padx=10, sticky="")

        # Campos de entrada del numero

        self.number_entry = CTkEntry(self.frame, text_color="white", placeholder_text="Por favor, ingrese tu número", fg_color="#5f9ab8", placeholder_text_color="white",
                             font=("", 16, "bold"), width=400, corner_radius=10, height=45)
        self.number_entry.grid(row=1, column=0, sticky="nwe", padx=80 )

        #label de error
        self.error_label = CTkLabel(self.frame, text="", text_color="red", font=("", 12), anchor="center")
        self.error_label.grid(row=3, column=0, sticky="n", pady=3, padx=10)

        self.success_label = CTkLabel(self.frame, text="", text_color="green", font=("", 24 ,'bold'), anchor="center")
        self.success_label.grid(row=3, column=0, sticky="n", pady=0, padx=10)



        #Tabla de suposiciones 
        self.data = []
        self.inicializar_tabla()



        # Botones de acción
        self.btn_comprobar = CTkButton(self.frame, text="Comprobar", text_color="black", cursor="hand2", font=("", 15 ,"bold"),
                       border_width=0, fg_color="#c2e9fc", bg_color="#c2e9fc", command=self.verificar_entrada)
        self.btn_comprobar.grid(row=3, column=0, sticky="w", pady=60, padx=20)
        self.btn_comprobar.focus()
        self.number_entry.bind('<Return>', self.verificar_entrada_con_evento)  # Vincula el evento <Return> al campo de entrada


        self.btn_reiniciar = CTkButton(self.frame, text="Reiniciar", text_color="black", cursor="hand2", font=("", 15 ,"bold"),
                       border_width=0, fg_color="#c2e9fc", bg_color="#c2e9fc", command=self.reiniciar)
        self.btn_reiniciar.grid(row=3, column=0, sticky="ne", pady=60, padx=20)


    def anyadir_fila(self , numero , muertos, heridos):
        # Agregar la entrada actual a la tabla y limpiar el campo de entrada
        
        fila = [len(self.data) + 1, numero, muertos, heridos]
        self.data.append(fila)
        self.number_entry.delete(0, 'end')
        if self.debug_mode:
            
            print(self.data)
            # Actualizar la tabla
        self.actualizar_tabla(fila)


    def verificar_entrada(self):
        entrada = self.number_entry.get()
        resultado = self.gestor.verificar_entrada(entrada)
        #Mejorar la gestion del resultado TODO
        if  resultado[1] == "err":
            self.mostrar_error(resultado[0])
        elif resultado[1] == "success":
            
            
            # self.master.after(3000, self.reiniciar)
            #rep line 91
            self.error_label.configure(text="")
            if self.auth:
                self.gestor.termina_y_calcula_tiempo()
                self.success_label.configure(text='🥳🥳🥳'+resultado[0]+'🥳🥳🥳\n'+"¿Desea almacenar el resultado de su juego?")
                self.btn_comprobar.configure(text="Si")
                self.btn_reiniciar.configure(text="No")
                self.btn_comprobar.configure(command= self.confirmar_guardar_resultado)
                # self.gestor.actualizar_record(self.nombre_jugador)
            else:
                self.success_label.configure(text='🥳🥳🥳'+resultado[0]+'🥳🥳🥳')
            # self.actualizar_intentos()
        elif resultado[1] == 'end':
            self.mostrar_error(resultado[0])
            self.btn_reiniciar.focus()
            self.btn_reiniciar.bind('<Return>', self.reiniciar_con_evento) 
        else:
            self.anyadir_fila(entrada,resultado[0][0],resultado[0][1])
            #Vaciar el label del error

            # self.gestor.record_intentos() # type: ignore
            self.error_label.configure(text="")

    def confirmar_guardar_resultado(self):
        self.gestor.actualizar_record(self.nombre_jugador)
        self.success_label.configure(text='Se ha guardado el resultado correctamente')
        self.btn_comprobar.configure(text="")
        self.btn_reiniciar.configure(text="Reiniciar")



    def mostrar_error(self, mensaje ):
        self.error_label.configure(text=mensaje )


    # def preguntar_guardar_resultados(self):
    #     respuesta= self.number_entry.get().strip().lower()
    #     if respuesta == 's'


    def reiniciar(self):

        #Borrar todos los widgets dentro del frame1(no deja . Se borra todo el frame . En este caso , se usa destroy )
        self.frame1.destroy()
        self.frame1 = CTkFrame(self.frame, fg_color="#fa7a70", height=350, width=100, corner_radius=20)
        self.frame1.grid(row=0, column=0, pady=60, padx=10, sticky="")
        self.data=[]
        self.error_label.configure(text="" )
        self.success_label.configure(text="")
        self.gestor = Gestor(self.debug_mode)       
        self.inicializar_tabla()
        self.number_entry.delete(0, 'end')
        self.btn_comprobar.configure(command=self.verificar_entrada)
        self.btn_comprobar.configure(text="Comprobar")
        self.btn_reiniciar.configure(text="Reiniciar")





    def inicializar_tabla(self):
        # Crear encabezados de tabla
        header_labels = ["#", "Número", "Muertos","Heridos"]
        for i, header_text in enumerate(header_labels):
            header_label = CTkLabel(self.frame1, text=header_text, font=("", 14, "bold"), width=20)
            header_label.grid(row=2, column=i, padx=35, pady=2)
        self.gestor.empieza_cuenta_de_tiempo()


    def actualizar_tabla(self, fila):
    # Llenar la tabla con la nueva fila
        row = len(self.data) + 5  # +5 para evitar la superposición con los encabezados
        for col, cell_data in enumerate(fila):
            cell_label = CTkLabel(self.frame1, text=cell_data, font=("", 15,'bold'), width=20, fg_color="#fa7a70", bg_color="white")
            cell_label.grid(row=row, column=col, padx=35, pady=0)


    def verificar_entrada_con_evento(self, event):
        self.verificar_entrada()
    def reiniciar_con_evento(self, event):
        self.reiniciar()

        

    def run(self):
        self.master.after(0, lambda: self.master.state('zoomed'))

        self.master.mainloop()






        
    

