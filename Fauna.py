﻿from Animales import Animales
from Gato import Gato
from Perro import Perro
from AnimalesConMenu import ListaAnimales

def menu(self):
        while True:
            print("\n---- Menu ----")
            print("1. Mostrar lista de animales")
            print("2. Agregar nuevo perro")
            print("3. Agregar nuevo gato")
            print("4. Salir")
            opcion = input("Inserta una opción: ")

            if opcion == "1":
                self.mostrar_animales()
            elif opcion == "2":
                nombre = input("Inserta el nombre del perro: ")
                edad = int(input("Inserta la edad del perro: "))
                nuevo_perro = Perro(nombre, edad)
                self.agregar_animal(nuevo_perro)
                print("Perro agregado correctamente.")
            elif opcion == "3":
                nombre = input("Inserta el nombre del gato: ")
                edad = int(input("Inserta la edad del gato: "))
                nuevo_gato = Gato(nombre, edad)
                self.agregar_animal(nuevo_gato)
                print("Gato agregado correctamente.")
            elif opcion == "4":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, elije una opción válida.")


def main():
    lista_animales = ListaAnimales()
    lista_animales.menu()
    

if __name__ == "__main__":
    main()





