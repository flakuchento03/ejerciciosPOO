class Automovil:
    def __init__(self, marca, modelo, color, puertas, anio, precio):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.puertas = puertas
        self.anio = anio
        self.precio = precio

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.anio}) - {self.color}, {self.puertas} puertas, ${self.precio}"


class Concesionaria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.autos = []  

    def agregar_auto(self, auto):
        self.autos.append(auto)
        print(f"Automóvil agregado: {auto}")

    def eliminar_auto(self, modelo):
        for auto in self.autos:
            if auto.modelo == modelo:
                self.autos.remove(auto)
                print(f"Automóvil eliminado: {auto}")
                return
        print("No se encontró un automóvil con ese modelo.")

    def mostrar_autos(self):
        if not self.autos:
            print("No hay automóviles en la concesionaria.")
        else:
            print(f"Automóviles en {self.nombre}:")
            for auto in self.autos:
                print(" -", auto)





Carro1 = Automovil("Honda", "Civic", "Azul", 4, 2010, 80000)
Carro2 = Automovil("Chevrolet", "Aveo", "Blanco", 4, 2017, 70000)

concesionaria = Concesionaria("Autos Felix")
concesionaria.agregar_auto(Carro1)
concesionaria.agregar_auto(Carro2)
concesionaria.mostrar_autos()
