import os
class Book:
    def __init__(self, title="", author="", isbn="", year="", status = "DISPONIBLE"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.status = status
        
    
    def createBook(self):
        self.title = input("Ingrese el título el libro: ")
        self.author = input("Ingrese el autor el libro: ")
        self.isbn = input("Ingrese el ISBN el libro: ")
        self.year = input("Ingrese el año de publicación el libro: ")
        self.status = "DISPONBILE"
        
    def borrow_book(self):
        self.status = "PRESTADO"
        print("El libro ha sido prestado...")
    
    def return_book(self):
        self.status = "DISPONIBLE"
        print("El libro ha sido regresado...")
        
    def show_book(self):
        print(f"Título: {self.title}" )
        print(f"Autor: {self.author}" )
        print(f"ISBN: {self.isbn}" )
        print(f"Año de Publicación: {self.year}" )
        print(f"Estado: {self.status}\n" )
        
def menu():
    on = True
    book1 = Book()
    
    while on:
        os.system("cls")
        
        print("\t==========> MENU <=========")
        print("\t\t1. Crear un libro")
        print("\t\t2. Prestar un libro")
        print("\t\t3. Devolver un libro")
        print("\t\t4. Mostrar libro")
        print("\t\t5. Salir del programa")
        option = int(input("Ingrese la opción que desee: "))
        
        if option == 1:
            os.system("cls")
            book1.createBook()
            print("El libro ha sido creado")
        
        elif option == 2:
            os.system("cls")
            print("El libro ha sido prestado...")
            book1.borrow_book()
            input()
            
        elif option == 3:
            os.system("cls")
            print("El libro ha sido regresado...")
            book1.return_book()
            input()
        
        elif option == 4:
            os.system("cls")
            book1.show_book()
            input()
        
        elif option == 5:
            print("Gracias por usar el programa")
            on = False
            
        else:
            print("Ingrese una opción válida")
            os.system("cls")
            input()
menu()
    
