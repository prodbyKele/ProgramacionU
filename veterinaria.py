import os
class dogs:
    def __init__(self, name= "", age = "", race = "", weight = "", size = "", owner = "", status = False ):
        self.name = name
        self.age = age
        self.race = race
        self.cowner = owner
        self.weight = weight
        self.size = size
        self.status = status
        
    def register(self):
        self.name = input("Ingrese el nombre de su perro: ")
        self.age = int(input("Ingrese la edad de su perro: "))
        self.race = input("Ingrese la raza de su perro: ")
        self.weight = float(input("Ingrese el peso de su perro: "))
        self.owner = input("Ingrese su nombre(Dueño): ")
        self.status = True
       
    def size_Change(self):
        if self.weight <= 10:
            self.weight = "Perro pequeño"
        else:
            self.weight = "Perro grande"
    
    def registered(self):
        if self.status == False:
            print(f"El estado de su perro es: {self.status}")
        elif self.status == True:
            print(f"El estado de su perro es: {self.status}")
            
    def show_info(self):
        print(f"Nombre: {self.name}")
        print(f"Edad: {self.age}")
        print(f"Raza: {self.race}")
        print(f"Peso: {self.weight}")
        print(f"Tamanio: {self.size}")
        print(f"Dueño: {self.owner}")
        
def menu():
    on = True
    perro1 = dogs()
    records = {}
    
    while on:
        os.system("cls")
        print("\t\t ===== VETONLINE =====")
        print("\t\t 1. Registar perro")
        print("\t\t 2. Mostrar informacion")
        print("\t\t 3. Salir del programa")
        opt = int(input("Ingrese la opcion que desea realizar: "))
        
        if opt == 1:
            os.system("cls")
            reg_num = int(input("Ingrese el numero de registro: "))
            records[reg_num] = perro1.register()
            print("Su perro ha sido registrado")
            input("Presione ENTER para continuar...")
            
        elif opt == 2:
            os.system("cls")
            perro1.size_Change()
            #perro1.show_info()
            for i in records:
                print(records[i])
            
            input("Presione ENTER para contiunar...")
            
        elif opt == 3:
            os.system("cls")
            on = False
            print("Gracias por utilizar VetOnline")
            input("Presione ENTER para salir...")
            
        else:
            os.system("cls")
            print("Ingrese un opcion valida :(")
            input("Presione ENTER para regresar...")
        
menu()