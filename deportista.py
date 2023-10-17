class Deportista():
    def __init__(self, deporte, añosPracticando):
        self.deporte = deporte
        self.añosPracticando = añosPracticando
    
    def __init__(self):
        self.deporte = "Futbol"
        self.añosPracticando  = 18
    
    def getDeporte(self):
        return self.deporte
    
    def setDeporte(self, deporte):
        self.deporte = deporte

    def getAñosPracticando(self):
        return self.añosPracticando
    
    def setAñosPracticando(self, añosPracticando):
        self.añosPracticando = añosPracticando



        