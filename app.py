import sys

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

def mostrar_menu():
    print("=" * 40)
    print("     CALCULADORA AVANZADA v2.0")
    print("=" * 40)
    print("1. ➕ Suma")
    print("2. ➖ Resta")
    print("3. ✖️ Multiplicación")
    print("4. ➗ División")
    print("5. 🚪 Salir")
    print("=" * 40)

def procesar_operacion(opcion, num1, num2):
    """Procesa la operación seleccionada y retorna el resultado"""
    if opcion == '1':
        return f"\n✨ Resultado: {num1} + {num2} = {suma(num1, num2)} ✨"
    elif opcion == '2':
        return f"\n✨ Resultado: {num1} - {num2} = {resta(num1, num2)} ✨"
    elif opcion == '3':
        return f"\n✨ Resultado: {num1} * {num2} = {multiplicacion(num1, num2)} ✨"
    elif opcion == '4':
        return f"\n✨ Resultado: {num1} / {num2} = {division(num1, num2)} ✨"

def calculadora(modo_test=False):
    """
    Calculadora interactiva
    
    Args:
        modo_test: Si es True, ejecuta pruebas automáticas en lugar de modo interactivo
    """
    if modo_test:
        # Ejecutar pruebas automáticas
        print("Ejecutando pruebas automáticas...")
        pruebas()
        return
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("\nSeleccione una opción (1-5): ")
            
            if opcion == '5':
                print("\n¡Hasta luego! 👋")
                break
            
            if opcion in ['1', '2', '3', '4']:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                
                resultado = procesar_operacion(opcion, num1, num2)
                print(resultado)
            else:
                print("\n⚠️ Opción no válida. Por favor, seleccione 1-5 ⚠️")
        except ValueError:
            print("\n❌ Error: Ingrese números válidos ❌")
        except EOFError:
            print("\n❌ Error: No se pudo leer la entrada del usuario ❌")
            break
        
        input("\nPresione Enter para continuar...")

def pruebas():
    """Función de pruebas automatizadas"""
    print("\n=== EJECUTANDO PRUEBAS ===\n")
    
    # Pruebas de operaciones básicas
    assert suma(5, 3) == 8, "Error en suma"
    print("✅ Prueba de suma: OK")
    
    assert resta(10, 4) == 6, "Error en resta"
    print("✅ Prueba de resta: OK")
    
    assert multiplicacion(6, 7) == 42, "Error en multiplicación"
    print("✅ Prueba de multiplicación: OK")
    
    assert division(10, 2) == 5, "Error en división"
    print("✅ Prueba de división: OK")
    
    assert division(5, 0) == "Error: División entre cero", "Error en división por cero"
    print("✅ Prueba de división por cero: OK")
    
    # Pruebas de procesamiento de operaciones
    resultado = procesar_operacion('1', 2, 3)
    assert "2 + 3 = 5" in resultado, "Error en procesar operación suma"
    print("✅ Prueba de procesar operación suma: OK")
    
    resultado = procesar_operacion('4', 10, 2)
    assert "10 / 2 = 5" in resultado, "Error en procesar operación división"
    print("✅ Prueba de procesar operación división: OK")
    
    print("\n=== TODAS LAS PRUEBAS PASARON EXITOSAMENTE ===")

if __name__ == "__main__":
    # Verificar si se ejecuta en modo prueba (GitHub Actions) o interactivo
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        calculadora(modo_test=True)
    else:
        try:
            calculadora(modo_test=False)
        except EOFError:
            print("\n❌ Error: No hay entrada disponible. Use 'python app.py --test' para ejecutar pruebas")
            sys.exit(1)