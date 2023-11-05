import time
from Entidades.ManejoDeArchivos import ManejadorDeArchivos
from Entidades.Jugador import Jugador
from Entidades.Juego import *

class Gestor:
    # Al instanciar el objeto gestor , se crea la lista de jugadores recuperada desde el fichero
    def __init__(self, debug_mode=False):
        self.__jugadores = self.__procesar_datos()  
        self.__juego =Juego()
        self.nombre_jugador = ""
        self.__tiempo_inicio = 0
        self.__record_tiempo = 0
        self.__record_intentos = 0
        self.debug_mode = debug_mode

    @property 
    def record_intentos(self):
        return self.__record_intentos

    # Devuelve los datos del fichero de usuario
    def __devolver_datos(self):
        fichero = "app/data/usuarios.txt"
        manejador = ManejadorDeArchivos(fichero)
        return manejador.leer_archivo()

    # Procesa los datos de los usuarios y crea la lista de jugadores
    def __procesar_datos(self):
        contenido = self.__devolver_datos()  
        lista_jugadores = []

        lineas = contenido.split('\n')  

        for linea in lineas:
            if linea:
                datos = linea.split('*')
                if len(datos) == 4:
                    nombre, pin, record_intentos, record_tiempo = datos
                    jugador = Jugador(nombre, pin, int(record_intentos), float(record_tiempo))
                    lista_jugadores.append(jugador)

        return lista_jugadores
    
    def jugadores(self):
        return self.__jugadores
    
    
    def buscar_usuario(self, nombre):
        for jugador in self.__jugadores:
            if nombre == jugador.nombre:
                return jugador
        return None

    #si no encuentra el usuario lo agrega
    def agregar_usuario(self, nombre, pin):
        if self.buscar_usuario(nombre) is None:
            jugador = Jugador(nombre, pin, 0, 0)
            self.__jugadores.append(jugador)
            self.escribir_usuario(jugador)
            return ""

        else :
            return "Ya existe un usuario con el mismo nombre"

    def autenticar_usuario(self, nombre, pin):
        jugador = self.buscar_usuario(nombre)
        if jugador is None:
            return "El usuario no existe"  
        if jugador.pin != pin:
            return "Datos de acceso incorrectos"  
        return "" 
    
    #Usa la clase ManejadorDeArchivos para leer y escribir el archivo (Sobreescribe)
    def escribir_usuario(self, jugador):
        fichero = "app/data/usuarios.txt"
        manejador = ManejadorDeArchivos(fichero)
        contenido = ''
        for jugador in self.__jugadores:
            contenido += f"{jugador.nombre}*{jugador.pin}*{jugador.record_intentos}*{jugador.record_tiempo}\n"

        resultado = manejador.escribir_archivo(contenido)

        return resultado



    def verificar_entrada(self,entrada):
        # Hay que arreglar el intentos
        if self.debug_mode:
            print("\x1b[31m" + "Intento Nº",str(self.__juego.intentos) + "\x1b[0m")
            print("\x1b[31m" + "Número secreto es: ",self.__juego.get_numero_secreto + "\x1b[0m")

        return self.__juego.validar_entrada(entrada)
    


    #Ordena la lista en funcion de los intentos y tiempo
    def ordenar_lista(self,lista_jugadores):
        def criterio_orden(jugador):
            return (jugador.record_intentos, jugador.record_tiempo)
        #Filtrar los jugadores que tienen 0 intentos no han jugador nunca  o no han guardado nunca su record
        lista_jugadores = [jugador for jugador in lista_jugadores if jugador.record_intentos > 0]
        lista_ordenada = sorted(lista_jugadores, key=criterio_orden)
        return lista_ordenada  

    #Arranca el contador
    def empieza_cuenta_de_tiempo(self):
        self.__tiempo_inicio = time.time()

    #Calcula el tiempo correspondiente de la partida
    def termina_y_calcula_tiempo(self):
        tiempo_fin = time.time()
        self.__record_tiempo = tiempo_fin - self.__tiempo_inicio
        self.__record_tiempo = round(self.__record_tiempo, 3)
        return self.__record_tiempo
    
    #borra el usuario de la lista y lo añade de nuevo sobreescribiendo el archivo
    def actualizar_record(self ,nombre):
         jugador = self.buscar_usuario(nombre)
         if jugador is not None:
            jugador_actualizado = Jugador(nombre,jugador.pin,self.__juego.intentos,self.__record_tiempo)
            if self.debug_mode:
                print( "Jugador actualizado",jugador_actualizado)
            self.__jugadores.remove(jugador)
            self.__jugadores.append(jugador_actualizado)
            self.escribir_usuario(jugador_actualizado)
                




