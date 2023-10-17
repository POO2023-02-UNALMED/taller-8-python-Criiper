from persona import Persona
from deportista import Deportista

class Futbolista(Persona, Deportista):
    listaFutbolistas = []

    def __init__(self, nombre, edad, altura, sexo, deporte, añosPracticando, _golesMarcados, _tarjetasRojas, _piernaHabil):
        super(Persona).__init__(nombre, edad, altura, sexo)
        super(Deportista).__init__(deporte, añosPracticando)
        self._golesMarcados = _golesMarcados
        self._tarjetasRojas = _tarjetasRojas
        self._piernaHabil = _piernaHabil

        Futbolista.listaFutbolistas.append(self)


    def __str__(self):
        return (f"Mi nombre es {self.getNombre()} soy profesional en el deporte {self.getDeporte()} Tengo {self.getEdad()} años de edad y llevo {self.getAñosPracticando()} Participando años en el deporte")
