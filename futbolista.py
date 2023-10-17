from persona import Persona
from deportista import Deportista

class Futbolista(Persona, Deportista):
    listaFutbolistas = []

    def __init__(self, nombre, edad, altura, sexo, añosPracticando, _golesMarcados, _tarjetasRojas, _piernaHabil):
        super().__init__()
        super(Deportista, self).__init__()
        self.setNombre(nombre)
        self.setEdad(edad)
        self.setAltura(altura)
        self.setSexo(sexo)
        self.setAñosPracticando(añosPracticando)
        self._golesMarcados = _golesMarcados
        self._tarjetasRojas = _tarjetasRojas
        self._piernaHabil = _piernaHabil

        Futbolista.listaFutbolistas.append(self)
    
    

    def getGolesMarcados(self):
        return self._golesMarcados
    
    def setGolesMarcados(self, _golesMarcados):
        self._golesMarcados = _golesMarcados
    
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    
    def setTarjetasRojas(self, _tarjetasRojas):
        self._tarjetasRojas = _tarjetasRojas

    def getPiernaHabil(self):
        return self._piernaHabil
    
    def setPiernaHabil(self, _piernaHabil):
        self._piernaHabil = _piernaHabil


    
    def __str__(self):
        return (f"Mi nombre es {self.getNombre()} soy profesional en el deporte {self.getDeporte()} Tengo {self.getEdad()} años de edad y llevo {self.getAñosPracticando()} Participando años en el deporte")
