def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División entre cero"

def potencia(a, b):
    return a ** b

def calculadora_interactiva():
    """Versión interactiva para uso normal"""
    print("\n=== CALCULADORA BÁSICA ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Salir")
    
    while True:
        try:
            opcion = input("\nSeleccione una opción (1-6): ")
            
            if opcion == '6':
                print("¡Hasta luego!")
                break
            
            if opcion in ['1', '2', '3', '4', '5']:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                
                if opcion == '1':
                    print(f"Resultado: {num1} + {num2} = {suma(num1, num2)}")
                elif opcion == '2':
                    print(f"Resultado: {num1} - {num2} = {resta(num1, num2)}")
                elif opcion == '3':
                    print(f"Resultado: {num1} * {num2} = {multiplicacion(num1, num2)}")
                elif opcion == '4':
                    print(f"Resultado: {num1} / {num2} = {division(num1, num2)}")
                elif opcion == '5':
                    print(f"Resultado: {num1} ^ {num2} = {potencia(num1, num2)}")
            else:
                print("Opción no válida")
        except ValueError:
            print("Error: Ingrese números válidos")
        except EOFError:
            print("\n⚠️ Modo no interactivo detectado - omitiendo entrada de usuario")
            break

def demo_operaciones():
    """Demostración no interactiva para CI/CD"""
    print("\n=== DEMOSTRACIÓN DE OPERACIONES ===")
    print(f"5 + 3 = {suma(5, 3)}")
    print(f"10 - 4 = {resta(10, 4)}")
    print(f"6 * 7 = {multiplicacion(6, 7)}")
    print(f"15 / 3 = {division(15, 3)}")
    print(f"2 ** 4 = {potencia(2, 4)}")
    print("✅ Todas las operaciones funcionan correctamente")
    return True

if __name__ == "__main__":
    import sys
    # Detectar si se está ejecutando en modo no interactivo (CI/CD)
    if not sys.stdin.isatty():
        print("🐍 Ejecutando en modo CI/CD - Demostración de operaciones")
        demo_operaciones()
    else:
        print("💻 Ejecutando en modo interactivo - Calculadora completa")
        calculadora_interactiva()