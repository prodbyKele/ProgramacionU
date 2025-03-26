import os
import time


#global option

class Dog:
    name = " "
    breed = " "
    color = " "
    weight = 0
    age = 0

    def __init__(self):
        pass

    def add_dog(self, name, breed, color, weight, age):
        self.name = name
        self.breed = breed
        self.color = color
        self.weight = weight
        self.age = age
        print("El perro se ha agregado satisfactoriamente :)")
    
    def __str__(self):
        return f"{self.name}\t {self.breed}\t {self.color}\t {self.weight}\t {self.age}"

dogs_list = []


def menu():
    on = True

    while on:
        os.system("cls")
        #global option
        print("-----> DICCIONARIO DE PERROS <-----")
        print("\t1. Crear perro")
        print("\t2. Agregar datos de perro")
        print("\t3. Lista de perros")
        print("\t4. Salir")

        opt = int(input("Ingrese la opción que desea: "))

        if opt == 1:
            os.system("cls")

            new_dog = Dog()

            print("El perro ha sido creado :D")
            input("Presione ENTER para regresar :)")

        elif opt == 2:
            os.system("cls")

            name = input("Ingrese el nombre del perro: ")
            breed = input("Ingrese la raza del perro: ")
            color = input("Ingrese el color del perro: ")
            weight = int(input("Ingrese el peso del perro: "))
            age = int(input("Ingrese la edad del perro: "))

            new_dog.add_dog(name, breed, color, weight, age)
            dogs_list.append(new_dog)

            input()

        elif opt == 3:
            os.system("cls")
            print("Nombre\t | Raza\t | Color\t | Peso\t | Edad")
            print("-"*50)
            for dog in dogs_list:
                print(dog)
                
            input("Presione ENTER para regresar al menu :)")
        
        elif opt == 4:
            os.system("cls")
            on = False
            print("Gracias por registrar a tu perro :)")
            input("Presion ENTER para salir...")
        
        else:
            os.system("cls")
            print("Ingrese una opción válida :(")
            input("Presione ENTER para volver a intententar...")


menu()
    

    