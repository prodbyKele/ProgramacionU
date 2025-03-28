import os

class Workshop:
    def __init__(self):
        pass
    
    def add_car(self):
        self.owner = input("Ingrese el duenio del vehiculio: ")
        self.manufacturer = input("Ingrese el fabricante de su vehiculo: ")
        self.model = input("Ingrese el modelo de su vehiculo: ")
        self.color = input("Ingrese el color de su vehiculo: ")
        self.type = input("Ingrese el tipo de vehiculo: ")
        self.status = "EN REPARACION"
        return f"{self.owner}\t|\t{self.manufacturer}\t\t|\t{self.model}\t|\t{self.color}\t|\t{self.type}\t|\t{self.status}"
    
    def __str__(self):
        pass
    

def menu():
    on = True
    os.system("cls")
    cars_list = list()
    
    while on:
        os.system("cls")
        print("-----> MENU DEL TALLER <-----")
        print("\t1. Agregar vehiculo")
        print("\t2. Entregar vehiculo")
        print("\t3. Listar vehiculo")
        print("\t4. Salir")
        opt = int(input("Ingrese la opcion que desea agregar: "))
        
        if opt == 1:
            os.system("cls")
            car = Workshop()
            cars_list.append(car.add_car())
            print("El vehiculo ha sido agregado satisfactoriamente :)")
            input("Presione ENTER para regresar al menu...")
            
        elif opt == 2:
            os.system("cls")
            if not cars_list:
                print("No hay vehiculos en el taller.")
            else:
                print("Seleccione el vehiculo a entregar:")
                for index, car in enumerate(cars_list):
                    print(f"{index + 1}. {car}")
                
                try:
                    car_index = int(input("Ingrese el numero del vehiculo a entregar: ")) - 1
                    if 0 <= car_index < len(cars_list):
                        delivered_car = cars_list[car_index]
                        #delivered_car.status = "ENTREGADO"
                        print(f"Vehiculo entregado: {delivered_car}")
                        cars_list.pop(car_index) 
                    else:
                        print("Numero de vehiculo invalido.")
                except ValueError:
                    print("Por favor, ingrese un numero valido.")
            input("Presione ENTER para regresar al menu...")
            
            
        elif opt == 3:
            os.system("cls")
            print("Duenio\t|\tFabricante\t|\tModelo\t|\tColor\t|\tTipo\t|\tEstado")
            print("=-"*50)
            for i in cars_list:
                print(i)
            input("Presione ENTER para regresar al menu...")
            
        elif opt == 4:
            os.system("cls")
            on = False
            print("Gracias por utilizar el programa :(")
            input("Presione ENTER para salir...")
            
        else:
            os.system("cls")
            print("Ingrese una opcion valida :(")
            input("Presion ENTER para volver a intentar")
            
menu()