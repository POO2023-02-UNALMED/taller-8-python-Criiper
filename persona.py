class Persona():
    def __init__(self, nombre, edad, altura, sexo):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.sexo = sexo

    def __init__(self):
        self.nombre = "No Define"
        self.edad = 18
        self.altura = "1.80"
        self.sexo = "No Define"   
    
    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def getEdad(self):
        return self.Edad
    
    def setEdad(self, edad):
        self.edad = edad

    def getAltura(self):
        return self.altura
    
    def setAltura(self, altura):
        self.altura = altura

    def getSexo(self):
        return self.sexo
    
    def setSexo(self, sexo):
        self.sexo = sexo