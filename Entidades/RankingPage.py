from customtkinter import CTk, CTkFrame, CTkEntry, CTkButton, CTkLabel, CTkImage,CTkScrollableFrame

from Entidades.GestorDeJuego import Gestor
from Entidades.Menu import *

class GameRanking:
    def __init__(self ,root):
        self.root = root
        self.master = CTk()
        self.master.title("Ranking de Jugadores")
        self.master.config(bg="#b3fbff")
        self.gestor = Gestor()

        self.data = [] 

        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_rowconfigure(1, weight=1)

        # Crear el frame de la tabla
        self.frame1 = CTkScrollableFrame(self.master, fg_color="#c2e9fc", bg_color="#b3fbff", height=600, width=500, corner_radius=20,border_width=5 ,border_color="#fc7703")
        self.frame1.grid(row=0, column=0, pady=20, padx=10, sticky="ne")
                #Boton Volver 
        self.volverAtras = CTkButton(self.frame1, text="⬅️", font=("", 15, "bold"), height=30, width=40, fg_color="#0085FF", cursor="hand2",
            corner_radius=15, command=self.volver)
        
        self.volverAtras.grid(row=0, column=0, sticky="nw", pady=0, padx=0)

        self.inicializar_tabla()
        self.crear_filas_ordenadas()

    #Por cada jugador de lista ordenada obtenida de la clase gestor se crea una nueva fila y se actualiza la tabla
    def crear_filas_ordenadas(self):
    
        self.data = []
        lista_ordenada = self.gestor.ordenar_lista(self.gestor.jugadores())
        for jugador in lista_ordenada:

            nombre = jugador.nombre
            intentos = jugador.record_intentos
            tiempo = jugador.record_tiempo

            fila = [nombre, intentos, tiempo]
            self.data.append(fila)
            self.actualizar_tabla(fila)

    def volver(self):
        self.root.master.after(0, lambda: self.root.master.state('zoomed'))
        self.root.master.deiconify()
        self.master.destroy()


    def inicializar_tabla(self):
        # Crear encabezados de tabla
        cabecera_etiquetas = ["Nombre", "Intentos", "Tiempo"]
        for i, cabecera in enumerate(cabecera_etiquetas):
            cabecera_etiqueta = CTkLabel(self.frame1, text=cabecera, font=("", 24, "bold"), width=20 , text_color="#fc7703")
            cabecera_etiqueta.grid(row=2, column=i, padx=30, pady=2)

    def actualizar_tabla(self, fila):

    # Llenar la tabla con la nueva fila
        row = len(self.data) + 5  # +5 para evitar la superposición con los encabezados
        for col, cell_data in enumerate(fila):
            cell_label = CTkLabel(self.frame1, text=cell_data, font=("", 24 ,"bold"), width=20,text_color="black")
            cell_label.grid(row=row, column=col, padx=30, pady=0)

    
    def run(self):
        self.master.after(0, lambda: self.master.state('zoomed'))
        self.master.mainloop()


