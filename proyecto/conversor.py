# Conversor de Temperatura en Python
# Proyecto para el Taller Individual de GitHub - Opción B

def celsius_a_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    """Convierte grados Fahrenheit a Celsius."""
    return (fahrenheit - 32) * 5/9

def mostrar_menu():
    print("\n" + "=" * 30)
    print("   CONVERSOR DE TEMPERATURA   ")
    print("=" * 30)
    print("1. Convertir Celsius a Fahrenheit")
    print("2. Convertir Fahrenheit a Celsius")
    print("3. Salir")
    print("=" * 30)

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-3): ").strip()
        
        if opcion == "3":
            print("\n¡Gracias por usar el conversor! Hasta luego.")
            break
            
        if opcion in ["1", "2"]:
            try:
                temp = float(input("\nIngrese el valor de la temperatura a convertir: "))
                
                if opcion == "1":
                    resultado = celsius_a_fahrenheit(temp)
                    print(f"\n---> {temp}°C equivalen a {resultado:.2f}°F")
                elif opcion == "2":
                    resultado = fahrenheit_a_celsius(temp)
                    print(f"\n---> {temp}°F equivalen a {resultado:.2f}°C")
                    
            except ValueError:
                print("\n Error: Debe ingresar un valor numérico válido.")
        else:
            print("\n Opción no válida. Por favor, seleccione 1, 2 o 3.")

if __name__ == "__main__":
    main()
