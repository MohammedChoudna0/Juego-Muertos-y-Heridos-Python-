class Jugador:
    def __init__(self, nombre, pin, record_intentos=0, record_tiempo=0.0):
        self.__nombre = nombre
        self.__pin = pin
        self.__record_intentos = record_intentos
        self.__record_tiempo = record_tiempo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, nuevo_pin):
        self.__pin = nuevo_pin


    @property
    def record_intentos(self):
        return self.__record_intentos

    @record_intentos.setter
    def record_intentos(self, nuevo_record_intentos):
        self.__record_intentos = nuevo_record_intentos

    @property
    def record_tiempo(self):
        return self.__record_tiempo

    @record_tiempo.setter
    def record_tiempo(self, nuevo_record_tiempo):
        if nuevo_record_tiempo >= 0.0:
            self.__record_tiempo = nuevo_record_tiempo

    def __str__(self):
        return f"Jugador: {self.__nombre}, Récord de Intentos: {self.__record_intentos}, Récord de Tiempo: {self.__record_tiempo} segundos"
    

    def __eq__(self, other):
        if isinstance(other, Jugador):
            return self.nombre == other.nombre
        return False
    

