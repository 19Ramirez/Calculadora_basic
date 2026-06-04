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

def calculadora():
    print("\n=== CALCULADORA BÁSICA ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    
    while True:
        try:
            opcion = input("\nSeleccione una opción (1-5): ")
            
            if opcion == '5':
                print("¡Hasta luego!")
                break
            
            if opcion in ['1', '2', '3', '4']:
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
            else:
                print("Opción no válida")
        except ValueError:
            print("Error: Ingrese números válidos")

if __name__ == "__main__":
    calculadora()