class Libro:
    def __init__(self, titulo, autor, anio, precio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.precio = precio

    def __str__(self):
        return f"'{self.titulo}' de {self.autor} ({self.anio}) - ${self.precio}"


class Libreria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = [] 

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro agregado: {libro}")

    def eliminar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                self.libros.remove(libro)
                print(f"Libro eliminado: {libro}")
                return
        print("No se encontró un libro con ese título.")

    def mostrar_libros(self):
        if not self.libros:
            print("No hay libros en la librería.")
        else:
            print(f"Libros en {self.nombre}:")
            for libro in self.libros:
                print(" -", libro)



libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967, 350)
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605, 500)


mi_libreria = Libreria("Librería Central")


mi_libreria.agregar_libro(libro1)
mi_libreria.agregar_libro(libro2)


mi_libreria.mostrar_libros()


mi_libreria.eliminar_libro("Cien Años de Soledad")


mi_libreria.mostrar_libros()


