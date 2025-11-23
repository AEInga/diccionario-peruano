# -*- coding: utf-8 -*-
"""
Diccionario Peruano 🇵🇪

Pequeña aplicación de línea de comandos para consultar
palabras y expresiones típicas del Perú.
"""

DICCIONARIO = {
    "jato": "Casa, hogar. Ejemplo: 'Nos vemos en mi jato a las 8.'",
    "pata": "Amigo, compañero. Ejemplo: 'Ese pata es de la universidad.'",
    "chela": "Cerveza. Ejemplo: 'Vamos por unas chelas el viernes.'",
    "yapa": "Extra que se da al comprar algo. Ejemplo: '¿Me das la yapa, casero?'",
    "chamba": "Trabajo. Ejemplo: 'Estoy buscando chamba desde hace un mes.'",
}


def mostrar_menu():
    print("=== Diccionario Peruano 🇵🇪 ===")
    print("1. Buscar palabra")
    print("2. Listar todas las palabras")
    print("3. Salir")


def buscar_palabra():
    termino = input("Ingresa la palabra que quieres buscar: ").strip().lower()
    definicion = DICCIONARIO.get(termino)
    if definicion:
        print(f"\n{termino}:\n  {definicion}\n")
    else:
        print(f"\nNo se encontró la palabra '{termino}' en el diccionario.\n")


def listar_palabras():
    print("\nPalabras disponibles:")
    for palabra in sorted(DICCIONARIO.keys()):
        print(f"- {palabra}")
    print("")


def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-3): ").strip()

        if opcion == "1":
            buscar_palabra()
        elif opcion == "2":
            listar_palabras()
        elif opcion == "3":
            print("¡Hasta luego, causa! 👋🇵🇪")
            break
        else:
            print("Opción no válida. Intenta de nuevo.\n")


if __name__ == "__main__":
    main()
