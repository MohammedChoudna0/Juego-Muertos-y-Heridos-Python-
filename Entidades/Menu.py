from Entidades.LoginPage import LoginPage
from Entidades.RankingPage import GameRanking
from customtkinter import CTk, CTkFrame, CTkEntry, CTkButton, CTkLabel, CTkImage, CTkToplevel



class GameApp:
    def __init__(self , debug_mode=False):

        # Configurar ventana prinicpal
        self.master = CTk()
        self.debug_mode = debug_mode 
        self.master.configure(fg_color="#00ccff")
        self.frame = CTkFrame(self.master, width=450, height=300 , fg_color="#c2e9fc", bg_color="#00ccff", corner_radius=50 , border_width=5)
        self.frame.place(relx=0.5, rely=0.5, anchor='center')

        # Titulo
        label = CTkLabel(self.frame, text="Juego de Muertos y Heridos", font=("Arial", 25 , 'bold'),text_color='black')
        label.place(relx=0.5, rely=0.1, anchor='center')

        #Los 3 botones de menu
        play_button = CTkButton(self.frame, text="Jugar", command=self.play ,width=350 , height=35 ,corner_radius=50)
        play_button.place(relx=0.5, rely=0.3, anchor='center')

        ranking_button = CTkButton(self.frame, text="Ranking", command=self.ranking, width=350 , height=35 ,corner_radius=50)
        ranking_button.place(relx=0.5, rely=0.5, anchor='center')

        exit_button = CTkButton(self.frame, text="Salir", command=self.master.destroy ,width=350 , height=35 ,corner_radius=50)
        exit_button.place(relx=0.5, rely=0.7, anchor='center')

    #función play cierra la ventana actual y abre la ventana login
    
    def play(self):
        
        self.master.destroy()
        master = LoginPage(self.debug_mode)
        master.run()
    
    #función que cierra la ventana actual y abre la ventana ranking
    def ranking(self):
        self.master.withdraw()
        master=GameRanking(self)
        master.run()
    
    #Mostrar la ventana y en modo pantalla completa 
    def run(self):
        self.master.after(0, lambda: self.master.state('zoomed'))
        self.master.mainloop()





