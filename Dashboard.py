import os
from colorama import init, Fore, Style

# Inicializa colorama para color en terminal
init(autoreset=True)


def mostrar_codigo(ruta_script):
    """
    Muestra el contenido del script especificado en consola con formato de color.
    """
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            print(Fore.CYAN + f"\n--- Código de {ruta_script} ---\n")
            print(Fore.GREEN + archivo.read())
    except FileNotFoundError:
        print(Fore.RED + "❌ El archivo no se encontró.")
    except Exception as e:
        print(Fore.RED + f"⚠️ Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    """
    Muestra un menú interactivo que permite al usuario ver o ejecutar scripts de ejemplo.
    """
    ruta_base = os.path.dirname(__file__)  # Directorio actual del archivo

    # Diccionario con las rutas relativas de los scripts del curso
    opciones = {
        '1': 'UNIDAD 1/1.2. Tecnicas de Programacion/1.2.1. Ejemplo Tecnicas de Programacion.py',
        '2': 'UNIDAD 2/2.1. Clases y Objetos/2.1.1. Ejemplo Clases.py',
        '3': 'UNIDAD 3/Herencia/3.1.1. Ejemplo Herencia.py',
        '4': 'UNIDAD 4/Polimorfismo/4.1.1. Ejemplo Polimorfismo.py'
        # Agrega más scripts si lo deseas
    }

    while True:
        print(Fore.YELLOW + "\n📚 Menú Principal - Dashboard de POO")
        print("Selecciona una opción para ver el código:\n")

        for key in opciones:
            print(f" {key}. {opciones[key]}")
        print(" 0. Salir")

        eleccion = input("\n🔸 Elige una opción: ")

        if eleccion == '0':
            print(Fore.YELLOW + "\n👋 Saliendo del dashboard. ¡Hasta luego!\n")
            break
        elif eleccion in opciones:
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)

            ejecutar = input(Fore.BLUE + "\n¿Deseas ejecutar este script? (s/n): ").lower()
            if ejecutar == 's':
                print(Fore.MAGENTA + "\n▶ Ejecutando script...\n")
                os.system(f'python "{ruta_script}"')
        else:
            print(Fore.RED + "Opción no válida. Intenta de nuevo.")


# Punto de entrada del programa
if __name__ == "__main__":
    mostrar_menu()
